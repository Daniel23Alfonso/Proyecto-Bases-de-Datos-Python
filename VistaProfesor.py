# -*- coding: utf-8 -*- 


import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *
from VistaIngresoCalificaciones import *
from VistaConsultaNotas import *

class VistaProfesor(QWidget):
	dimension_x=1000
	dimension_y=600


	def __init__(self,usuarioNombre,*args):
		QWidget.__init__(self,*args)
		self.setGeometry(100,50,self.dimension_x,self.dimension_y)
		self.contenedor = QHBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
		self.form_layout = QFormLayout() #layout interno
		self.usuarioNombre=QLabel(usuarioNombre)
		self.setWindowTitle("Opciones Profesor")
		
		self.opciones=QTabWidget()

		self.consultas= QWidget()
		self.reportes= QWidget()
		self.calificaciones= QWidget()

		self.layoutConsultas= QFormLayout()
		self.layoutReportes= QFormLayout()
		self.layoutCalificaciones= QFormLayout()

		self.consultas.setLayout(self.layoutConsultas)
		self.reportes.setLayout(self.layoutReportes)
		self.calificaciones.setLayout(self.layoutCalificaciones)

		self.botonConsultas=QPushButton("Ir Consultas")
		self.connect(self.botonConsultas,SIGNAL("clicked()"),self.initConsultas)
		
		self.botonReportes=QPushButton("Ir a Reportes")
		self.connect(self.botonReportes,SIGNAL("clicked()"),self.initReportes)

		self.botonCalificaciones=QPushButton("Ir a calificaciones")
		self.connect(self.botonCalificaciones,SIGNAL("clicked()"),self.initCalificaciones)

		self.opciones.addTab(self.consultas,"Consultas")
		self.opciones.addTab(self.reportes,"Generar Reportes")
		self.opciones.addTab(self.calificaciones,"Insertar Calificaciones")

		self.tablaConsultas=MyTable()
		self.tablaConsultas.addRow("Consultas")

		self.tablaReporte=MyTable()
		self.tablaReporte.addRow("Reportes")

		self.tablaCalificaciones=MyTable()
		self.tablaCalificaciones.addRow("Calificaciones")

		self.layoutConsultas.addRow(self.tablaConsultas)
		self.layoutConsultas.addRow(self.botonConsultas)

		self.layoutReportes.addRow(self.tablaReporte)
		self.layoutReportes.addRow(self.botonReportes)
		
		self.layoutCalificaciones.addRow(self.tablaCalificaciones)
		self.layoutCalificaciones.addRow(self.botonCalificaciones)


		#for i in range(4):
		#	self.form_layout.addRow(QLabel("")) #estoy agregando filas vacias 				

		#self.form_layout.addRow(QLabel("      "))
		self.form_layout.addRow('Usuario:', self.usuarioNombre)
		
		self.form_layout.addRow(QLabel("      "))
		self.form_layout.addRow(self.opciones)

		#self.form_layout.addRow('Opciones', self.Opciones) #agrego el combo box

		hvbox= QVBoxLayout() #layout con disposicion vertical
		hvbox.addWidget(QLabel("               ")) #agrego un espacio

		self.contenedor.addLayout(hvbox)
		self.contenedor.addLayout(self.form_layout)
		self.contenedor.addLayout(hvbox)	
		self.setLayout(self.contenedor)

	def initCalificaciones(self):
		self.vistaCalificaciones=VistaIngresoCalificaciones()
		self.close()
		self.vistaCalificaciones.show()


	def initConsultas(self):
		self.vistaConsultas=VistaConsultaNotas()
		self.close()
		self.vistaConsultas.show()


	def initReportes(self):
		pass
