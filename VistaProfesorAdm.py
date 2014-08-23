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
			self.connect(self.btnGuardar,SIGNAL("clicked()"),self.accionGuardarEdicion)
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
			self.connect(self.btnCrear,SIGNAL("clicked()"),self.accionGuardarCreacion)

			self.profesores=MyTable(self)
			#agrego datos a la tabla
			self.headers= [u"Cédula", "Apellidos","Nombres"]
			self.profesores.setHeader(self.headers)
			self.manejador= ManejadorBD()
			self.profesores.addTable(self.manejador.consultarProfesores())
			self.profesores.setEditable(False)
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
			
			tab_widget.addTab(tab_creacion,"Crear")
			tab_widget.addTab(tab_consultas,u"Consultar")
			tab_widget.addTab(tab_edicionElim,u"Edición")

			self.botonObtenerInfo=QPushButton("Obtener Informacion del Profesor")
			self.connect(self.botonObtenerInfo,SIGNAL("clicked()"),self.mostrarInfoProfesor)

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
		
		primeraFila = QVBoxLayout()
		GBoxProfInfo = QGroupBox ( "Profesor" )
		vboxProfInfo = QFormLayout()
		GBoxProfInfo.setLayout(vboxProfInfo)
		primeraFila.addWidget(self.botonObtenerInfo)
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


	def mostrarInfoProfesor(self):
		profesoresSeleccionados=self.profesores. getSelectedRegister()
		profesor=profesoresSeleccionados[0]#el primer registro seleccionado
		resultados=self.manejador.obtenerInfoProfesor(profesor[0])
		registro=resultados[0]
		for i in range(len(registro)):
			self.labelsProfesor[i].setText(QString(str(registro[i])))  

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
		profesoresSeleccionados=self.profesores.getSelectedRegister()
		profesor=profesoresSeleccionados[0]#el primer registro seleccionado
		resultados=self.manejador.obtenerInfoProfesor(profesor[0])
		registro=resultados[0]
		for i in range(len(registro)):
			if i!=0:
				self.editorProfesor[i].setReadOnly(False)
			else:
				self.editorProfesor[i].setEnabled(False)
			self.editorProfesor[i].setText(QString(str(registro[i])))  


	def accionGuardarCreacion(self):
		try:
			cedula = self.textCamposProfesor[0].displayText()
			nombre = unicode(self.textCamposProfesor[1].displayText())
			apellido = unicode(self.textCamposProfesor[2].displayText())
			usuario = unicode(self.textCamposProfesor[3].displayText())
			clave = unicode(self.textCamposProfesor[4].displayText())

			if (not(len(cedula)==10)):
				mensaje = QMessageBox.about(self, 'Error',u'Cédula inválida: debe tener 10 dígitos')
			elif (cedula =="" or nombre == "" or apellido == "" or usuario =="" or clave == ""):
				mensaje = QMessageBox.about(self, 'Error',u'Datos sin llenar: llene todos los datos')
			else:
				tupla = (cedula, nombre, apellido, usuario, clave)
				resultado=self.manejador.existeUsuarioProfesor(usuario)
				if(len(resultado)==0):#el usuario que se desea insertar no existe
					self.manejador.insertarProfesor(tupla)
					QMessageBox.about(self,"Aviso",u'Se ha creado un nuevo profesor con éxito')
				else:#el usuario que se desea insertar si existe
					mensaje = QMessageBox.about(self, 'Error',u'Usuario ya existente en el Sistema')

				for i in self.textCamposProfesor:
					i.setText("")

				self.actualizarProfesores()
		except:
			QMessageBox.about(self, 'Error',u'Datos Invalidos')


	def accionGuardarEdicion(self):
		try:
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
				tupla=(cedula,nombre,apellido,usuario,clave)
				resultados=self.manejador.existeUsuarioRepetido(cedula,usuario)
				if(len(resultados)==0):
					self.manejador.editarProfesor(tupla)
					QMessageBox.about(self,"Aviso",u'Se han guardado los cambios con éxito')		
					for i in self.editorProfesor:
						i.setReadOnly(True)
					self.actualizarProfesores()
				else:
					QMessageBox.about(self,"Error",u'Usuario ya existente en el sistema')				
		except:
			QMessageBox.about(self, 'Error',u'Datos invalidos')


	def actualizarProfesores(self):
		self.profesores.deleteData()
		self.profesores.addTable(self.manejador.consultarProfesores())
		self.profesores.setEditable(False)
