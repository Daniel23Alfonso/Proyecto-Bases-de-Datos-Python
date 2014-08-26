# -*- coding: utf-8 -*- 
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
		self.A=[]
		self.B=[]
		self.headerEstudainte = [u"Matrícula",u"cédula", "Nombres", "Apellidos"]
		self.comboBusqueda=QComboBox()
		self.comboBusqueda.addItems(self.headerEstudainte)
		
		self.busqueda=QLineEdit()

		self.botonAgregar=QPushButton()
		self.botonAgregar.setIcon(QIcon("Imagenes/agregar.jpg"))
		
		self.alumnos=MyTable(self)
		self.cursos=MyTable(self)

		self.initBusqueda()
		self.contenedor.addWidget(QLabel("Estudiantes Existentes:"))
		self.contenedor.addWidget(self.alumnos)
		self.contenedor.addWidget(QLabel("Cursos Disponibles:"))
		self.layout_uno.addWidget(self.cursos)
		self.botonAsignar=QPushButton("Asignar")
		self.layout_uno.addWidget(self.botonAsignar)
		self.contenedor.addLayout(self.layout_uno)

		self.connect(self.botonAgregar,SIGNAL("clicked()"),self.agregarEstudiante)
		self.manejadorBD = ManejadorBD()
		#agrego la tabla de alumnos
		self.alumnos.setHeader(self.headerEstudainte)
		self.alumnos.addTable(self.manejadorBD.consultarEstudiante2())
		self.busqueda.textChanged.connect(self.alumnos.on_lineEdit_textChanged)
		self.comboBusqueda.currentIndexChanged.connect(self.alumnos.on_comboBox_currentIndexChanged)
		#agrego datos a la tabla curso
		self.HeadersCurso= [u"Código", u"Número", u"Año Lectivo", "Paralelo",u"Cédula Profesor"]
		self.cursos.setHeader(self.HeadersCurso)
		self.cursos.addTable(self.manejadorBD.obtenerCursos())


		self.connect(self.botonAsignar,SIGNAL("clicked()"),self.eventoAsignar)
		self.setLayout(self.contenedor)

	def initBusqueda(self):
		primeraFila=QHBoxLayout()
		primeraFila.addWidget(QLabel("			"))
		primeraFila.addWidget(QLabel("Tipo de Busqueda"))
		primeraFila.addWidget(self.comboBusqueda)
		primeraFila.addWidget(self.busqueda)
		primeraFila.addWidget(self.botonAgregar)
		primeraFila.addWidget(QLabel("			"))
		 
		self.contenedor.addLayout(primeraFila)

	def agregarEstudiante(self):
		self.vistaAgregarEst=VistaAgregarEstudiante()
		self.vistaAgregarEst.show()

	def seleccionAlumno(self):
		self.A=self.alumnos.getSelectedRegister()

	def seleccionCurso(self):
		self.C=self.cursos.getSelectedRegister()

	def eventoAsignar(self):
		self.seleccionAlumno()
		self.seleccionCurso()
		if(len(self.A) !=0 and len(self.C) != 0):
			alumno=self.A[len(self.A)-1]
			curso=self.C[len(self.C)-1]
			self.manejadorBD.agregarEstudianteEnCurso(curso[0],alumno[0])
			self.A=[]
			self.C=[]
			QMessageBox.about(self,'Informacion',u'Se agrego el estudiante en el curso de forma satisfactoria')
		else:
			QMessageBox.about(self,'Error!',u'No se ha seleccionado curso y estudiante')




class VistaAgregarEstudiante(QWidget):
	dimension_x=600
	dimension_y=500

	def __init__(self,*args):
		QWidget.__init__(self,*args)
		self.setWindowTitle("Agregar Estudiante")
		self.setGeometry(100,50,self.dimension_x,self.dimension_y)
		#validadores
		#expresiones regulares para los nombres
		self.regex = QRegExp(u"^[À-Ÿà-ÿA-Za-z\\s*\\u'\xf1'*]+$")
		self.validator = QRegExpValidator(self.regex)
		#expresiones regulares para la cedula
		self.regexN = QRegExp("[0-9]*")
		self.validatorN = QRegExpValidator(self.regexN)
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
		self.initPadre()
		self.initMadre()
		self.initRepresentante()
		self.setLayout(self.contenedor)


	def initEstudiante(self):
		self.layout_estudiante=QVBoxLayout()
		self.listaLayouts=[QFormLayout(),QFormLayout()]
		
		#for i in range(8):
		#	self.listaLayouts.append(QFormLayout())

		listDatosEst = [u"Cédula:","Nombres:","Apellidos:", "Sexo:","Estado Civil:","Origen:","Etnia:" ,"Fecha de nacimiento:"]
		indiceSexo=3
		indiceEstadoCivil=4
		self.textos=[QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit()]
		for i in range(0,3):
			self.listaLayouts[0].addRow(QLabel(listDatosEst[i]),self.textos[i])

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
		self.textos[0].setValidator(self.validatorN)


		self.layout_estudiante.addLayout(self.listaLayouts[0])


		self.estudiante.setLayout(self.layout_estudiante)
		#validaciones


	def initPadre(self):
		self.layout_Padre=QFormLayout()
		#creacion de cajas de texto
		self.ListaDatosPadre=["Cedula:","Nombres:","Apellidos:","Sexo:","Fecha de Nacimiento:","Estado Civil:","Ocupacion:","Lugar de Trabajo:","Ocupacion:"]
		self.ListaEntradasPadre=[QLineEdit(),QLineEdit(),QLineEdit(),QComboBox(),QCalendarWidget(),QComboBox(),QLineEdit(),QLineEdit()]
		for i in range(0,8):
			self.layout_Padre.addRow(self.ListaDatosPadre[i],self.ListaEntradasPadre[i])
		self.padre.setLayout(self.layout_Padre)
		#seteo las validaciones
		self.ListaEntradasPadre[0].setValidator(self.validatorN)

	def initMadre(self):
		self.layout_Madre=QFormLayout()
		#creacion de cajas de texto
		self.ListaDatosMadre=["Cedula:","Nombres:","Apellidos:","Sexo:","Fecha de Nacimiento:","Estado Civil:","Ocupacion:","Lugar de Trabajo:","Ocupacion:"]
		self.ListaEntradasMadre=[QLineEdit(),QLineEdit(),QLineEdit(),QComboBox(),QCalendarWidget(),QComboBox(),QLineEdit(),QLineEdit()]
		for i in range(0,8):
			self.layout_Madre.addRow(self.ListaDatosMadre[i],self.ListaEntradasMadre[i])
		self.madre.setLayout(self.layout_Madre)
		#seteo las validaciones
		self.ListaEntradasMadre[0].setValidator(self.validatorN)

	def initRepresentante(self):
		self.layout_Representante=QFormLayout()
		#creacion de cajas de texto
		self.ListaDatosRepresentante=["Cedula:","Nombres:","Apellidos:","Sexo:","Fecha de Nacimiento:","Estado Civil:","Ocupacion:","Lugar de Trabajo:","Ocupacion:"]
		self.ListaEntradasRepresentante=[QLineEdit(),QLineEdit(),QLineEdit(),QComboBox(),QCalendarWidget(),QComboBox(),QLineEdit(),QLineEdit()]
		for i in range(0,8):
			self.layout_Representante.addRow(self.ListaDatosRepresentante[i],self.ListaEntradasRepresentante[i])
		self.representante.setLayout(self.layout_Representante)
		#seteo las validaciones
		self.ListaEntradasRepresentante[0].setValidator(self.validatorN)

	def guardarEstudiante(self):
		pass