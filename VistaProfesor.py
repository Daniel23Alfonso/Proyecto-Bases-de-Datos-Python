# -*- coding: utf-8 -*- 


import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *

class VistaSemestre(QWidget):

	def __init__(self,numQuimestre,*args):
		QWidget.__init__(self,*args)
		self.layout_uno=QVBoxLayout()
		self.tab_uno=QTabWidget()#parciales
		self.parciales_uno=[QWidget(),QWidget(),QWidget(),QWidget()]#pestañas con los parciales y el examen
		self.layouts=[QVBoxLayout(),QVBoxLayout(),QVBoxLayout(),QVBoxLayout()]#layouts para cada pestaña
		self.botones=[QPushButton("Agregar Actividad"),QPushButton("Agregar Actividad"),QPushButton("Agregar Actividad")]
		self.layoutHorizontal=[QHBoxLayout(),QHBoxLayout(),QHBoxLayout()]#layouts para los espacios
		
		self.tipoActividades=["Actividad 1","Actividad 2","Actividad 3"];
		self.comboActividades=[QComboBox(),QComboBox(),QComboBox()]
		self.initComboBox(self.comboActividades,self.tipoActividades)

		self.initTab(self.tab_uno,self.layout_uno,self.parciales_uno,self.layouts)
		self.initBotones(self.layoutHorizontal,self.layouts,self.botones,self.comboActividades)
		
		self.setLayout(self.layout_uno)


	def initTab(self,tabWidget,layoutWidget,coleccionWidget,coleccionLayout):
		tabWidget.addTab(coleccionWidget[0],"1er Parcial")
		tabWidget.addTab(coleccionWidget[1],"2do Parcial")
		tabWidget.addTab(coleccionWidget[2],"3er Parcial")
		tabWidget.addTab(coleccionWidget[3],"Examen")
		for i in range(4):
			coleccionLayout[i].addWidget(QLabel("Lista de Estudiantes:"))
			coleccionLayout[i].addWidget(MyTable())
			coleccionWidget[i].setLayout(coleccionLayout[i])
		layoutWidget.addWidget(tabWidget)#se añaden las pestañas de los parciales y el examen

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



class VistaExamenes(QWidget):
	def __init__(self,*args):
		QWidget.__init__(self,*args)
		self.layout_examen=QVBoxLayout()
		self.layout_examen.addWidget(QLabel("Lista de Estudiantes:"))
		self.Estudiantes=MyTable()
		self.layout_examen.addWidget(self.Estudiantes)
		self.setLayout(self.layout_examen)



class VistaIngresoCalificaciones(QWidget):
	dimension_x=600
	dimension_y=500

	def __init__(self,*args):
		QWidget.__init__(self,*args)
		self.setGeometry(100,50,self.dimension_x,self.dimension_y)
		self.setWindowTitle("Ingreso Calificaciones")
		self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
		self.Tab=QTabWidget()#pestañas con los quimestres y examenes
			
		self.tab_primer= VistaSemestre(1)

		self.tab_segundo= VistaSemestre(2)

		self.tab_examen=VistaExamenes()

		self.Tab.addTab (self.tab_primer,"1er Quimestre")
		self.Tab.addTab (self.tab_segundo,"2do Quimestre")
		self.Tab.addTab(self.tab_examen,"Examenes")

		self.contenedor.addWidget(QLabel("                               "))
		self.contenedor.addWidget(QLabel("Usuario:"))
		self.contenedor.addWidget(QLabel("                               "))
		self.contenedor.addWidget(self.Tab)
		self.setLayout(self.contenedor)


class VistaConsultaNotas(QWidget):
	dimension_x=800
	dimension_y=300

	def __init__(self,*args):
		QWidget.__init__(self,*args)
		self.setGeometry(100,50,self.dimension_x,self.dimension_y)
		self.setWindowTitle("Consulta Notas")
		self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal	
		self.Estudiantes=MyTable()	
		self.contenedor.addWidget(QLabel("Calificaciones de los Estudiantes:"))				
		self.contenedor.addWidget(self.Estudiantes)
		self.setLayout(self.contenedor)

