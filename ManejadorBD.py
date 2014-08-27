import MySQLdb

class ManejadorBD():
	def __init__(self):
		self.direccion="localhost"
		self.user="root"
		self.passwor=""
		self.nombreBD="BaseEscuela"

	def conectar(self):
		self.BD = MySQLdb.connect(self.direccion,self.user,self.passwor,self.nombreBD )
		self.BD.autocommit(True)


	def desconectar(self):
		self.BD.close()


	def imprimirTablas(self):
		self.conectar()
		cursor=self.BD.cursor()
		cursor.execute("SELECT VERSION()")
		data = cursor.fetchone()
		print "Version Base de Datos : %s " % data
		print "Se conecto correctamente" 
		cursor.execute("USE BasePeliculas")
		cursor.execute("SHOW TABLES")
		tables = cursor.fetchall() 
		cont=0
		for (table_name,) in cursor:
			cont+=1
			print(table_name)
		print "numero de tablas: %d" %cont
		self.desconectar()


	def consulta(self,instrucion,tupla=()):
		self.conectar()
		cursor=self.BD.cursor()
		cursor.execute(instrucion,tupla)
		self.desconectar()
		cursor.close()
		return cursor

	def llamarProcedimineto(self, nombreProcedimiento, tupla=()):
		self.conectar()
		cursor=self.BD.cursor()
		cursor.callproc(nombreProcedimiento,tupla)
		resultado = cursor.fetchall()
		return resultado

	def consultarEstudiante(self):
		return self.llamarProcedimineto("consultarEstudiante")
		self.desconectar()

	def consultarPersonas(self):
		return self.llamarProcedimineto("consultarPersonas")
		self.desconectar()

	def consultarProfesores(self):
		return self.llamarProcedimineto("consultarProfesor")
		self.desconectar()

	def insertarProfesor(self, tupla):
		self.llamarProcedimineto("InsertarProfesor", tupla)
		self.BD.commit()
		self.desconectar()

	def editarProfesor(self,tupla):
		self.llamarProcedimineto("editarProfesor",tupla)
		self.BD.commit()
		self.desconectar()

	def obtenerCursos(self):
		return self.llamarProcedimineto("consultarCursos")
		self.desconectar()

	def consultarEstudiante2(self):
		return self.llamarProcedimineto("consultarEstudiante2")
		self.desconectar()

	def estudianteObtenerPersona(self, numCedula, tipoPersona):
		return self.llamarProcedimineto("EstudianteObtenerPersona",(numCedula, tipoPersona))
		self.desconectar()
	
	def agregarEstudianteEnCurso(self,curso,matricula):
		arg=(curso,matricula)
		self.llamarProcedimineto("agregarEstudianteEnCurso",arg)
		self.BD.commit()
		self.desconectar()

	def obtenerCursosPorProfesor(self,usuarioNombre):
		arg= (usuarioNombre,)
		return self.llamarProcedimineto('consultarCursosDelProfesor',arg)
		self.desconectar()

	def obtenerMateriasPorCurso(self,idCurso):
		return self.llamarProcedimineto("obtenerMateriasPorCurso",(idCurso,))
		self.desconectar()

	def agregarProfesorAMateriaDeCurso(self,curso,materia,profesor):
		arg=(curso,materia,profesor)
		self.llamarProcedimineto("ligarCursoConProfesor",arg)
		self.desconectar()

	def quitarProfesorDeMateria(self,curso,materia,profesor):
		arg=(curso,materia,profesor)
		self.llamarProcedimineto("desligarCursoConProfesor",arg)
		self.desconectar()

	def obtenerMateriaCursoProfesor(self,idCurso):
		return self.llamarProcedimineto("obtenerMateriaCursoProfesor",(idCurso,))
		self.desconectar()

	def obtenerInfoProfesor(self,cedula):
		return self.llamarProcedimineto("mostrarInfoProfesor",(cedula,))
		self.desconectar()

	def existeUsuarioProfesor(self,user):
		return self.llamarProcedimineto("existeUsuario",(user,))
		self.desconectar()

	def existeUsuarioRepetido(self,cedula,user):
		return self.llamarProcedimineto("existeUsuarioRepetido",(cedula,user))
		self.desconectar()

	def estudianteObtenerPersona(self, numCedula, tipoPersona):
		return self.llamarProcedimineto("EstudianteObtenerPersona",(numCedula, tipoPersona))
		self.desconectar()

	def agregarEstudianteEnCurso(self,curso,matricula):
		arg=(curso,matricula)
		self.llamarProcedimineto("agregarEstudianteEnCurso",arg)
		self.BD.commit()
		self.desconectar()

	def actualizarPersona(self,datos):
		self.llamarProcedimineto("editarPersonas",datos)
		self.BD.commit()
		self.desconectar()


	def crearPersona(self,datos):
		self.llamarProcedimineto("crearPersonas",datos)

	def consultarEstudiantesPorMateria(self,idCurso,materia,quimestre,parcial):
		arg=(idCurso,materia,quimestre,parcial)
		return self.llamarProcedimineto("consultarEstudiantesPorMateria",arg)

	def actualizarEstudianteActividad(self,idCurso,materia,quimestre,parcial,tipoActividad,matriculaEstudiante,nota):
		arg=(idCurso,materia,quimestre,parcial,tipoActividad,matriculaEstudiante,nota)
		self.llamarProcedimineto("actualizarEstudianteActividad",arg)
		self.BD.commit()
		self.desconectar()

	def consultarEstudiantesPorMateria(self,idCurso,materia,quimestre,parcial):
		return self.llamarProcedimineto("consultarEstudiantesPorMateria",(idCurso,materia,quimestre,parcial))

	def consultarExamenesPorCurso(self,idCurso,materia):
		return self.llamarProcedimineto("consultarExamenesPorCurso",(idCurso,materia))

	def consultarExamenPorQuimestre(self,idCurso,materia,quimestre):
		arg=(idCurso,materia,quimestre)
		return self.llamarProcedimineto("consultarExamenPorQuimestre",arg)

	def actualizarExamenPorQuimestre(self,id_curso,materia,quimestre,matriculaEstudiante,notaExamen):
		arg=(id_curso,materia,quimestre,matriculaEstudiante,notaExamen)
		self.llamarProcedimineto("actualizarExamenPorQuimestre",arg)
		self.BD.commit()
		self.desconectar()

	def actualizarNotasParcial(self,id_curso,materia,quimestre,parcial,matriculaEstudiante):
		arg=(id_curso,materia,quimestre,parcial,matriculaEstudiante)
		self.llamarProcedimineto("actualizarNotasParcial",arg)
		self.BD.commit()
		self.desconectar()

	def actualizarNotaQuimestre(self,id_curso,materia,quimestre,matriculaEstudiante):
		arg=(id_curso,materia,quimestre,matriculaEstudiante)
		self.llamarProcedimineto("actualizarNotaQuimestre",arg)
		self.BD.commit()
		self.desconectar()

	def consultarNotasParcial(self,id_curso,materia,quimestre):
		arg=(id_curso,materia,quimestre)
		return self.llamarProcedimineto("consultarNotasParcial",arg)

	def crearEstudiante(self,estudiante,padre,madre,representante,personaFactura):
		self.llamarProcedimineto("InsertarPersonaFactura",personaFactura)
		self.llamarProcedimineto("InsertarEstudiante",estudiante)
		self.crearPersona(padre)
		self.crearPersona(madre)
		self.crearPersona(representante)
		print padre[0]
		print madre[0]
		print representante[0]
		matricula=self.obtenerMatriculaEstudiante(estudiante[0])
		print matricula[0][0]
		tuplaPadre=(str(padre[0]),matricula[0][0],1)
		tuplaMadre=(str(madre[0]),matricula[0][0],2)
		tuplaRepre=(str(representante[0]),matricula[0][0],3)
		self.ligarEstudiantePersona(tuplaPadre)
		self.ligarEstudiantePersona(tuplaMadre)
		self.ligarEstudiantePersona(tuplaRepre)
		self.BD.commit()
		self.desconectar()


	def crearCurso(self,datos):
		self.llamarProcedimineto("crearCurso",datos)
		self.BD.commit()
		self.desconectar()

	def AsignarDirigente(self,datos):
		self.llamarProcedimineto("AsignarDirigente",datos)
		self.BD.commit()
		self.desconectar()

	def obtenerDeudas(self,matricula):
		return self.llamarProcedimineto("obtenerDeudas",(matricula,))
		self.desconectar()

	def generarFactura(self,deudas):
		self.llamarProcedimineto("crearFactura")
		self.BD.commit()
		facturas=self.llamarProcedimineto("obtenerFacturas")
		self.desconectar()
		factura=facturas[0]
		id_Factura=factura[0]
		for deuda in deudas:
			self.llamarProcedimineto("cancelarDeuda",(deuda,id_Factura))
		
		self.BD.commit()
		self.desconectar()


	def ligarEstudiantePersona(self,tupla):
		self.llamarProcedimineto("ligarEstudiantePersona",tupla)


	def validarLogguin(self,user,contra):
		pass

	def obtenerPersonaFactura(self,estudiante):
		return self.llamarProcedimineto("obtenerPersonaFactura",(estudiante,))
		self.desconectar()

	def obtenerMatriculaEstudiante(self,cedula):
		return self.llamarProcedimineto("obtenerMatriculaEstudiante",(cedula,))
		self.desconectar()



	def obtenerEstudiantesPorCurso(self, id_curso):
		return self.llamarProcedimineto("obtenerEstudiantesPorCurso", (id_curso,))
		self.desconectar()
