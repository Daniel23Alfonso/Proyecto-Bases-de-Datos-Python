# -*- coding: utf-8 -*- 
import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *
from ManejadorBD import *

class VistaProfesor(QMainWindow):
	dimension_x=700
	dimension_y=500 

	def __init__(self,usuarioNombre,*args):
		QWidget.__init__(self,*args)
		self.setGeometry(100,50,self.dimension_x,self.dimension_y)
		self.setWindowTitle("Opciones Profesor")
		self.showMaximized()
		self.main_widget = QWidget(self)
		self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
		self.form_layout = QFormLayout() #layout interno
		
		self.usuarioNombre=usuarioNombre
		self.opciones=QTabWidget()#opciones disponibles del profesor: Consultar Notas,Generar Reportes e Ingresar Calificaciones
		
		self.tablas=[MyTable(self),MyTable(self),MyTable(self)]
		self.manejador=ManejadorBD()
		self.resultados=self.manejador.obtenerCursosPorProfesor(self.usuarioNombre)#obtiene los cursos del profesor que ingreso al sistema

		self.consultas=VistaConsulta(self.tablas[0])
		self.calificaciones=VistaCalificaciones(self.tablas[1])
		self.reportes=VistaReporte(self.tablas[2])

		#muestra los cursos asignados al profesor 
		for tabla_actual in self.tablas:
			tabla_actual.setHeader(["Materia Asignada","Codigo","Curso","Paralelo",u"Año Lectivo"])#establece las cabezeras de las tablas
			tabla_actual.addTable(self.resultados)#agrega los resultados obtenidos a la tabla

		self.opciones.addTab(self.consultas,"Consultas")
		self.opciones.addTab(self.reportes,"Generar Reportes")
		self.opciones.addTab(self.calificaciones,"Insertar Calificaciones")

		self.contenedor.addWidget(QLabel("		"))
		self.contenedor.addWidget(QLabel("Usuario: "+usuarioNombre))
		self.contenedor.addWidget(QLabel("		"))
		self.contenedor.addWidget(self.opciones)

		self.main_widget.setLayout(self.contenedor)
		self.setCentralWidget(self.main_widget)


class VistaConsulta(QWidget):

	def __init__(self,tablaDatos,*args):
		QWidget.__init__(self,*args)
		self.layout_consultas=QVBoxLayout()
		self.layout_consultas.addWidget(QLabel("Cursos Disponibles:"))
		self.cursos=tablaDatos
		#self.connect(self.cursos,SIGNAL("clicked()"),self.selectedItem
		self.layout_consultas.addWidget(self.cursos)#agrega los cursos del profesor para mostrarlos
		self.layout_cero=QHBoxLayout()
		self.layout_cero.addWidget(QLabel("                               "))
		self.layout_cero.addWidget(QLabel("                               "))
		self.botonConsultas=QPushButton("Consulta Calificaciones")
		self.connect(self.botonConsultas,SIGNAL("clicked()"),self.initConsultas)
		self.layout_cero.addWidget(self.botonConsultas)
		self.layout_cero.addWidget(QLabel("                               "))
		self.layout_cero.addWidget(QLabel("                               "))
		self.layout_consultas.addLayout(self.layout_cero)
		self.setLayout(self.layout_consultas)

	def initConsultas(self):
		resultados=self.cursos.getSelectedRegister()
		cursoSeleccionado=resultados[0]
		self.vistaNotasPorCurso=VistaNotasPorCurso(cursoSeleccionado)#muestra las notas de los estudiantes del curso seleccionado por el usuario
		self.vistaNotasPorCurso.show()


