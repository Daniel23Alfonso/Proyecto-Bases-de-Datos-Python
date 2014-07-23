# -*- coding: utf-8 -*- 
import sys
import time
import threading
from VistaProfesor import *
from VistaPersAdm import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import * 



class VistaIngresoSist(QWidget):
	dimension_x=500
	dimension_y=600

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.contenedor = QHBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.form_layout = QFormLayout() #layout interno
			self.setLayout(self.contenedor)
			self.setWindowTitle("Ingreso al Sistema")
			self.tipoUsuario=["Profesor","Personal Administrativo"] #lista para escoger el tipo de usuario
			
			s = u"Contrase\xf1a:" #string usado para escribir "contraseña"
			self.usuario = QLineEdit() #textEdit 
			self.contrasenia = QLineEdit()  
			self.contrasenia.setEchoMode(QLineEdit.Password)
			self.botonIngresar = QPushButton("Ingresar")
			
			self.Tusuarios =QComboBox() #tipos de usuario mostrados en un combo box
			self.Tusuarios.addItems(self.tipoUsuario)
			
			for i in range(4):
				self.form_layout.addRow(QLabel("")) #estoy agregando filas vacias 				

			self.form_layout.addRow('Tipo de Usuario:', self.Tusuarios) #agrego el combo box
			self.form_layout.addRow('Usuario:', self.usuario)
			self.form_layout.addRow(s, self.contrasenia)

			self.hbox = QHBoxLayout() #layout que coloca los widgets en forma horizontal
			self.hbox.addWidget(QLabel("           ")) #agego un espacio en el lado izquierdo 
			self.hbox.addWidget(self.botonIngresar)

			self.hbox.addWidget(QLabel("           "))
			
			self.vistaUsuario()

			self.contenedor.addWidget(QLabel("                      ")) #agrego ese espacio al layout principal
			self.contenedor.addLayout(self.form_layout)
			self.contenedor.addWidget(QLabel("                      ")) #agrego ese espacio al layout principal
			self.form_layout.addRow(self.hbox)
			
	def vistaUsuario(self):
		self.connect(self.botonIngresar,SIGNAL("clicked()"),self.vista)

	def vista(self):
		if(self.Tusuarios.currentIndex()==0):
			self.vistaProfesor()
		else:
			self.vistaAdmin()

	def vistaProfesor(self):
		nombre=self.usuario.displayText()
		self.ventana_profesor=VistaProfesor(nombre)
		self.close()
		self.ventana_profesor.show()

	def vistaAdmin(self):
		self.ventana_administrador=VistaPersAdm()
		self.close()
		self.ventana_administrador.show()



app = QApplication(sys.argv)
vista1 = VistaIngresoSist()
vista1.show()
app.exec_()