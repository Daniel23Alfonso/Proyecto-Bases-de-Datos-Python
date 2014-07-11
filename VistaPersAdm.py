# -*- coding: utf-8 -*- 

import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from VistasFacturacion import *
from VistaPersona import *
from VistaCurso import *
from VistasMateria import *

class VistaPersAdm(QMainWindow):
	dimension_x=1000
	dimension_y=600

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.main_widget = QWidget(self)
			self.contenedor= QVBoxLayout()
			
			#--Creacion de Pestañas---#
			tab_widget = QTabWidget()
			tab_est = QWidget()
			tab_est.setWindowIcon(QIcon("Imagenes/estudiante.jpg"))
			tab_pers = VistaPersona()
			tab_cursos = VistaCurso()
			tab_materias = VistasMateria()
			tab_facturacion = VistaFacturacion()
			
			#--definicion de contenedores de cada pestaña--#
			
			
			self.cont_est = QHBoxLayout(tab_est) #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.cont_pers = QHBoxLayout(tab_pers) 
			self.cont_Cursos = QHBoxLayout(tab_cursos)
			self.cont_materias = QHBoxLayout(tab_materias)
			self.cont_Facturacion = QHBoxLayout(tab_facturacion)
			
			#--agrego las pestañas al tab biew
			tab_widget.addTab(tab_facturacion,u"Facturación")
			tab_widget.addTab(tab_est,"Estudiantes")
			tab_widget.addTab(tab_pers,"Personas")
			tab_widget.addTab(tab_cursos,"Cursos")
			tab_widget.addTab(tab_materias,"Materias")
			
			
			
			self.setWindowTitle("Administrativo opciones")
			
			

							

			
			self.contenedor.addWidget(tab_widget)
			

			self.main_widget.setLayout(self.contenedor)
			self.setCentralWidget(self.main_widget)
			
			
			#---Menu---#	
			exitAction = QAction(QIcon('Imagenes/salir.jpg'), '&Salir', self)
			exitAction.setShortcut('Ctrl+Q')
			exitAction.setStatusTip('Exit application')
			exitAction.triggered.connect(qApp.quit)
			self.statusBar()
			menubar = self.menuBar()
			fileMenu = menubar.addMenu('&Archivo')
			fileMenu.addAction(exitAction)