class VistaNotasPorCurso(QWidget):

	def __init__(self,curso,*args):
		QWidget.__init__(self,*args)
		self.setWindowTitle("Consulta Notas")
		self.showMaximized()
		self.cursoSeleccionado=curso
		materia=self.cursoSeleccionado[0]
		idCurso=self.cursoSeleccionado[1]
		
		primerQuimestre=0
		segundoQuimestre=1
		examenes=2

		self.contenedor=QVBoxLayout()
	
		#definicion de las tablas en donde se insertaran los datos	
		self.Estudiantes=[MyTable(self),MyTable(self),MyTable(self)]#grid 0 para primer quimestre, 1 para segundo y 2 para los examenes
		self.manejador=ManejadorBD()
		self.Estudiantes[primerQuimestre].setHeader(["","Apellidos","Nombres","Primer Parcial ", "Segundo Parcial ","Tercer Parcial","Quimestre"])
		self.Estudiantes[primerQuimestre].hideColumn(0)
		self.Estudiantes[primerQuimestre].setEditable(False)
		self.Estudiantes[segundoQuimestre].setHeader(["","Apellidos","Nombres","Primer Parcial ", "Segundo Parcial ","Tercer Parcial","Quimestre"])
		self.Estudiantes[segundoQuimestre].hideColumn(0)
		self.Estudiantes[segundoQuimestre].setEditable(False)

		self.tab_uno=QTabWidget()
		self.pestanias=[QWidget(),QWidget(),QWidget()]#pestañas
		
		
		#layouts
		self.layout_uno=QVBoxLayout()
		self.layout_uno.addWidget(self.Estudiantes[primerQuimestre])
		self.pestanias[primerQuimestre].setLayout(self.layout_uno)
		self.layout_dos=QVBoxLayout()
		self.layout_dos.addWidget(self.Estudiantes[segundoQuimestre])
		self.pestanias[segundoQuimestre].setLayout(self.layout_dos)


		self.tab_uno.addTab(self.pestanias[primerQuimestre],"Notas Primer Quimestre")
		self.tab_uno.addTab(self.pestanias[segundoQuimestre],"Notas Segundo Quimestre")
		self.tab_uno.addTab(self.pestanias[examenes],"Notas Examenes")

		self.contenedor.addWidget(QLabel("Materia: " +self.cursoSeleccionado[0]))	
		self.contenedor.addWidget(self.tab_uno)		
		self.setLayout(self.contenedor)


class VistaCalificaciones(QWidget):

	def __init__(self,tablaDatos,*args):
		QWidget.__init__(self,*args)
		self.layout_calificaciones=QVBoxLayout()
		self.showMaximized()
		self.layout_calificaciones.addWidget(QLabel("Cursos Disponibles:"))
		self.cursos=tablaDatos
		self.manejador=ManejadorBD()
		self.layout_calificaciones.addWidget(self.cursos)
		self.layout_dos=QHBoxLayout()
		self.layout_dos.addWidget(QLabel("                               "))
		self.layout_dos.addWidget(QLabel("                               "))
		self.botonCalificaciones=QPushButton("Insertar Calificaciones")
		self.connect(self.botonCalificaciones,SIGNAL("clicked()"),self.initCalificaciones)
		self.layout_dos.addWidget(self.botonCalificaciones)
		self.layout_dos.addWidget(QLabel("                               "))
		self.layout_dos.addWidget(QLabel("                               "))
		self.layout_calificaciones.addLayout(self.layout_dos)
		self.setLayout(self.layout_calificaciones)

	def initCalificaciones(self):
		resultados=self.cursos.getSelectedRegister()
		cursoSeleccionado=resultados[0]
		self.vistaIngresoDeCalificaciones=VistaIngresoCalificaciones(cursoSeleccionado)#dado un curso muestra la interfaz para ingresar las notas de los estudiantes
		self.vistaIngresoDeCalificaciones.show()

class VistaIngresoCalificaciones(QWidget):
	dimension_x=600
	dimension_y=500

	def __init__(self,curso,*args):
		QWidget.__init__(self,*args)
		self.setGeometry(100,50,self.dimension_x,self.dimension_y)
		self.showMaximized()
		self.setWindowTitle("Ingreso Calificaciones")
		self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
		self.Tab=QTabWidget()#pestañas con los quimestres y examenes

		self.tab_primer= VistaSemestre(1,curso[1],curso[0])

		self.tab_segundo= VistaSemestre(2,curso[1],curso[0])

		self.tab_examen=VistaExamenes(curso[1])

		self.Tab.addTab (self.tab_primer,"1er Quimestre")
		self.Tab.addTab (self.tab_segundo,"2do Quimestre")
		self.Tab.addTab(self.tab_examen,"Examenes")

		self.contenedor.addWidget(QLabel("                               "))
		self.contenedor.addWidget(QLabel("Materia: "+curso[0]))
		self.contenedor.addWidget(QLabel("                               "))
		self.contenedor.addWidget(self.Tab)
		self.setLayout(self.contenedor)