class VistaReporte(QWidget):
	def __init__(self,*args):
		QWidget.__init__(self,*args)
		self.layout_reportes=QVBoxLayout()
		self.layout_reportes.addWidget(QLabel("Cursos Disponibles:"))
		self.Estudiantes=MyTable()
		self.layout_reportes.addWidget(self.Estudiantes)
		self.boton_uno=QHBoxLayout()
		#self.boton_uno.addWidget(QLabel("                               "))
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


class VistaProfesor(QMainWindow):
	dimension_x=700
	dimension_y=500 

	def __init__(self,usuarioNombre,*args):
		QWidget.__init__(self,*args)
		self.setGeometry(100,50,self.dimension_x,self.dimension_y)
		self.main_widget = QWidget(self)
		self.activarCalificaciones=False
		self.activarConsultas=False
		self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
		self.form_layout = QFormLayout() #layout interno
		self.setWindowTitle("Opciones Profesor")
		
		self.opciones=QTabWidget()
		
		self.tablas=[MyTable(),MyTable()]

		self.consultas=QWidget()
		self.calificaciones=QWidget()
		self.reportes=VistaReporte()

		self.layout_consultas=QVBoxLayout()
		self.layout_consultas.addWidget(QLabel("Cursos Disponibles:"))
		self.layout_consultas.addWidget(self.tablas[0])
		self.layout_cero=QHBoxLayout()
		self.layout_cero.addWidget(QLabel("                               "))
		self.layout_cero.addWidget(QLabel("                               "))
		self.botonConsultas=QPushButton("Consulta Calificaciones")
		self.connect(self.botonConsultas,SIGNAL("clicked()"),self.initConsultas)
		self.layout_cero.addWidget(self.botonConsultas)
		self.layout_cero.addWidget(QLabel("                               "))
		self.layout_cero.addWidget(QLabel("                               "))
		self.layout_consultas.addLayout(self.layout_cero)


		self.layout_calificaciones=QVBoxLayout()
		self.layout_calificaciones.addWidget(QLabel("Cursos Disponibles:"))
		self.layout_calificaciones.addWidget(self.tablas[1])
		self.layout_dos=QHBoxLayout()
		self.layout_dos.addWidget(QLabel("                               "))
		self.layout_dos.addWidget(QLabel("                               "))
		self.botonCalificaciones=QPushButton("Insertar Calificaciones")
		self.connect(self.botonCalificaciones,SIGNAL("clicked()"),self.initCalificaciones)
		self.layout_dos.addWidget(self.botonCalificaciones)
		self.layout_dos.addWidget(QLabel("                               "))
		self.layout_dos.addWidget(QLabel("                               "))
		self.layout_calificaciones.addLayout(self.layout_dos)

		self.consultas.setLayout(self.layout_consultas)
		self.calificaciones.setLayout(self.layout_calificaciones)

		self.opciones.addTab(self.consultas,"Consultas")
		self.opciones.addTab(self.reportes,"Generar Reportes")
		self.opciones.addTab(self.calificaciones,"Insertar Calificaciones")

		self.contenedor.addWidget(QLabel("		"))
		self.contenedor.addWidget(QLabel("Usuario: "+usuarioNombre))
		self.contenedor.addWidget(QLabel("		"))
		self.contenedor.addWidget(self.opciones)

		self.main_widget.setLayout(self.contenedor)
		self.setCentralWidget(self.main_widget)

	def initCalificaciones(self):
		if self.activarCalificaciones==False:
			self.vistaCalificaciones=VistaIngresoCalificaciones()
			self.vistaCalificaciones.show()
			#self.layout_calificaciones.addWidget(self.vistaCalificaciones)
			self.activarCalificaciones=True

	def initConsultas(self):
		if self.activarConsultas==False:
			self.vistaConsultas=VistaConsultaNotas()
			self.vistaConsultas.show()
			#self.layout_consultas.addWidget(self.vistaConsultas)
			self.activarConsultas=True

