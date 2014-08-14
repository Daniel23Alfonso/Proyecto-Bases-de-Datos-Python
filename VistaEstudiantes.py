# -*- coding: utf-8 -*- 

import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *
from ManejadorBD import *

class VistaEstudiantes(QWidget):
	dimension_x=400
	dimension_y=500
	
	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma vertical
			self.setLayout(self.contenedor)


			#elementos de la tabla
			self.headersTabla = [u"Matrícula",u"Número de cédula", "Nombres", "Apellidos","Sexo", 
			"Estado Civil","Origen", "Etnia", "Fecha de Nacimiento"]
			self.manejadorBD = ManejadorBD() 

			#componentes que iran en la ventana
			self.tipoBusqueda=[u"Matrícula",u"Cédula","Nombres","Apellidos"]
			self.paramBusqueda = QLineEdit() #entrada de texto usada para ingresar el parametro de busqueda seccion Consultas
			self.comboBusquedaEstudiante=QComboBox() #tipos de usuario mostrados en un combo box
			self.comboBusquedaEstudiante.addItems(self.tipoBusqueda)
			

			#elementos de la pestaña de edicion
			self.btnEditar = QPushButton("Editar")
			self.btnEditar.setIcon(QIcon("Imagenes/editar.jpg"))
			self.connect(self.btnEditar,SIGNAL("clicked()"),self.activarEdicion)
			self.btnGuardar = QPushButton("Guardar")
			self.btnGuardar.setIcon(QIcon("Imagenes/guardar.jpg"))
			self.connect(self.btnGuardar,SIGNAL("clicked()"),self.accionGuadarEdicion)
			#labels que muestran informacion 
			self.labelsDatosEstudiantes = [ QLabel(""), QLabel(""), QLabel(""), QLabel(""),QLabel(""), QLabel(""), QLabel(""), QLabel("") ]
			
			#lables que muestran informacion del padre

			self.labelsDatosPadre = [ QLabel(""), QLabel(""), QLabel(""), QLabel(""), QLabel(""),
			QLabel(""), QLabel(""), QLabel(""), QLabel(""), QLabel("") ]

			#labels que muestran informacion de la madre

			self.labelsDatosMadre = [ QLabel(""), QLabel(""), QLabel(""), QLabel(""), QLabel(""),
			QLabel(""), QLabel(""), QLabel(""), QLabel(""), QLabel("") ]
			
			#lables que muestran informacion del representante

			self.labelsDatosRep = [ QLabel(""), QLabel(""), QLabel(""), QLabel(""), QLabel(""),
			QLabel(""), QLabel(""), QLabel(""), QLabel(""), QLabel("") ]

			#variables de la pestaña de edicion
			self.listsexos=["MASCULINO","FEMENINO"] #lista para escoger el tipo de usuario
			self.listEstCivil = ["SOLTERO(A)","CASADO(A)","DIVORCIADO(A)","VIUDO(A)","UNIDO(A)" ]
			self.listEtnia = ["BLANCO","MESTIZO","AFROECUATORIANO","INDIGENA", "MONTUBIO","NEGRO","MULATO","OTROS"]

			#lineas de texto para deditar al estudiante


			self.textDatosEstudiantes = [ QLineEdit(), QLineEdit(), QLineEdit(), QComboBox(), QComboBox(),
			QLineEdit(), QComboBox(), QLineEdit()]

			#expresiones regulares para los nombres
			self.regex = QRegExp(u"^[À-Ÿà-ÿA-Za-z\\s*\\u'\xf1'*]+$")
			self.validator = QRegExpValidator(self.regex)

			#expresiones regulares para la cedula
			self.regexN = QRegExp("[0-9]*")
			self.validatorN = QRegExpValidator(self.regexN)
						
			#itero los QLineEdit y les seteo la expresion regular y que sean solo de lectura
			for i in [0,1,2,5]:
				self.textDatosEstudiantes[i].setReadOnly(True)
			
			for i in [1,2,5]:
				self.textDatosEstudiantes[i].setValidator(self.validator)
			
			self.textDatosEstudiantes[0].setValidator(self.validatorN)

			
			#agrego la tabla de alumnos
			self.alumnos=MyTable(self)
			self.alumnos.setHeader(self.headersTabla)
			self.alumnos.addTable(self.manejadorBD.consultarEstudiante())
			self.paramBusqueda.textChanged.connect(self.alumnos.on_lineEdit_textChanged)
			self.comboBusquedaEstudiante.currentIndexChanged.connect(self.alumnos.on_comboBox_currentIndexChanged)

			
			
			# creacion de pestañas
			tab_widget = QTabWidget()
			tab_consultas = QScrollArea () #se crean dos pestañas
			tab_edicion = QWidget ()
			tab_consultas.setWidget(QWidget())
			tab_consultas. setWidgetResizable ( True )
			
			#agrego las pestañas
			self.cont_consulta = QVBoxLayout(tab_consultas.widget()) #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.cont_edicion = QVBoxLayout(tab_edicion)
			
			tab_widget.addTab(tab_consultas,u"Consultas")
			tab_widget.addTab(tab_edicion,u"Edición")
			
			self.llenarTabConsultas()
			self.llenarTabEdicion()
			self.layoutBusqueda=QHBoxLayout()
			self.layoutBusqueda.addWidget(self.comboBusquedaEstudiante)
			self.layoutBusqueda.addWidget(self.paramBusqueda)
			self.contenedor.addLayout(self.layoutBusqueda)
			self.contenedor.addWidget(self.alumnos)
			self.contenedor.addWidget(tab_widget)
			
	
	def llenarTabConsultas(self):
		"""
		Esta funcion sirve para llenar los elementos de la pestaña consultas
		"""
		contenidoTab = self.cont_consulta
		
		# aqui estoy creando la primera fila de la pestaña
		
		
		#creacion de la tercera fila
		terceraFila = QHBoxLayout()
		GBoxEstudianteInfo = QGroupBox ( "Estudiante" )
		vboxEstInfo = QFormLayout()
		GBoxEstudianteInfo.setLayout(vboxEstInfo)
		terceraFila.addWidget(GBoxEstudianteInfo)
		
		listDatosEst = ["Nombres:","Apellidos:",u"Cédula:", "Sexo:","Estado Civil:","Origen:","Etnia:" ,"Fecha de nacimiento:"]
		
		for i in range (0,8):
			vboxEstInfo.addRow(listDatosEst[i], self.labelsDatosEstudiantes[i])


		GBoxPadreInfo = QGroupBox ( "Padre" )
		vboxPadreInfo = QFormLayout()
		GBoxPadreInfo.setLayout(vboxPadreInfo)
		terceraFila.addWidget(GBoxPadreInfo)
		
		listDatosPersona = ["Nombres:","Apellidos:",u"Cédula:","Sexo:","Fecha de Nacimiento:","Estado Civil:",u"Ocupación",
		"Lugar de Trabajo:",u"Teléfono:", u"Dirección:"]

		for i in range (0,10):
			vboxPadreInfo.addRow(listDatosPersona[i], self.labelsDatosPadre[i])

		contenidoTab.addLayout(terceraFila)
		#cuarta fila
		cuartaFila = QHBoxLayout()
		GBoxMadreInfo = QGroupBox ( "Madre" )
		vboxMadreInfo = QFormLayout()
		GBoxMadreInfo.setLayout(vboxMadreInfo)
		cuartaFila.addWidget(GBoxMadreInfo)
		
		for i in range (0,10):
			vboxMadreInfo.addRow(listDatosPersona[i], self.labelsDatosMadre[i])

		GBoxRepInfo = QGroupBox ( "Representante" )
		vboxRepInfo = QFormLayout()
		GBoxRepInfo.setLayout(vboxRepInfo)
		cuartaFila.addWidget(GBoxRepInfo)
		contenidoTab.addLayout(cuartaFila)

		for i in range (0,10):
			vboxRepInfo.addRow(listDatosPersona[i], self.labelsDatosRep[i])



	def llenarTabEdicion(self):
		"""
		Esta funcion sirve para llenar los elementos de la pestaña consultas
		"""
		contenidoTab = self.cont_edicion
		listDatosEst = [u"Cédula","Nombres:","Apellidos:", "Sexo:","Estado Civil:","Origen:","Etnia:" ,"Fecha de nacimiento:"]
		form_layout = QFormLayout()

		for i in range (0,7):
			form_layout.addRow(listDatosEst[i], self.textDatosEstudiantes[i])

		contenidoTab.addLayout(form_layout)

		terceraFila = QHBoxLayout()
		terceraFila.addWidget(self.btnEditar)
		terceraFila.addWidget(self.btnGuardar)
		contenidoTab.addLayout(terceraFila)


	def activarEdicion(self):
		for i in [0,1,2,5]:
			self.textDatosEstudiantes[i].setReadOnly(False)

		self.textDatosEstudiantes[3].addItems(self.listsexos)
		self.textDatosEstudiantes[4].addItems(self.listEstCivil)
		self.textDatosEstudiantes[6].addItems(self.listEtnia)


	def accionGuadarEdicion(self):
		cedula = self.textDatosEstudiantes[0].displayText()
		nombre = self.textDatosEstudiantes[1].displayText()
		apellido = self.textDatosEstudiantes[2].displayText()
		origen = self.textDatosEstudiantes[5].displayText()

		if (not(len(cedula)==10)):
			QMessageBox.about(self, 'Error',u'Cédula inválida: debe tener 10 dígitos')
		elif (cedula =="" or nombre == "" or apellido == "" or origen =="" ):
			QMessageBox.about(self, 'Error',u'Datos sin llenar: llene todos los datos')
		else:
			QMessageBox.about(self,"Aviso",u'Se han guardado los cambios con éxito')
			for i in [0,1,2,5]:
				self.textDatosEstudiantes[i].setReadOnly(True)



