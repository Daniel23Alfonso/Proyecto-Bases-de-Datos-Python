import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *

class VistaFacturacion(QWidget):
	dimension_x=400
	dimension_y=500

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.setLayout(self.contenedor)
			#combobox tipo busqueda
			self.tipoBusqueda=["Cedula","Apellido","Nombre"]
			self.comboBusquedaAlumno=QComboBox() #tipos de usuario mostrados en un combo box
			self.comboBusquedaAlumno.addItems(self.tipoBusqueda)
			#Tabla alumnos
			self.alumnos=MyTable()
			#Tabla factura
			self.factura=MyTable()
			#Tabla cliente
			self.clientes=MyTable()
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
			self.layoutFactura2.addWidget(self.btnGenerar)
			self.layoutFactura1.addWidget(self.lblNumeroFactura)
			



			self.contenedor.addLayout(self.layoutCliente)
			self.contenedor.addLayout(self.layoutEstudiantes)
			self.contenedor.addLayout(self.layoutFactura)

			
		


#app = QApplication(sys.argv)
#vista1 = VistaFacturacion()
#vista1.show()
#app.exec_()