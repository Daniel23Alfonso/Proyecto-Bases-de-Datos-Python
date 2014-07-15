import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *


class VistaMatriculacion(QWidget):

	def __init__(self,*args):
		QWidget.__init__(self,*args)
		self.contenedor = QVBoxLayout()
		self.layout_uno=QHBoxLayout()

		self.tipoBusqueda=["Cedula","Apellido","Nombre"]
		self.comboBusqueda=QComboBox()
		self.comboBusqueda.addItems(self.tipoBusqueda)
		
		self.busqueda=QLineEdit()

		self.botonBusqueda=QPushButton()
		self.botonBusqueda.setIcon(QIcon("Imagenes/buscar.jpg"))
		self.botonAgregar=QPushButton()
		self.botonAgregar.setIcon(QIcon("Imagenes/agregar.jpg"))
		
		self.estudiantes=MyTable()
		self.cursos=MyTable()

		self.initBusqueda()
		self.contenedor.addWidget(QLabel("Estudiantes Existentes:"))
		self.contenedor.addWidget(self.estudiantes)
		self.contenedor.addWidget(QLabel("Cursos Disponibles:"))
		self.layout_uno.addWidget(self.cursos)
		self.botonAsignar=QPushButton("Asignar")
		self.layout_uno.addWidget(self.botonAsignar)
		self.contenedor.addLayout(self.layout_uno)

		self.connect(self.botonAgregar,SIGNAL("clicked()"),self.agregarEstudiante)

		self.setLayout(self.contenedor)

	def initBusqueda(self):
		primeraFila=QHBoxLayout()
		primeraFila.addWidget(QLabel("			"))
		primeraFila.addWidget(QLabel("Tipo de Busqueda"))
		primeraFila.addWidget(self.comboBusqueda)
		primeraFila.addWidget(self.busqueda)
		primeraFila.addWidget(self.botonBusqueda)
		primeraFila.addWidget(self.botonAgregar)
		primeraFila.addWidget(QLabel("			"))
		self.contenedor.addLayout(primeraFila)

	def agregarEstudiante(self):
		self.vistaAgregarEst=VistaAgregarEstudiante()
		self.vistaAgregarEst.show()


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
		#self.initEstudiante()
		self.setLayout(self.contenedor)

	def initEstudiante(self):
		self.layout_estudiante=QFormLayout()
		self.listaLayouts=[]
		for i in range(7):
			self.listaLayouts.append(QHBoxLayout())

		listDatosEst = ["Nombres:","Apellidos:","Cedula:", "Sexo:","Estado Civil:","Origen:","Etnia:" ,"Fecha de nacimiento:"]
		indiceSexo=3
		indiceEstadoCivil=4

		for i in range(7):
			self.listaLayouts[i].addWidget(QLabel(listDatosEst[i]))
			if (i!=indiceSexo)and(i!=indiceEstadoCivil):
				self.listaLayouts[i].addWidget(QLineEdit())
			self.layout_estudiante.addRow(self.listaLayouts[i])

		self.comboSexo=QComboBox()
		self.sexos=["Masculino","Femenino"]
		self.comboSexo.addItems(self.sexos)
		self.listaLayouts[indiceSexo].addWidget(self.comboSexo)
		self.listaLayouts[indiceSexo].addWidget(QLabel("				"))
		self.listaLayouts[indiceSexo].addWidget(QLabel("				"))
		self.listaLayouts[i].addWidget(QLabel(listDatosEst[i]))


		self.comboEstadoCivil=QComboBox()
		self.EstadoCivil=["Soltero"]
		self.comboEstadoCivil.addItems(self.EstadoCivil)
		self.listaLayouts[indiceEstadoCivil].addWidget(self.comboEstadoCivil)
		self.listaLayouts[indiceEstadoCivil].addWidget(QLabel("				"))
		self.listaLayouts[indiceEstadoCivil].addWidget(QLabel("				"))




		self.estudiante.setLayout(self.layout_estudiante)






