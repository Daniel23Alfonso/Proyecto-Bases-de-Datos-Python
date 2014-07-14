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
			self.paramBusqueda = QLineEdit() #entrada de texto usada para ingresar el parametro de busqueda
			self.btnBuscar = QPushButton() # boton para aceptar la busqueda
			self.btnBuscar.setIcon(QIcon("Imagenes/buscar.jpg"))
			self.comboBusquedaEstudiante=QComboBox() #tipos de usuario mostrados en un combo box
			self.comboBusquedaEstudiante.addItems(self.tipoBusqueda)
			
			self.alumnos=MyTable()
			
			
			# creacion de pestañas
			tab_widget = QTabWidget()
			tab_consultas = QWidget() #se crean dos pestañas
			tab_edicion = QWidget()
			
			#agrego las pestañas
			self.cont_consulta = QVBoxLayout(tab_consultas) #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.cont_edicion = QHBoxLayout(tab_edicion)
			
			tab_widget.addTab(tab_consultas,u"Consultas")
			tab_widget.addTab(tab_edicion,u"Edición")
			
			self.llenarTabConsultas()
			
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
		vboxEstInfo = QVBoxLayout()
		GBoxEstudianteInfo.setLayout(vboxEstInfo)
		terceraFila.addWidget(GBoxEstudianteInfo)
		contenidoTab.addLayout(terceraFila)
		GBoxPadreInfo = QGroupBox ( "Padre" )
		vboxPadreInfo = QVBoxLayout()
		GBoxPadreInfo.setLayout(vboxPadreInfo)
		terceraFila.addWidget(GBoxPadreInfo)
		
		#cuarta fila
		cuartaFila = QHBoxLayout()
		GBoxMadreInfo = QGroupBox ( "Madre" )
		vboxMadreInfo = QVBoxLayout()
		GBoxMadreInfo.setLayout(vboxEstInfo)
		cuartaFila.addWidget(GBoxMadreInfo)
		GBoxRepInfo = QGroupBox ( "Representante" )
		vboxRepInfo = QVBoxLayout()
		GBoxRepInfo.setLayout(vboxRepInfo)
		cuartaFila.addWidget(GBoxRepInfo)
		contenidoTab.addLayout(cuartaFila)