class VistaSemestre(QWidget):

	def __init__(self,numQuimestre,curso,materia,*args):
		QWidget.__init__(self,*args)
		self.layout_uno=QVBoxLayout()
		self.tab_uno=QTabWidget()#parciales
		self.parciales_uno=[QWidget(),QWidget(),QWidget(),QWidget()]#pestañas con los parciales y el examen
		self.layouts=[QVBoxLayout(),QVBoxLayout(),QVBoxLayout(),QVBoxLayout()]#layouts para cada pestaña
		self.botones=[QPushButton("Agregar Actividad"),QPushButton("Agregar Actividad"),QPushButton("Agregar Actividad")]
		
		self.layoutHorizontal=[QHBoxLayout(),QHBoxLayout(),QHBoxLayout()]#layouts para los espacios
		
		self.botonesGuardar=[QPushButton("Guardar"),QPushButton("Guardar"),QPushButton("Guardar")]
		
		self.idCurso=curso
		self.materia=materia
		self.numQuimestre=numQuimestre
		self.manejador=ManejadorBD()

		self.tipoActividades=["Actividad 1","Actividad 2","Actividad 3"];
		self.comboActividades=[QComboBox(),QComboBox(),QComboBox()]

		#self.initComboBox(self.comboActividades,self.tipoActividades)
		self.initTab()
		#self.initBotones(self.layoutHorizontal,self.layouts,self.botones,self.comboActividades)
		self.setLayout(self.layout_uno)

		self.botonesGuardar[0].clicked.connect(lambda:self.guardarNotas(curso,materia,numQuimestre,1))
		self.botonesGuardar[1].clicked.connect(lambda:self.guardarNotas(curso,materia,numQuimestre,2))
		self.botonesGuardar[2].clicked.connect(lambda:self.guardarNotas(curso,materia,numQuimestre,3))


	def initTab(self):
		self.tab_uno.addTab(self.parciales_uno[0],"1er Parcial")
		self.tab_uno.addTab(self.parciales_uno[1],"2do Parcial")
		self.tab_uno.addTab(self.parciales_uno[2],"3er Parcial")
		#tabWidget.addTab(coleccionWidget[3],"Examen")
		self.estudiantes=[MyTable(self),MyTable(self),MyTable(self)]
		for i in range(3):
			self.layouts[i].addWidget(QLabel("Lista de Estudiantes:"))		
			consulta=self.manejador.consultarEstudiantesPorMateria(self.idCurso,self.materia,self.numQuimestre,i+1)
			resultados=self.ordenarDatos(consulta)
			self.estudiantes[i].addTable(resultados)
			self.estudiantes[i].setHeader(["","Apellidos","Nombres","En Clase", "En Grupo","Examen","Individual","Leccion"])
			self.estudiantes[i].hideColumn(0)
			self.layouts[i].addWidget(self.estudiantes[i])
			self.layouts[i].addWidget(self.botonesGuardar[i])
			self.parciales_uno[i].setLayout(self.layouts[i])
		self.layout_uno.addWidget(self.tab_uno)#se añaden las pestañas de los parciales 


	def initComboBox(self,coleccionCombo,contenido):
		for i in range(3):
			coleccionCombo[i].addItems(contenido)


	def initBotones(self,layoutHorizontal,coleccionLayout,coleccionBotones,coleccionCombo):
		for i in range (3):
			layoutHorizontal[i].addWidget(QLabel("			"))
			layoutHorizontal[i].addWidget(coleccionBotones[i])
			layoutHorizontal[i].addWidget(QLabel("			"))
			layoutHorizontal[i].addWidget(QLabel("Tipo de Actividad:"))
			layoutHorizontal[i].addWidget(coleccionCombo[i])
			layoutHorizontal[i].addWidget(QLabel("			"))
			coleccionLayout[i].addLayout(layoutHorizontal[i])


	def ordenarDatos(self,lista):
		resultados=[]
		i=0
		acumular=1
		print len(lista)
		while i<len(lista):
			registro_actual=lista[i]
			registro_nuevo=[]
			registro_nuevo.append(registro_actual[0])
			registro_nuevo.append(registro_actual[1])
			registro_nuevo.append(registro_actual[2])
			registro_nuevo.append(registro_actual[4])
			j=0
			for j in range(4):
				registro_siguiente=lista[acumular+j]
				registro_nuevo.append(registro_siguiente[4])
			resultados.append(registro_nuevo)
			acumular=acumular+5
			i=acumular
		return resultados

	def guardarNotas(self,curso,materia,numQuimestre,idParcial):
		resultados=[]
		print "Parcial"+str(idParcial)
		for i in range(self.estudiantes[idParcial-1].getSize()):
			registro=self.estudiantes[idParcial-1].getRegister(i)
			j=0
			for j in range(5):
				registro_nuevo=[]
				registro_nuevo.append(unicode(registro[0]))
				registro_nuevo.append(unicode(registro[1]))
				registro_nuevo.append(unicode(registro[2]))
				registro_nuevo.append(unicode(registro[j+3]))
				resultados.append(registro_nuevo)
		tipoActividad=["En Clase","En Grupo","Examen","Individual","Leccion"]
		i=0
		for registro in resultados:			
			self.manejador.actualizarEstudianteActividad(curso,materia,numQuimestre,idParcial,tipoActividad[i],registro[0],registro[3])
			if i==4: 
				i=0#empieza a barrer de nuevo el arreglo tipo de actividad
			else:
				i+=1


