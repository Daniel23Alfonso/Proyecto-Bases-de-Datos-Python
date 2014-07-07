import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *


class VistaConsultaNotas(QWidget):
	dimension_x=700
	dimension_y=600

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.setWindowTitle("Consulta de Notas")
			self.contenedor = QHBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.form_layout = QFormLayout() #layout interno
			self.setLayout(self.contenedor)
			self.form_layout.addRow("Curso:      ",QLabel("Paralelo:"     ))
			self.Estudiantes=MyTable()
			self.Tab=QTabWidget()
			self.form_layout.addRow(self.Estudiantes)

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