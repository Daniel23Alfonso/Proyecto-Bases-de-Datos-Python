import MySQLdb

class ManejadorBD():
	def __init__(self):
		self.direccion="localhost"
		self.user="root"
		self.passwor="sasukekun30"
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
		self.BD.commit()
		self.desconectar()

	def consultarEstudiantesPorMateria(self,idCurso,materia,quimestre,parcial):
		return self.llamarProcedimineto("consultarEstudiantesPorMateria",(idCurso,materia,quimestre,parcial))

	def actualizarEstudianteActividad(self,idCurso,materia,quimestre,parcial,tipoActividad,matriculaEstudiante,nota):
		arg=(str(idCurso),str(materia),str(quimestre),str(parcial),str(tipoActividad),str(matriculaEstudiante),str(nota))
		self.llamarProcedimineto("actualizarEstudianteActividad",arg)
		self.BD.commit()
		self.desconectar()

	def crearEstudiante(self,estudiante,padre,madre,representante,personaFactura):
		pass

	def crearCurso(self,datos):
		self.llamarProcedimineto("crearCurso",datos)
		self.BD.commit()
		self.desconectar()

	def AsignarDirigente(self,datos):
		self.llamarProcedimineto("AsignarDirigente",datos)
		self.BD.commit()
		self.desconectar()


