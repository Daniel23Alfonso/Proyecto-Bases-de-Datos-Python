# -*- coding: utf-8 -*- 

import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *
from ManejadorBD import*

class VistaPersona(QWidget):
	dimension_x=400
	dimension_y=500

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.setLayout(self.contenedor)
			self.Personas=MyTable(self)
			self.layoutPersona=QFormLayout()
			self.layoutBotones=QHBoxLayout()
			self.layoutBusqueda=QFormLayout()
			#definicion cajas de texto
			self.cedula=QLineEdit()
			self.nombre=QLineEdit()
			self.apellido=QLineEdit()
			self.sexo=QComboBox()
			self.sexo.addItems(["Masculino","Femenino"])
			self.estadoCivil=QComboBox()
			self.estadoCivil.addItems(["Soltero","Casado","Divorsiado","Union Libre","Viudo"])
			self.ocupacion=QLineEdit()
			self.lugarTrabajo=QLineEdit()
			self.telefono=QLineEdit()
			self.direccion=QLineEdit()
			#botones
			self.btnEditar=QPushButton("Editar")
			self.btnEditar.setIcon(QIcon("Imagenes/editar.jpg"))
			self.btnGuardar=QPushButton("Guardar")
			self.btnGuardar.setIcon(QIcon("Imagenes/guardar.jpg"))
			self.btnEliminar=QPushButton("Eliminar")
			#definicion objetos busqueda
			self.comboBusqueda=QComboBox()
			self.txtBusqueda=QLineEdit()
			self.comboBusqueda.addItems([u"cédula","Nombres","Apellidos"])

			# llenamos el layout de los botones
			self.layoutBotones.addWidget(self.btnEditar)
			self.layoutBotones.addWidget(self.btnGuardar)
			self.layoutBotones.addWidget(self.btnEliminar)

			#creacion de formulario
			self.layoutPersona.addRow("cedula: ",self.cedula)
			self.layoutPersona.addRow("Nombre: ",self.nombre)
			self.layoutPersona.addRow("Apellido: ",self.apellido)
			self.layoutPersona.addRow("sexo: ",self.sexo)
			self.layoutPersona.addRow("Estado Civil: ",self.estadoCivil)
			self.layoutPersona.addRow("Ocupacion: ",self.ocupacion)
			self.layoutPersona.addRow("Lugar Trabajo: ",self.lugarTrabajo)
			self.layoutPersona.addRow("Telefono: ",self.telefono)
			self.layoutPersona.addRow("Direccion: ",self.direccion)

			#creacion de layout busqueda
			self.layoutBusqueda.addRow(self.comboBusqueda,self.txtBusqueda)

			#agregamos los layout a la ventana
			self.contenedor.addLayout(self.layoutBusqueda)
			self.contenedor.addWidget(self.Personas)
			self.contenedor.addLayout(self.layoutPersona)
			self.contenedor.addLayout(self.layoutBotones)

			#tablas
			self.manejador = ManejadorBD()
			self.headers= [u"Cédula", "Nombres", "Apellidos", "Sexo", "Fecha de Nacimiento", "Estado Civil",
			u"Ocupación", "Lugar de Trabajo", u"Teléfono", u"Dirección"]
			self.Personas.setHeader(self.headers)
			self.Personas.addTable(self.manejador.consultarPersonas())

			self.txtBusqueda.textChanged.connect(self.Personas.on_lineEdit_textChanged)
			self.comboBusqueda.currentIndexChanged.connect(self.Personas.on_comboBox_currentIndexChanged)
			
			def modoBusquedaInsercion(self):
				pass

			def modoEliminacionActualizacion(self):
				pass
