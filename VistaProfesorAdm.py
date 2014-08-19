# -*- coding: utf-8 -*- 

import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *
from ManejadorBD import*

class VistaProfesorAdm(QWidget):
	dimension_x=700
	dimension_y=600

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma vertical
			self.setLayout(self.contenedor)

			#componentes que iran en la ventana
			

			self.tipoBusqueda=[u"Cédula","Nombres","Apellidos"]
			self.paramBusqueda = QLineEdit() #entrada de texto usada para ingresar el parametro de busqueda seccion Consultas
			self.btnBuscar = QPushButton() # boton para aceptar la busqueda
			self.btnBuscar.setIcon(QIcon("Imagenes/buscar.jpg"))
			self.comboBusquedaProfesor=QComboBox() #tipos de usuario mostrados en un combo box
			self.comboBusquedaProfesor.addItems(self.tipoBusqueda)
			
			#COMPONENTES DE LA VENTANA CONSULTAS
			self.labelsProfesor = [QLabel(""),QLabel(""),QLabel(""),QLabel(""),QLabel(""),QLabel("")]
			

			#elementos de la pestaña de EDICION
			
			# expresion regular`para validar nombres
			self.regex = QRegExp(u"^[À-Ÿà-ÿA-Za-z\\s*\\u'\xf1'*]+$")
			self.validator = QRegExpValidator(self.regex)

			#expresiones regulares para la cedula
			self.regexN = QRegExp("[0-9]*")
			self.validatorN = QRegExpValidator(self.regexN)

			self.btnEditar = QPushButton("Editar")
			self.btnEditar.setIcon(QIcon("Imagenes/editar.jpg"))
			self.connect(self.btnEditar,SIGNAL("clicked()"),self.activarEdicion)
			self.btnGuardar = QPushButton("Guardar")
			self.btnGuardar.setIcon(QIcon("Imagenes/guardar.jpg"))
			self.connect(self.btnGuardar,SIGNAL("clicked()"),self.accionGuadarEdicion)
			#cuadros de texto que permiten editar
			self.editorProfesor = [ QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit(),QLineEdit(), QLineEdit()]
			
			for i in self.editorProfesor:
				i.setReadOnly(True)

			for i in range(1,4):
				self.editorProfesor[i].setValidator(self.validator)

			self.editorProfesor[0].setValidator(self.validatorN)

			
			#ATRIBUTOS DE CREACION
			#lineas de texto para crear al profesor
			self.textCamposProfesor = [ QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit(),QLineEdit()]
			
			#seteo la expresion regular en los QLineEdit
			for i in range(1,4):
				self.textCamposProfesor[i].setValidator(self.validator)

			self.textCamposProfesor[0].setValidator(self.validatorN)


			self.btnCrear = QPushButton("Guardar")
			self.btnCrear.setIcon(QIcon("Imagenes/guardar.jpg"))
			self.connect(self.btnCrear,SIGNAL("clicked()"),self.accionGuadarCreacion)



			self.profesores=MyTable(self)
			#agrego datos a la tabla
			self.headers= [u"Cédula", "Nombres", "Apellidos"]
			self.profesores.setHeader(self.headers)
			self.manejador= ManejadorBD()
			self.profesores.addTable(self.manejador.consultarProfesores())
			self.paramBusqueda.textChanged.connect(self.profesores.on_lineEdit_textChanged)
			self.comboBusquedaProfesor.currentIndexChanged.connect(self.profesores.on_comboBox_currentIndexChanged)


			
			
			# creacion de pestañas
			tab_widget = QTabWidget()
			tab_consultas = QWidget() #se crean dos pestañas
			tab_creacion = QWidget()
			tab_edicionElim = QWidget ()
			
			#agrego las pestañas
			self.cont_consulta = QVBoxLayout(tab_consultas) #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.cont_creacion = QVBoxLayout(tab_creacion)
			self.cont_edicionElim = QVBoxLayout(tab_edicionElim)
			
			tab_widget.addTab(tab_consultas,u"Consultas")
			tab_widget.addTab(tab_creacion,"Crear")
			tab_widget.addTab(tab_edicionElim,u"Edición")
			
			self.llenarTabConsultas()
			self.llenarTabEdicion()
			self.llenarTabCreacion()
			self.primeraFila = QHBoxLayout()
			self.primeraFila.addWidget(self.comboBusquedaProfesor)
			self.primeraFila.addWidget(self.paramBusqueda)
			self.primeraFila.addWidget(self.btnBuscar)
			self.contenedor.addLayout(self.primeraFila)
			self.contenedor.addWidget(self.profesores)
			self.contenedor.addWidget(tab_widget)
			
	
	def llenarTabConsultas(self):
		"""
		Esta funcion sirve para llenar los elementos de la pestaña consultas
		"""
		contenidoTab = self.cont_consulta
		
		# aqui estoy creando la primera fila de la pestaña
		
		primeraFila = QHBoxLayout()
		GBoxProfInfo = QGroupBox ( "Profesor" )
		vboxProfInfo = QFormLayout()
		GBoxProfInfo.setLayout(vboxProfInfo)
		primeraFila.addWidget(GBoxProfInfo)
		
		listDatosEProf = [u"Cédula:","Nombres:", "Apellidos:","Usuario:","Clave:"]
		
		for i in range (0,5):
			vboxProfInfo.addRow(listDatosEProf[i], self.labelsProfesor[i])

		contenidoTab.addLayout(primeraFila)


		



	def llenarTabCreacion(self):
		contenidoTab = self.cont_creacion
		textoCampos = [u"Cédula:","Nombres:", "Apellidos:","Usuario:","Clave:"]
		form_layout = QFormLayout()
		form_layout.addRow("Ingrese correctamente los campos:",QLabel("    "))
		form_layout.addRow(QLabel("    "))

		for i in range (0,5):
			form_layout.addRow(textoCampos[i], self.textCamposProfesor[i])

		contenidoTab.addLayout(form_layout)

		fila = QHBoxLayout()
		fila.addWidget(self.btnCrear)
		fila.addWidget(QLabel("                         "))
		contenidoTab.addLayout(fila)





	def llenarTabEdicion(self):
		"""
		Esta funcion sirve para llenar los elementos de la pestaña consultas
		"""
		contenidoTab = self.cont_edicionElim
		
		# aqui estoy creando la primera fila de la pestaña
		
		textoCampos = [u"Cédula:","Nombres:", "Apellidos:","Usuario:","Clave:"]
		form_layout = QFormLayout()

		for i in range (0,5):
			form_layout.addRow(textoCampos[i], self.editorProfesor[i])

		contenidoTab.addLayout(form_layout)

		terceraFila = QHBoxLayout()
		terceraFila.addWidget(self.btnEditar)
		terceraFila.addWidget(self.btnGuardar)
		contenidoTab.addLayout(terceraFila)


	def activarEdicion(self):
		for i in self.editorProfesor:
			i.setReadOnly(False)


	def accionGuadarCreacion(self):
		cedula = self.textCamposProfesor[0].displayText()
		nombre = self.textCamposProfesor[1].displayText()
		apellido = self.textCamposProfesor[2].displayText()
		usuario = self.textCamposProfesor[3].displayText()
		clave = self.textCamposProfesor[4].displayText()

		if (not(len(cedula)==10)):
			mensaje = QMessageBox.about(self, 'Error',u'Cédula inválida: debe tener 10 dígitos')
		elif (cedula =="" or nombre == "" or apellido == "" or usuario =="" or clave == ""):
			mensaje = QMessageBox.about(self, 'Error',u'Datos sin llenar: llene todos los datos')
		else:
			mensaje = QMessageBox.about(self,"Aviso",u'Se ha creado un nuevo profesor con éxito')
			tupla = (cedula, nombre, apellido, usuario, clave)
			self.manejador.insertarProfesor(tupla)
			for i in self.textCamposProfesor:
				i.setText("")


	def accionGuadarEdicion(self):
		cedula = self.editorProfesor[0].displayText()
		nombre = self.editorProfesor[1].displayText()
		apellido = self.editorProfesor[2].displayText()
		usuario = self.editorProfesor[3].displayText()
		clave = self.editorProfesor[4].displayText()

		if (not(len(cedula)==10)):
			QMessageBox.about(self, 'Error',u'Cédula inválida: debe tener 10 dígitos')
		elif (cedula =="" or nombre == "" or apellido == "" or usuario =="" or clave == ""):
			QMessageBox.about(self, 'Error',u'Datos sin llenar: llene todos los datos')
		else:
			QMessageBox.about(self,"Aviso",u'Se han guardado los cambios con éxito')
			for i in self.editorProfesor:
				i.setReadOnly(True)

