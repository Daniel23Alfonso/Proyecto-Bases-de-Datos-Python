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
			self.lEstadoCivil=["Soltero","Casado","Divorsiado","Union Libre","Viudo"]
			self.estadoCivil.addItems(self.lEstadoCivil)
			self.ocupacion=QLineEdit()
			self.lugarTrabajo=QLineEdit()
			self.telefono=QLineEdit()
			self.direccion=QLineEdit()
			self.calendarioFecha=QCalendarWidget()
			#botones
			self.btnGuardar=QPushButton("Guardar")
			self.btnGuardar.setIcon(QIcon("Imagenes/guardar.jpg"))
			self.btnCancelar=QPushButton("Cancelar")
			self.btnSeleccionar=QPushButton("Seleccionar")
			#definicion objetos busqueda
			self.comboBusqueda=QComboBox()
			self.txtBusqueda=QLineEdit()
			self.comboBusqueda.addItems([u"cédula","Nombres","Apellidos"])

			# llenamos el layout de los botones
			self.layoutBotones.addWidget(self.btnGuardar)
			self.layoutBotones.addWidget(self.btnCancelar)

			#creacion de formulario
			self.layoutPersona.addRow("cedula: ",self.cedula)
			self.cedula.setEnabled(False)
			self.layoutPersona.addRow("Nombre: ",self.nombre)
			self.layoutPersona.addRow("Apellido: ",self.apellido)
			self.layoutPersona.addRow("sexo: ",self.sexo)
			self.layoutPersona.addRow("Fecha Nacimiento",self.calendarioFecha)
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
			self.contenedor.addWidget(self.btnSeleccionar)
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
			self.modoSeleccion()
			self.connect(self.btnSeleccionar,SIGNAL("clicked()"),self.clik_Seleccionar)
			self.connect(self.btnGuardar,SIGNAL("clicked()"),self.clik_Guardar)
			self.connect(self.btnCancelar,SIGNAL("clicked()"),self.clik_Cancelar)
			self.P=[]
			
	def seleccionarPersona(self):
		self.P=self.Personas.getSelectedRegister()


	def modoSeleccion(self):
		self.btnCancelar.setEnabled(False)
		self.btnGuardar.setEnabled(False)
		self.btnSeleccionar.setEnabled(True)



	def modoEdicion(self):
		self.btnCancelar.setEnabled(True)
		self.btnGuardar.setEnabled(True)
		self.btnSeleccionar.setEnabled(False)

	def clik_Seleccionar(self):
		self.seleccionarPersona()
		if(len(self.P)!=0):
			persona=self.P[len(self.P)-1]
			self.llenarPersona(persona)
			self.P=[]
			self.modoEdicion()
		else:
			QMessageBox.about(self,'Error!',u'Seleccione una Persona')
			

	def llenarPersona(self,l):
		self.cedula.setText(l[0])
		self.nombre.setText(l[1])
		self.apellido.setText(l[2])
		if(l[3]=="Masculino"):
			self.sexo.setCurrentIndex(0)
		else:
			self.sexo.setCurrentIndex(1)
		# se necesita un QDate
		#self.calendarioFecha.setSelectedDate (l[4])
		if(l[5]==self.lEstadoCivil[0]):
			self.estadoCivil.setCurrentIndex(0)
		elif(l[5]==self.lEstadoCivil[1]):
			self.estadoCivil.setCurrentIndex(1)
		elif(l[5]==self.lEstadoCivil[2]):
			self.estadoCivil.setCurrentIndex(2)
		elif(l[5]==self.lEstadoCivil[3]):
			self.estadoCivil.setCurrentIndex(3)
		elif(l[5]==self.lEstadoCivil[4]):
			self.estadoCivil.setCurrentIndex(4)
		self.ocupacion.setText(l[6])
		self.lugarTrabajo.setText(l[7])
		self.telefono.setText(l[8])
		self.direccion.setText(l[9])

	def limpiar(self):
		self.cedula.setText("")
		self.nombre.setText("")
		self.apellido.setText("")
		self.sexo.setCurrentIndex(0)
		self.estadoCivil.setCurrentIndex(0)
		self.ocupacion.setText("")
		self.lugarTrabajo.setText("")
		self.telefono.setText("")
		self.direccion.setText("")

	def clik_Cancelar(self):
		self.modoSeleccion()
		self.limpiar()

	def clik_Guardar(self):
		self.fecha=self.calendarioFecha.selectedDate()
		datos=(self.cedula.displayText(),self.nombre.displayText(),self.apellido.displayText(),self.sexo.currentText(),self.fecha,
					self.estadoCivil.currentText(),self.ocupacion.displayText(),self.lugarTrabajo.displayText(),self.telefono.displayText(),
					self.direccion.displayText())
		self.modoSeleccion()
		self.limpiar()
		try:
			self.manejador.actualizarPersona(datos)
			QMessageBox.about(self,'Informacion!',u'Se ha actualizado correctamente la persona')
			self.Actualizar_Personas()
		except:
			QMessageBox.about(self,'Error!',u'No se ha podido actualizar a la Persona')

	def Actualizar_Personas(self):
		self.Personas.deleteData()
		self.Personas.addTable(self.manejador.consultarPersonas())
