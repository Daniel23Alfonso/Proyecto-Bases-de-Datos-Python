# -*- coding: utf-8 -*-
import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *
from ManejadorBD import *

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
			#Tabla cliente
			self.clientes=MyTable(self)
			#combobox Cliente
			self.tipoCliente=["Consumidor Final","Con Nombre"]
			self.comboBusquedaCliente=QComboBox() #tipos de usuario mostrados en un combo box
			self.comboBusquedaCliente.addItems(self.tipoCliente)
			#cajas de texto
			self.cliente=QLineEdit()
			self.estudiante=QLineEdit()
			#boton
			self.btnGenerar=QPushButton("Generar Factura")
			self.btnAgregar=QPushButton("Agregar")
			self.btnNuevo=QPushButton("Nuevo Cliente")
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
			self.layoutEstudiantes.addLayout(self.layoutEstudiantes1)
			self.layoutEstudiantes.addLayout(self.layoutEstudiantes2)
			self.layoutEstudiantes1.addWidget(QLabel("                               "))
			self.layoutEstudiantes1.addWidget(QLabel("Tipo Busqueda"))
			self.layoutEstudiantes1.addWidget(self.comboBusquedaAlumno)
			self.layoutEstudiantes1.addWidget(self.estudiante)
			self.layoutEstudiantes1.addWidget(QLabel("                               "))
			self.layoutEstudiantes2.addWidget(self.alumnos)
			self.layoutEstudiantes2.addWidget(self.btnAgregar)

			self.layoutCliente=QVBoxLayout()
			self.layoutCliente1=QHBoxLayout()
			self.layoutCliente1.addWidget(self.comboBusquedaCliente)
			self.layoutCliente1.addWidget(QLabel("Cedula:"))
			self.layoutCliente1.addWidget(self.cliente)
			self.layoutCliente1.addWidget(self.btnNuevo)
			self.layoutCliente1.addWidget(QLabel("                               "))
			self.layoutCliente.addLayout(self.layoutCliente1)
			self.layoutCliente.addWidget(self.clientes)

			self.layoutFactura=QVBoxLayout()
			self.layoutFactura1=QHBoxLayout()
			self.layoutFactura2=QHBoxLayout()
			self.layoutFactura.addLayout(self.layoutFactura1)
			self.layoutFactura.addLayout(self.layoutFactura2)
			self.layoutFactura2.addWidget(self.factura)
			self.layoutFactura2.addWidget(self.GBoxValores)
			self.layoutFactura2.addWidget(self.btnGenerar)
			self.layoutFactura1.addWidget(self.lblNumeroFactura)
			



			self.contenedor.addLayout(self.layoutCliente)
			self.contenedor.addLayout(self.layoutEstudiantes)
			self.contenedor.addLayout(self.layoutFactura)

			self.headerEstudainte = [u"Matrícula",u"cédula", "Nombres", "Apellidos"]
			self.manejadorBD = ManejadorBD() 
			#agrego la tabla de alumnos
			self.alumnos.setHeader(self.headerEstudainte)
			self.alumnos.addTable(self.manejadorBD.consultarEstudiante2())
			self.estudiante.textChanged.connect(self.alumnos.on_lineEdit_textChanged)
			self.comboBusquedaAlumno.currentIndexChanged.connect(self.alumnos.on_comboBox_currentIndexChanged)
			
			#lagrego los datos a la tabla
			self.headerCliente= [u"Cédula", "Nombres", "Apellidos", "Sexo", "Fecha de Nacimiento", "Estado Civil",
			u"Ocupación", "Lugar de Trabajo", u"Teléfono", u"Dirección"]
			self.clientes.setHeader(self.headerCliente)
			self.clientes.addTable(self.manejadorBD.consultarPersonas())
			self.cliente.textChanged.connect(self.clientes.on_lineEdit_textChanged)
		


#app = QApplication(sys.argv)
#vista1 = VistaFacturacion()
#vista1.show()
#app.exec_()