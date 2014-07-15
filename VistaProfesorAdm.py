# -*- coding: utf-8 -*- 

import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *

class VistaProfesorAdm(QWidget):
	dimension_x=700
	dimension_y=600

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma vertical
			self.setLayout(self.contenedor)

			#componentes que iran en la ventana
			#componentes de la pestaña consultas
			self.tipoBusqueda=[u"Cédula","Apellido","Nombre"]
			self.tipoBusquedaEdit = ["Apellidos", "Nombre"]
			self.paramBusqueda = QLineEdit() #entrada de texto usada para ingresar el parametro de busqueda seccion Consultas
			self.btnBuscar = QPushButton() # boton para aceptar la busqueda
			self.btnBuscar.setIcon(QIcon("Imagenes/buscar.jpg"))
			self.comboBusquedaProfesor=QComboBox() #tipos de usuario mostrados en un combo box
			self.comboBusquedaProfesor.addItems(self.tipoBusqueda)
			self.labelsProfesor = [QLabel(""),QLabel(""),QLabel(""),QLabel(""),QLabel(""),QLabel("")]
			

			#elementos de la pestaña de edicion
			self.paramBusquedaEdit = QLineEdit() #entrada de texto usada para ingresar el parametro de busqueda seccion Consultas
			self.cedulaEdit = QLineEdit()  # entrada de texto donde se ingresa la cedula 
			self.btnBuscarEdit = QPushButton("Buscar") # boton para aceptar la busqueda
			self.btnBuscarEdit.setIcon(QIcon("Imagenes/buscar.jpg"))
			self.comboBusquedaEdit=QComboBox() #tipos de usuario mostrados en un combo box
			self.comboBusquedaEdit.addItems(self.tipoBusquedaEdit)
			self.btnEditar = QPushButton("Editar")
			self.btnEditar.setIcon(QIcon("Imagenes/editar.jpg"))
			self.connect(self.btnEditar,SIGNAL("clicked()"),self.activarEdicion)
			self.btnGuardar = QPushButton("Guardar")
			self.btnGuardar.setIcon(QIcon("Imagenes/guardar.jpg"))
			#cuadros de texto que permiten editar
			self.editorProfesor = [ QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit(),QLineEdit(), QLineEdit()]
			for i in self.editorProfesor:
				i.setReadOnly(True)
			
			#atributos de creacion
			#lineas de texto para crear al profesor
			self.textCamposProfesor = [ QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit(),QLineEdit()]
			self.btnCrear = QPushButton("Guardar")
			self.btnCrear.setIcon(QIcon("Imagenes/guardar.jpg"))

			self.profesores=MyTable()
			
			
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
			self.contenedor.addWidget(tab_widget)
			
	
	def llenarTabConsultas(self):
		"""
		Esta funcion sirve para llenar los elementos de la pestaña consultas
		"""
		contenidoTab = self.cont_consulta
		
		# aqui estoy creando la primera fila de la pestaña
		primeraFila = QHBoxLayout() # primera fila, contiene el combobox y la entrada de texto
		primeraFila.addWidget(self.comboBusquedaProfesor)
		primeraFila.addWidget(self.paramBusqueda)
		primeraFila.addWidget(self.btnBuscar)
		primeraFila.addWidget(QLabel("                         "))
		primeraFila.addWidget(QLabel("               "))
		contenidoTab.addLayout(primeraFila)
		
		#agrego una tabla donde habra informacion de los estudiantes, segunda fila
		contenidoTab.addWidget(self.profesores)
		
		#creacion de la tercera fila
		terceraFila = QHBoxLayout()
		GBoxProfInfo = QGroupBox ( "Profesor" )
		vboxProfInfo = QFormLayout()
		GBoxProfInfo.setLayout(vboxProfInfo)
		terceraFila.addWidget(GBoxProfInfo)
		
		listDatosEProf = [u"Cédula:","Nombres:", "Apellidos:","Usuario:","Clave:"]
		
		for i in range (0,5):
			vboxProfInfo.addRow(listDatosEProf[i], self.labelsProfesor[i])

		contenidoTab.addLayout(terceraFila)


		



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
		primeraFila = QHBoxLayout() # primera fila, contiene el combobox y la entrada de texto
		primeraFila.addWidget(self.comboBusquedaEdit)
		primeraFila.addWidget(self.paramBusquedaEdit)
		contenidoTab.addLayout(primeraFila)
		segundaFila = QHBoxLayout()
		segundaFila.addWidget(QLabel(u"Cédula"))
		segundaFila.addWidget(self.cedulaEdit)
		segundaFila.addWidget(self.btnBuscarEdit)
		contenidoTab.addLayout(segundaFila)
		textoCampos = [u"Cédula:","Nombres:", "Apellidos:","Usuario:","Clave:"]
		form_layout = QFormLayout()

		for i in range (0,5):
			form_layout.addRow(textoCampos[i], self.editorProfesor[i])

		contenidoTab.addLayout(form_layout)

		cuartaFila = QHBoxLayout()
		cuartaFila.addWidget(self.btnEditar)
		cuartaFila.addWidget(self.btnGuardar)
		contenidoTab.addLayout(cuartaFila)


	def activarEdicion(self):
		for i in self.editorProfesor:
			i.setReadOnly(False)