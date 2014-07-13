import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *

class VistaPersona(QWidget):
	dimension_x=400
	dimension_y=500

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.setLayout(self.contenedor)
			self.Personas=MyTable()
			self.contenedor.addWidget(QLabel("Personas"))
			self.contenedor.addWidget(self.Personas)
			self.layoutPersona=QFormLayout()
			#definicion cajas de texto
			self.cedula=QLineEdit()
			self.nombre=QLineEdit()
			self.apellido=QLineEdit()
			self.sexo=QComboBox()
			self.sexo.addItems(["Masculino","Femenino"])
			self.estadoCivil=QComboBox()
			self.estadoCivil.addItems(["Soltero","Casado","Divorsiado","Union Libre","Viudo"])
			self.ocupacion=QLineEdit()
			self.lugarTrabajo=QLineEdit()
			self.telefono=QLineEdit()
			self.direccion=QLineEdit()

			#creacion de formulario
			self.layoutPersona.addRow("cedula: ",self.cedula)
			self.layoutPersona.addRow("Nombre: ",self.nombre)
			self.layoutPersona.addRow("Apellido: ",self.apellido)
			self.layoutPersona.addRow("sexo: ",self.sexo)
			self.layoutPersona.addRow("Estado Civil: ",self.estadoCivil)
			self.layoutPersona.addRow("Ocupacion: ",self.ocupacion)
			self.layoutPersona.addRow("Lugar Trabajo: ",self.lugarTrabajo)
			self.layoutPersona.addRow("Telefono: ",self.telefono)
			self.layoutPersona.addRow("Direccion: ",self.direccion)
			self.contenedor.addLayout(self.layoutPersona)

		