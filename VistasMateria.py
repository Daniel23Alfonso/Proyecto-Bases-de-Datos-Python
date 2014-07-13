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
			self.layoutMaterias2=QHBoxLayout()
			self.layoutMaterias1.addLayout(self.layoutMateria1Sub)
			self.layoutMateria1Sub.addWidget(QLabel("Materias"))
			self.layoutMateria1Sub.addWidget(self.materiasGrid)
			
			

			tab_widget = QTabWidget()
			tab_crearM = QWidget()
			tab_modifM = QWidget()
			tab_elimiM = QWidget()
			
			#--definicion de contenedores de cada pestaña--#
			
			
			self.cont_crear = QVBoxLayout(tab_crearM) #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.cont_mod = QHBoxLayout(tab_modifM) 
			self.cont_elimi = QHBoxLayout(tab_elimiM)

			self.layoutMaterias2.addWidget(tab_widget)
			tab_widget.addTab(tab_crearM,"Crear Materia")
			tab_widget.addTab(tab_modifM,"Modificar Materia")
			tab_widget.addTab(tab_elimiM,"Eliminar Materia")


			
			self.nombreMateria = QLineEdit()



			self.contenedor.addLayout(self.layoutMaterias1)
			self.contenedor.addLayout(self.layoutMaterias2)


			
		


#app = QApplication(sys.argv)
#vista1 = VistaFacturacion()
#vista1.show()
#app.exec_()