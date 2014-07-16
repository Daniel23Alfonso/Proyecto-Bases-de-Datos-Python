import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *

class VistaAgregarEstudiante(QWidget):
	dimension_x=600
	dimension_y=500

	def __init__(self,*args):
		QWidget.__init__(self,*args)
		self.setWindowTitle("Agregar Estudiante")
		self.setGeometry(100,50,self.dimension_x,self.dimension_y)
		self.contenedor=QHBoxLayout()
		self.tab_uno=QTabWidget()
		self.estudiante=QWidget()
		self.padre=QWidget()
		self.madre=QWidget()
		self.representante=QWidget()
		self.tab_uno.addTab(self.estudiante,"Estudiante")
		self.tab_uno.addTab(self.padre,"Padre")
		self.tab_uno.addTab(self.madre,"Madre")
		self.tab_uno.addTab(self.representante,"Representante")
		self.contenedor.addWidget(self.tab_uno)
		self.initEstudiante()
		self.setLayout(self.contenedor)

	def initEstudiante(self):
		self.layout_estudiante=QVBoxLayout()
		self.listaLayouts=[QFormLayout(),QFormLayout()]
		
		#for i in range(8):
		#	self.listaLayouts.append(QFormLayout())

		listDatosEst = ["Nombres:","Apellidos:",u"Cédula:", "Sexo:","Estado Civil:","Origen:","Etnia:" ,"Fecha de nacimiento:"]
		indiceSexo=3
		indiceEstadoCivil=4
		for i in range(0,3):
			self.listaLayouts[0].addRow(QLabel(listDatosEst[i]),QLineEdit())

		self.comboSexo=QComboBox()
		self.sexos=["MASCULINO","FEMENINO"]
		self.comboSexo.addItems(self.sexos)

		self.comboEstadoCivil=QComboBox()
		self.EstadoCivil=["SOLTERO(A)","CASADO(A)","DIVORCIADO(A)","VIUDO(A)","UNIDO(A)"]
		self.comboEstadoCivil.addItems(self.EstadoCivil)

		self.listaLayouts[0].addRow(QLabel(listDatosEst[indiceSexo]),self.comboSexo)
		self.listaLayouts[0].addRow(QLabel(listDatosEst[indiceEstadoCivil]),self.comboEstadoCivil)
		self.listaLayouts[0].addRow(QLabel(listDatosEst[5]),QLineEdit())

		self.comboEtnia=QComboBox()
		self.Etnia=["BLANCO","MESTIZO","AFROECUATORIANO","INDIGENA", "MONTUBIO","NEGRO","MULATO","OTROS"]
		self.comboEtnia.addItems(self.Etnia)

		self.listaLayouts[0].addRow(QLabel(listDatosEst[6]),self.comboEtnia)

		self.calendario=QCalendarWidget()
		self.calendario.setMinimumDate(QDate(1940,1,1))
		self.calendario.setMaximumDate(QDate(2015,1,1))
		self.calendario.setGridVisible(False)

		self.listaLayouts[0].addRow(QLabel(listDatosEst[7]),self.calendario)



		self.layout_estudiante.addLayout(self.listaLayouts[0])


		self.estudiante.setLayout(self.layout_estudiante)
