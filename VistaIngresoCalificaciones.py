# -*- coding: utf-8 -*- 


import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *


class VistaIngresoCalificaciones(QWidget):
	dimension_x=700
	dimension_y=600

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.setWindowTitle("Ingreso Calificaciones")
			self.contenedor = QHBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.form_layout = QFormLayout() #layout interno
			self.setLayout(self.contenedor)
			self.form_layout.addRow("Estudiantes",QLabel(""))
			self.Estudiantes=MyTable()
			self.Estudiantes.setHeader(["Apellido","Nombre"])
			self.Tab=QTabWidget()
			tab1= QWidget()	
			tab2= QWidget()
			self.Tab.addTab (tab1,"1 Quimestre")
			self.Tab.addTab (tab2,"2 Quimestre")
			#tab1.addWidget(QPushButton("Ingresar"))
			#tab1.addWidget(QPushButton("Ingresar"))
			#tab1.addWidget(QPushButton("Ingresar"))
			#tab1.addWidget(QPushButton("Ingresar"))

			self.form_layout.addRow(self.Estudiantes)
			self.form_layout.addRow(self.Tab)

			self.hbox = QHBoxLayout() #layout que coloca los widgets en forma horizontal
			#self.hbox.addWidget(QLabel("           ")) #agego un espacio en el lado izquierdo 
			#self.hbox.addWidget(QLabel("           "))
			hvbox= QVBoxLayout() #layout con disposicion vertical
			#hvbox.addWidget(QLabel("                      ")) #agrego un espacio
			self.contenedor.addLayout(hvbox) #agrego ese espacio al layout principal
			self.contenedor.addLayout(self.form_layout)
			self.contenedor.addLayout(hvbox)
			self.form_layout.addRow(self.hbox)
			self.setLayout(self.contenedor)
			

