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
		self.initTab(self.tab_uno,self.layout_uno,self.parciales_uno,self.layouts)
		self.initBotones(self.layouts,self.botones)
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

	def initBotones(self,coleccionLayout,coleccionBotones):
		for i in range (3):
			coleccionLayout[i].addWidget(coleccionBotones[i])


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
		self.contenedor = QHBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
		self.form_layout = QFormLayout() #layout interno
		self.setLayout(self.contenedor)

		self.Tab=QTabWidget()#pestañas con los quimestres y examenes
			
		self.tab_primer= VistaSemestre(1)

		self.tab_segundo= VistaSemestre(2)

		self.tab_examen=VistaExamenes()

		self.Tab.addTab (self.tab_primer,"1er Quimestre")
		self.Tab.addTab (self.tab_segundo,"2do Quimestre")
		self.Tab.addTab(self.tab_examen,"Examenes")

		self.form_layout.addRow(QLabel("                               "))
		self.form_layout.addRow(QLabel("Usuario:"))
		self.form_layout.addRow(QLabel("                               "))
		self.form_layout.addRow(self.Tab)
		self.contenedor.addLayout(self.form_layout)
		self.setLayout(self.contenedor)


class VistaConsultaNotas(QWidget):
	dimension_x=800
	dimension_y=300

	def __init__(self,*args):
		QWidget.__init__(self,*args)
		self.setGeometry(100,50,self.dimension_x,self.dimension_y)
		self.contenedor = QHBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
		self.form_layout = QFormLayout() #layout interno
		self.setLayout(self.contenedor)			
		self.Estudiantes=MyTable()	
		self.form_layout.addWidget(QLabel("Calificaciones de los Estudiantes:"))		
		
		self.form_layout.addRow(self.Estudiantes)

		self.contenedor.addLayout(self.form_layout)
		self.setLayout(self.contenedor)


class VistaProfesor(QWidget):
	dimension_x=800
	dimension_y=500 

	def __init__(self,usuarioNombre,*args):
		QWidget.__init__(self,*args)
		self.setGeometry(100,50,self.dimension_x,self.dimension_y)
		self.activarCalificaciones=False
		self.activarConsultas=False
		self.contenedor = QHBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
		self.form_layout = QFormLayout() #layout interno
		self.usuarioNombre=QLabel(usuarioNombre)
		self.setWindowTitle("Opciones Profesor")
		
		self.opciones=QTabWidget()
		
		self.tablas=[MyTable(),MyTable(),MyTable()]

		self.consultas=QWidget()
		self.calificaciones=QWidget()
		self.reportes=QWidget()

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

		self.layout_reportes=QVBoxLayout()
		self.layout_reportes.addWidget(QLabel("Cursos Disponibles:"))
		self.layout_reportes.addWidget(self.tablas[1])
		
		self.boton_uno=QHBoxLayout()
		self.boton_uno.addWidget(QLabel("                               "))
		self.boton_uno.addWidget(QLabel("                               "))
		self.botonReportes=QPushButton("Generar Reportes")
		self.connect(self.botonReportes,SIGNAL("clicked()"),self.initReportes)
		self.boton_uno.addWidget(self.botonReportes)
		self.boton_uno.addWidget(QLabel("                               "))
		self.boton_uno.addWidget(QLabel("                               "))	
		self.layout_reportes.addLayout(self.boton_uno)

		self.layout_calificaciones=QVBoxLayout()
		self.layout_calificaciones.addWidget(QLabel("Cursos Disponibles:"))
		self.layout_calificaciones.addWidget(self.tablas[2])
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
		self.reportes.setLayout(self.layout_reportes)

		self.opciones.addTab(self.consultas,"Consultas")
		self.opciones.addTab(self.reportes,"Generar Reportes")
		self.opciones.addTab(self.calificaciones,"Insertar Calificaciones")

		self.form_layout.addRow(QLabel("      "))
		self.form_layout.addRow(QLabel("      "))
		self.form_layout.addRow(QLabel("      "))
		self.form_layout.addRow('Usuario:', self.usuarioNombre)
		self.form_layout.addRow(QLabel("      "))
		self.form_layout.addRow(QLabel("      "))
		self.form_layout.addRow(self.opciones)

		hvbox= QVBoxLayout() #layout con disposicion vertical
		hvbox.addWidget(QLabel("               ")) #agrego un espacio

		self.contenedor.addLayout(hvbox)
		self.contenedor.addLayout(self.form_layout)
		self.contenedor.addLayout(hvbox)	
		self.setLayout(self.contenedor)

	def initCalificaciones(self):
		if self.activarCalificaciones==False:
			self.vistaCalificaciones=VistaIngresoCalificaciones()
			self.close()
			self.vistaCalificaciones.show()
			#self.layout_calificaciones.addWidget(self.vistaCalificaciones)
			self.activarCalificaciones=True

	def initConsultas(self):
		if self.activarConsultas==False:
			self.vistaConsultas=VistaConsultaNotas()
			self.layout_consultas.addWidget(self.vistaConsultas)
			self.activarConsultas=True


	def initReportes(self):
		pass