class VistaExamenes(QWidget):
	def __init__(self,curso,*args):
		QWidget.__init__(self,*args)
		self.layout_examen=QVBoxLayout()
		self.layout_examen.addWidget(QLabel("Lista de Estudiantes:"))
		self.Estudiantes=MyTable(self)
		self.manejador=ManejadorBD()
		self.idCurso=curso

		#self.Estudiantes.addTable(self.manejador.consultarEstudiantesPorMateria(self.idCurso,self.materia,numQuimestre))

		self.Estudiantes.setHeader(["","Apellidos","Nombres","Examen Primer Quimestre","Examen Segundo Quimestre"])
		self.Estudiantes.hideColumn(0)
		self.boton=QPushButton("Guardar")
		self.layout_examen.addWidget(self.Estudiantes)
		self.layout_examen.addWidget(self.boton)
		self.boton.clicked.connect(self.guardarNotas)
		self.setLayout(self.layout_examen)

	def guardarNotas(self):
		resultados=[]
		for i in range(self.Estudiantes.getSize()):
			registro=self.Estudiantes.getRegister(i)
			for atributo in registro:
				resultados.append(unicode(atributo))




class VistaReporte(QWidget):

	def __init__(self,tabla,*args):
		QWidget.__init__(self,*args)
		self.layout_reportes=QVBoxLayout()
		self.layout_reportes.addWidget(QLabel("Cursos Disponibles:"))
		self.Estudiantes=tabla
		self.layout_reportes.addWidget(self.Estudiantes)
		self.boton_uno=QHBoxLayout()
		self.boton_uno.addWidget(QLabel("                               "))
		self.tiposReportes=["Lista de Estudiantes","Acta de Calificaciones","Libretas","Sabanas","Promociones"]
		self.comboReportes=QComboBox()
		self.comboReportes.addItems(self.tiposReportes)
		self.boton_uno.addWidget(QLabel("Tipos de Reportes:"))
		self.boton_uno.addWidget(self.comboReportes)
		self.boton_uno.addWidget(QLabel("                               "))
		self.boton_uno.addWidget(QLabel("                               "))	
		self.botonReportes=QPushButton("Generar Reporte")
		self.connect(self.botonReportes,SIGNAL("clicked()"),self.initReportes)
		self.boton_uno.addWidget(self.botonReportes)
		self.boton_uno.addWidget(QLabel("                               "))
		self.boton_uno.addWidget(QLabel("                               "))
		self.layout_reportes.addLayout(self.boton_uno)
		self.setLayout(self.layout_reportes)

	def initReportes(self):
		pass
