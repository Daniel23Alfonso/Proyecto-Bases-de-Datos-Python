import MySQLdb

class ManejadorBD():
	def __init__(self):
		self.direccion="127.0.0.1"
		self.user="root"
		self.passwor=""
		self.nombreBD="BaseEscuela"


	def conectar(self):
		self.BD = MySQLdb.connect(self.direccion,self.user,self.passwor,self.nombreBD )


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
		

	def consultarMaterias(self):
		query = "SELECT * FROM Materia"
		return self.consulta(query, None)

	def consultarPersonas(self):
		return self.llamarProcedimineto("consultarPersonas")
		self.desconectar()

	def consultarProfesores(self):
		return self.llamarProcedimineto("consultarProfesor")
		self.desconectar()

	def obtenerCursosPorProfesor(self,usuarioNombre):
		arg= (usuarioNombre,)
		return self.llamarProcedimineto('consultarCursosDelProfesor',arg)
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

