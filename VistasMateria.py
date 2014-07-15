# -*- coding: utf-8 -*- 

import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *

class VistasMateria(QWidget):
	dimension_x=400
	dimension_y=500

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.setLayout(self.contenedor)
			
			#Tabla alumnos
			self.materiasGrid=MyTable()
			
			
			
			self.layoutMaterias1=QHBoxLayout()
			self.layoutMateria1Sub = QVBoxLayout()
			self.layoutMaterias2=QVBoxLayout()
			self.layoutMateria21=QFormLayout()
			self.layoutMateria22=QHBoxLayout()
			self.layoutMaterias1.addLayout(self.layoutMateria1Sub)
			self.layoutMateria1Sub.addWidget(QLabel("Materias"))
			self.layoutMateria1Sub.addWidget(self.materiasGrid)
			
			
			#--definicion de contenedores de cada pestaña--#

			self.layoutMaterias2.addLayout(self.layoutMateria21)
			self.layoutMaterias2.addLayout(self.layoutMateria22)


			
			self.nombreMateria = QLineEdit()
			self.btnCrea=QPushButton("Crear")
			self.btnActualizar=QPushButton("Actualizar")
			self.btnEliminar=QPushButton("Eliminar")


			self.contenedor.addLayout(self.layoutMaterias1)
			self.contenedor.addLayout(self.layoutMaterias2)
			self.layoutMateria21.addRow("Nombre: ",self.nombreMateria)
			self.layoutMateria22.addWidget(self.btnCrea)
			self.layoutMateria22.addWidget(self.btnActualizar)
			self.layoutMateria22.addWidget(self.btnEliminar)

			
		


#app = QApplication(sys.argv)
#vista1 = VistaFacturacion()
#vista1.show()
#app.exec_()