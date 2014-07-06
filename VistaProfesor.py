# -*- coding: utf-8 -*- 


import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class VistaProfesor(QWidget):
	dimension_x=500
	dimension_y=600


	def __init__(self,usuarioNombre,*args):
		QWidget.__init__(self,*args)
		self.setGeometry(100,50,self.dimension_x,self.dimension_y)
		self.contenedor = QHBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
		self.form_layout = QFormLayout() #layout interno
		self.usuarioNombre=QLabel(usuarioNombre)
		self.setWindowTitle("Opciones Profesor")
		self.opciones=QTabBar()
		self.opciones.addTab("Consultas")
		self.opciones.addTab("Generar Reportes")
		self.opciones.addTab("Insertar Calificaciones")

		#self.opcionesProfesor=["Consultas","Generar Reportes","Insertar Calificaciones"] #lista para escoger el tipo de usuario
		#self.Opciones=QComboBox() #opciones disponibles para el profesor en un combo box
		#self.Opciones.addItems(self.opcionesProfesor)

		self.gridLayout=QGridLayout()

		for i in range(2):
			self.gridLayout.addWidget(QLabel("Consultas"),0,i)

		gridWidget=QWidget()
		gridWidget.setLayout(self.gridLayout)

		for i in range(4):
			self.form_layout.addRow(QLabel("")) #estoy agregando filas vacias 				

		self.form_layout.addRow(QLabel("      "))
		self.form_layout.addRow('Usuario:', self.usuarioNombre)
		
		self.form_layout.addRow(QLabel("      "))
		self.form_layout.addRow(self.opciones)

		#self.form_layout.addRow('Opciones', self.Opciones) #agrego el combo box
		self.form_layout.addRow(gridWidget)

		hvbox= QVBoxLayout() #layout con disposicion vertical
		hvbox.addWidget(QLabel("               ")) #agrego un espacio

		self.contenedor.addLayout(hvbox)
		self.contenedor.addLayout(self.form_layout)
		self.contenedor.addLayout(hvbox)	
		self.setLayout(self.contenedor)