# -*- coding: utf-8 -*- 


import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class VistaIngresoSist(QWidget):
	dimension_x=500
	dimension_y=600

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.contenedor = QHBoxLayout()
			self.form_layout = QFormLayout()
			self.setLayout(self.contenedor)
			self.setWindowTitle("Ingreso al Sistema")
			self.tipoUsuario=["Profesor","Personal Administrativo"]
			
			s = u"Contrase\xf1a:"
			self.usuario = QLineEdit()
			self.contrasenia = QLineEdit()  
			self.contrasenia.setEchoMode(QLineEdit.Password)
			self.botonIngresar = QPushButton("Ingresar")
			self.Tusuarios =QComboBox()
			self.Tusuarios.addItems(self.tipoUsuario)
			
			for i in range(4):
				self.form_layout.addRow(QLabel(""))				

			self.form_layout.addRow('Tipo de Usuario:', self.Tusuarios)
			self.form_layout.addRow('Usuario:', self.usuario)
			self.form_layout.addRow(s, self.contrasenia)
			self.hbox = QHBoxLayout()
			self.hbox.addWidget(QLabel("           "))
			self.hbox.addWidget(self.botonIngresar)
			self.hbox.addWidget(QLabel("           "))
			hvbox= QVBoxLayout()
			hvbox.addWidget(QLabel("                      "))
			self.contenedor.addLayout(hvbox)
			self.contenedor.addLayout(self.form_layout)
			self.contenedor.addLayout(hvbox)
			self.form_layout.addRow(self.hbox)
			self.setLayout(self.contenedor)

			


			
			



app = QApplication(sys.argv)
vista1 = VistaIngresoSist()
vista1.show()
app.exec_()