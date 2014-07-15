# -*- coding: utf-8 -*- 

import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *

class VistaEstudiantes(QWidget):
	dimension_x=400
	dimension_y=500

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma vertical
			self.setLayout(self.contenedor)

			#componentes que iran en la ventana
			self.tipoBusqueda=[u"Cédula","Apellido","Nombre"]
			self.tipoBusquedaEdit = ["Apellidos", "Nombre"]
			self.paramBusqueda = QLineEdit() #entrada de texto usada para ingresar el parametro de busqueda seccion Consultas
			self.btnBuscar = QPushButton() # boton para aceptar la busqueda
			self.btnBuscar.setIcon(QIcon("Imagenes/buscar.jpg"))
			self.comboBusquedaEstudiante=QComboBox() #tipos de usuario mostrados en un combo box
			self.comboBusquedaEstudiante.addItems(self.tipoBusqueda)
			

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

			
			#lineas de texto para deditar al estudiante
			self.textDatosEstudiantes = [ QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit(),QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit() ]

			for i in self.textDatosEstudiantes:
				i.setReadOnly(True)

			self.alumnos=MyTable()
			
			
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
			
			self.contenedor.addWidget(tab_widget)
			
	
	def llenarTabConsultas(self):
		"""
		Esta funcion sirve para llenar los elementos de la pestaña consultas
		"""
		contenidoTab = self.cont_consulta
		
		# aqui estoy creando la primera fila de la pestaña
		primeraFila = QHBoxLayout() # primera fila, contiene el combobox y la entrada de texto
		primeraFila.addWidget(self.comboBusquedaEstudiante)
		primeraFila.addWidget(self.paramBusqueda)
		primeraFila.addWidget(self.btnBuscar)
		primeraFila.addWidget(QLabel("                         "))
		primeraFila.addWidget(QLabel("               "))
		contenidoTab.addLayout(primeraFila)
		
		#agrego una tabla donde habra informacion de los estudiantes, segunda fila
		contenidoTab.addWidget(self.alumnos)
		
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
		listDatosEst = ["Nombres:","Apellidos:",u"Cédula:", "Sexo:","Estado Civil:","Origen:","Etnia:" ,"Fecha de nacimiento:"]
		form_layout = QFormLayout()

		for i in range (0,7):
			form_layout.addRow(listDatosEst[i], self.textDatosEstudiantes[i])

		contenidoTab.addLayout(form_layout)

		cuartaFila = QHBoxLayout()
		cuartaFila.addWidget(self.btnEditar)
		cuartaFila.addWidget(self.btnGuardar)
		contenidoTab.addLayout(cuartaFila)


	def activarEdicion(self):
		for i in self.textDatosEstudiantes:
			i.setReadOnly(False)
