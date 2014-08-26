# -*- coding: utf-8 -*-
import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *
from ManejadorBD import *
import os
from GeneradorReporte import *

class VistaFacturacion(QWidget):
	dimension_x=400
	dimension_y=500

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.setLayout(self.contenedor)
			#combobox tipo busqueda
			self.tipoBusqueda=["Matricula","Cedula","Nombre","Apellido"]
			self.comboBusquedaAlumno=QComboBox() #tipos de usuario mostrados en un combo box
			self.comboBusquedaAlumno.addItems(self.tipoBusqueda)
			#Tabla alumnos
			self.alumnos=MyTable(self)
			#Tabla factura
			self.factura=MyTable(self)
			#cajas de texto
			self.estudiante=QLineEdit()
			#boton
			self.btnGenerar=QPushButton("Generar Factura")
			self.btnSeleccionar=QPushButton("Seleccionar")
			self.btnCancelar=QPushButton("Cancelar")
			self.btnAgregar=QPushButton("Agregar Mes")
			#etiquetas
			self.lblNumeroFactura=QLabel("Factura:     ")
			#valores de la factura
			self.lblSubTotal=QLabel("SubTota = $ 0.00   ")
			self.lblIva=QLabel("IVA 12% = $ 0.00   ")
			self.lblTotal=QLabel("Total = $ 0.00   ")
			self.GBoxValores = QGroupBox ( "valores" )
			vGBoxValores = QVBoxLayout()
			self.GBoxValores.setLayout(vGBoxValores)
			vGBoxValores.addWidget(self.lblSubTotal)
			vGBoxValores.addWidget(self.lblIva)
			vGBoxValores.addWidget(self.lblTotal)
			#contruccion ventana
			
			self.layoutEstudiantes=QVBoxLayout()
			self.layoutEstudiantes1=QHBoxLayout()
			self.layoutEstudiantes2=QHBoxLayout()
			self.layoutEstudiantes21=QVBoxLayout()
			self.layoutEstudiantes.addLayout(self.layoutEstudiantes1)
			self.layoutEstudiantes.addLayout(self.layoutEstudiantes2)
			self.layoutEstudiantes1.addWidget(QLabel("                               "))
			self.layoutEstudiantes1.addWidget(QLabel("Tipo Busqueda"))
			self.layoutEstudiantes1.addWidget(self.comboBusquedaAlumno)
			self.layoutEstudiantes1.addWidget(self.estudiante)
			self.layoutEstudiantes1.addWidget(QLabel("                               "))
			self.layoutEstudiantes2.addWidget(self.alumnos)
			self.layoutEstudiantes2.addLayout(self.layoutEstudiantes21)
			self.layoutEstudiantes21.addWidget(self.btnSeleccionar)
			self.layoutEstudiantes21.addWidget(self.btnAgregar)
			self.layoutEstudiantes21.addWidget(self.btnCancelar)

	
			self.layoutFactura=QVBoxLayout()
			self.layoutFactura1=QHBoxLayout()
			self.layoutFactura2=QHBoxLayout()
			self.layoutFactura.addLayout(self.layoutFactura1)
			self.layoutFactura.addLayout(self.layoutFactura2)
			self.layoutFactura2.addWidget(self.factura)
			self.layoutFactura2.addWidget(self.GBoxValores)
			self.layoutFactura2.addWidget(self.btnGenerar)
			self.layoutFactura1.addWidget(self.lblNumeroFactura)
			

			self.contenedor.addLayout(self.layoutEstudiantes)
			self.contenedor.addLayout(self.layoutFactura)

			self.headerEstudainte = [u"Matrícula",u"cédula", "Nombres", "Apellidos"]
			self.manejadorBD = ManejadorBD() 
			#agrego la tabla de alumnos
			self.alumnos.setHeader(self.headerEstudainte)
			self.alumnos.addTable(self.manejadorBD.consultarEstudiante2())
			self.estudiante.textChanged.connect(self.alumnos.on_lineEdit_textChanged)
			self.comboBusquedaAlumno.currentIndexChanged.connect(self.alumnos.on_comboBox_currentIndexChanged)
			self.headerFactura=["Cantidad","Descripcion","P. Unitario","V. Total"]
			self.factura.setHeader(self.headerFactura)
			self.connect(self.btnSeleccionar,SIGNAL("clicked()"),self.AccionSeleccionar)
			self.connect(self.btnAgregar,SIGNAL("clicked()"),self.agregarElemntoFactura)
			self.connect(self.btnCancelar,SIGNAL("clicked()"),self.AccionCancelar)
			self.connect(self.btnGenerar,SIGNAL("clicked()"),self.genrarFactura)
			self.modoSeleccion()
			self.deudas=[]
			self.idDeudas=[]
			self.total=0.0
			self.subTotal=0.0
			self.iva=0.0
			self.gReporte=GeneradorReporte()

	def modoSeleccion(self):
		self.btnSeleccionar.setEnabled(True)
		self.btnCancelar.setEnabled(False)
		self.btnAgregar.setEnabled(False)

	def modoAgregar(self):
		self.btnSeleccionar.setEnabled(False)
		self.btnCancelar.setEnabled(True)
		self.btnAgregar.setEnabled(True)

	def AccionSeleccionar(self):
		alumnos=self.alumnos.getSelectedRegister()
		if(len(alumnos)>0):
			alumno=alumnos[len(alumnos)-1]
			idAlumno=alumno[0]
			self.modoAgregar()
			try:
				self.deudas=self.manejadorBD.obtenerDeudas(idAlumno)
				self.idDeudas=[]
			except Exception, e:
				raise e
		else:
			QMessageBox.about(self,'Error!',u'No ah seleccionado alumno')

	def AccionCancelar(self):
		self.factura.deleteData()
		self.modoSeleccion()

	
	def agregarElemntoFactura(self):
		if(len(self.deudas)>0):
			deuda=self.deudas[0]
			self.deudas=self.deudas[1:]
			datoFactura=["1",deuda[1],deuda[2],deuda[2]]
			self.idDeudas.append(deuda[0])
			self.factura.addRow(datoFactura)
			self.subTotal=self.subTotal+float(deuda[2])
			self.total=self.total+float(deuda[2])
			self.actualizarValores()
		else:
			QMessageBox.about(self,'Aviso!',u'No hay mas deudas Disponibles')

	def genrarFactura(self):
		try:
			self.manejadorBD.generarFactura(self.idDeudas)
			QMessageBox.about(self,'Aviso!',u'Se genero Correctamente la Factura')
			self.factura.deleteData()
			self.subTotal=0.00
			self.total=0.00
			self.actualizarValores()
			self.modoSeleccion()
		except Exception, e:
			QMessageBox.about(self,'Error!',u'Problemas al generar la factura')			
	
	def actualizarValores(self):
		strSubt="SubTota = $ %.2f" %self.subTotal 
		strTotal="Total = $ %.2f   " %self.total
		self.lblSubTotal.setText(strSubt)
		self.lblIva.setText("IVA 12% = $ 0.00   ")
		self.lblTotal.setText(strTotal)
