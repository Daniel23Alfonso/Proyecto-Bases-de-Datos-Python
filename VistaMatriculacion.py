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
		self.manejadorBD = ManejadorBD()
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
		self.personaFactura=QWidget()
		self.tab_uno.addTab(self.estudiante,"Estudiante")
		self.tab_uno.addTab(self.padre,"Padre")
		self.tab_uno.addTab(self.madre,"Madre")
		self.tab_uno.addTab(self.representante,"Representante")
		self.tab_uno.addTab(self.personaFactura,"Persona Factura")
		self.contenedor.addWidget(self.tab_uno)
		self.initEstudiante()
		self.initPadre()
		self.initMadre()
		self.initRepresentante()
		self.initPersonaFacura()
		self.setLayout(self.contenedor)
		self.connect(self.btnGuardar,SIGNAL("clicked()"),self.guardarEstudiante)
		

	def initPersonaFacura(self):
		self.layout_PersonaFactura=QVBoxLayout()
		self.layout_PersonaFactura1=QFormLayout()
		self.layout_PersonaFactura2=QHBoxLayout()
		self.lisDatosPersona=[u"Cédula: ","Nombres: ","Apellidos: ","Telefono: ","Direccion: "]
		self.lisEntradasPersona=[QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit()]
		self.lisEntradasPersona[0].setValidator(self.validatorN)
		self.btnGuardar=QPushButton("Guardar")
		i=0
		for l in self.lisDatosPersona:
			self.layout_PersonaFactura1.addRow(l,self.lisEntradasPersona[i])
			i=i+1	
		self.layout_PersonaFactura.addLayout(self.layout_PersonaFactura1)
		self.layout_PersonaFactura2.addWidget(self.btnGuardar)
		self.layout_PersonaFactura.addLayout(self.layout_PersonaFactura2)
		self.personaFactura.setLayout(self.layout_PersonaFactura)

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

		self.sexos=["MASCULINO","FEMENINO"]
		self.EstadoCivil=["SOLTERO(A)","CASADO(A)","DIVORCIADO(A)","VIUDO(A)","UNIDO(A)"]

		self.comboSexo=QComboBox()
		
		self.comboSexo.addItems(self.sexos)

		self.comboEstadoCivil=QComboBox()
		
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
		self.ListaDatosPadre=["Cedula:","Nombres:","Apellidos:","Sexo:","Fecha de Nacimiento:","Estado Civil:","Ocupacion:","Lugar de Trabajo:","Ocupacion:","Telefono: ","Direccion: "]
		self.ListaEntradasPadre=[QLineEdit(),QLineEdit(),QLineEdit(),QComboBox(),QCalendarWidget(),QComboBox(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit()]
		for i in range(0,10):
			self.layout_Padre.addRow(self.ListaDatosPadre[i],self.ListaEntradasPadre[i])
		self.padre.setLayout(self.layout_Padre)
		#seteo las validaciones
		self.ListaEntradasPadre[0].setValidator(self.validatorN)
		self.ListaEntradasPadre[3].addItems(self.sexos)
		self.ListaEntradasPadre[5].addItems(self.EstadoCivil)


	def initMadre(self):
		self.layout_Madre=QFormLayout()
		#creacion de cajas de texto
		self.ListaDatosMadre=["Cedula:","Nombres:","Apellidos:","Sexo:","Fecha de Nacimiento:","Estado Civil:","Ocupacion:","Lugar de Trabajo:","Ocupacion:","Telefono: ","Direccion: "]
		self.ListaEntradasMadre=[QLineEdit(),QLineEdit(),QLineEdit(),QComboBox(),QCalendarWidget(),QComboBox(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit()]
		for i in range(0,10):
			self.layout_Madre.addRow(self.ListaDatosMadre[i],self.ListaEntradasMadre[i])
		self.madre.setLayout(self.layout_Madre)
		#seteo las validaciones
		self.ListaEntradasMadre[0].setValidator(self.validatorN)
		self.ListaEntradasMadre[3].addItems(self.sexos)
		self.ListaEntradasMadre[5].addItems(self.EstadoCivil)

	def initRepresentante(self):
		self.layout_Representante=QFormLayout()
		#creacion de cajas de texto
		self.ListaDatosRepresentante=["Cedula:","Nombres:","Apellidos:","Sexo:","Fecha de Nacimiento:","Estado Civil:","Ocupacion:","Lugar de Trabajo:","Ocupacion:","Telefono: ","Direccion: "]
		self.ListaEntradasRepresentante=[QLineEdit(),QLineEdit(),QLineEdit(),QComboBox(),QCalendarWidget(),QComboBox(),QLineEdit(),QLineEdit(),QLineEdit(),QLineEdit()]
		for i in range(0,10):
			self.layout_Representante.addRow(self.ListaDatosRepresentante[i],self.ListaEntradasRepresentante[i])
		self.representante.setLayout(self.layout_Representante)
		#seteo las validaciones
		self.ListaEntradasRepresentante[0].setValidator(self.validatorN)
		self.ListaEntradasRepresentante[3].addItems(self.sexos)
		self.ListaEntradasRepresentante[5].addItems(self.EstadoCivil)

	def guardarEstudiante(self):
		tuplaEstudiante=self.obtenerEstudiante()
		tuplaPadre=self.obtenerPadre()
		tuplaMadre=self.obtenerMadre()
		tuplaRepresentante=self.obtenerRepresentante()
		tuplaPersonaF=self.obtenerPersonaFactura()
		#try:
		self.manejadorBD.crearEstudiante(tuplaEstudiante,tuplaPadre,tuplaMadre,tuplaRepresentante,tuplaPersonaF)
		#QMessageBox.about(self,'Aviso!',u'Se Creo Correctamente a el Estudiante')
		#except Exception, e:
		#	QMessageBox.about(self,'Error!',u'No se ha podido Crear el Estudiante')
		



	def obtenerEstudiante(self):
		fecha=self.calendario.selectedDate ()
		strFecha=self.obtenerFechaString(fecha)
		return (self.textos[0].displayText(),self.textos[1].displayText(),self.textos[2].displayText(), self.comboSexo.currentText(),self.comboEstadoCivil.currentText(),self.textos[3].displayText(),self.comboEtnia.currentText(),strFecha,self.lisEntradasPersona[0].displayText())

	def obtenerPadre(self):
		fecha=self.ListaEntradasRepresentante[4].selectedDate ()
		strFecha=self.obtenerFechaString(fecha)
		return (self.ListaEntradasPadre[0].displayText(),self.ListaEntradasPadre[1].displayText(),self.ListaEntradasPadre[2].displayText(), self.ListaEntradasPadre[3].currentText(),strFecha,self.ListaEntradasPadre[5].currentText(),self.ListaEntradasPadre[6].displayText(),self.ListaEntradasPadre[7].displayText(),self.ListaEntradasPadre[8].displayText(),self.ListaEntradasPadre[9].displayText())
		
	def obtenerMadre(self):
		fecha=self.ListaEntradasMadre[4].selectedDate ()
		strFecha=self.obtenerFechaString(fecha)
		return (self.ListaEntradasMadre[0].displayText(),self.ListaEntradasMadre[1].displayText(),self.ListaEntradasMadre[2].displayText(), self.ListaEntradasMadre[3].currentText(),strFecha,self.ListaEntradasMadre[5].currentText(),self.ListaEntradasMadre[6].displayText(),self.ListaEntradasMadre[7].displayText(),self.ListaEntradasMadre[8].displayText(),self.ListaEntradasMadre[9].displayText())
		

	def obtenerRepresentante(self):
		fecha=self.ListaEntradasRepresentante[4].selectedDate ()
		strFecha=self.obtenerFechaString(fecha)
		return (self.ListaEntradasRepresentante[0].displayText(),self.ListaEntradasRepresentante[1].displayText(),self.ListaEntradasRepresentante[2].displayText(), self.ListaEntradasRepresentante[3].currentText(),strFecha,self.ListaEntradasRepresentante[5].currentText(),self.ListaEntradasRepresentante[6].displayText(),self.ListaEntradasRepresentante[7].displayText(),self.ListaEntradasRepresentante[8].displayText(),self.ListaEntradasRepresentante[9].displayText())
	
	def obtenerPersonaFactura(self):
		return(self.lisEntradasPersona[0].displayText(),self.lisEntradasPersona[1].displayText(),self.lisEntradasPersona[2].displayText(),self.lisEntradasPersona[3].displayText(),self.lisEntradasPersona[4].displayText())

	def obtenerFechaString(self,date):
		dia=date.day()
		mes=date.month()
		anio=date.year()
		return "%d-%d-%d" %(anio,mes,dia)