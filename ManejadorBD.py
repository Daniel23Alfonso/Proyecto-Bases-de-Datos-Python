import MySQLdb

class ManejadorBD():
	def __init__(self):
		self.direccion="127.0.0.1"
		self.user="root"
		self.passwor="sasukekun30"
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
		print tupla
		cursor.callproc(nombreProcedimiento,tupla)
		resultado = cursor.fetchall()
		return resultado
		self.desconectar()


	def consultarEstudiante(self):
		return self.llamarProcedimineto("consultarEstudiante")
		

	def consultarMaterias(self):
		query = "SELECT * FROM Materia"
		return self.consulta(query, None)

	def consultarPersonas(self):
		return self.llamarProcedimineto("consultarPersonas")

	def consultarProfesores(self):
		return self.llamarProcedimineto("consultarProfesor")

	def obtenerCursosPorProfesor(self,usuarioNombre):
		arg= (usuarioNombre,)
		return self.llamarProcedimineto('consultarCursosDelProfesor',arg)


	def obtenerCursos(self):
		return self.llamarProcedimineto("consultarCursos")

	def consultarEstudiante2(self):
		return self.llamarProcedimineto("consultarEstudiante2")

	def agregarEstudianteEnCurso(self,curso,matricula):
		arg=(curso,matricula)
		self.llamarProcedimineto("agregarEstudianteEnCurso",arg)
		print "se agrego el estudiante al curso"	


