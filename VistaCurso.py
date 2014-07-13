import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *

class VistaCurso(QWidget):
	dimension_x=400
	dimension_y=500

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.setLayout(self.contenedor)
			self.Cursos=MyTable()
			self.contenedor.addWidget(QLabel("Cursos"))
			self.contenedor.addWidget(self.Cursos)
			self.layoutCurso=QFormLayout()
			self.contenedor.addLayout(self.layoutCurso)
			#definicion cajas de texto
			self.aLectivo=QLineEdit()
			self.curso=QComboBox()
			self.curso.addItems(["Kinder","Primero","Segundo","Tercero","Cuarto","Quinto","Sexto","Septimo"])
			#creacion de formulario
			self.layoutCurso.addRow("Ano Lectivo: ",self.aLectivo)
			self.layoutCurso.addRow("curso: ",self.curso)


