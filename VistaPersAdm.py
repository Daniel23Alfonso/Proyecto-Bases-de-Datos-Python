# -*- coding: utf-8 -*- 


import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class VistaPersAdm(QMainWindow):
	dimension_x=1000
	dimension_y=600

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.main_widget = QWidget(self)
			 

			self.contenedor = QHBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.form_layout = QFormLayout() #layout interno Izquierdo
			
			self.setLayout(self.contenedor)
			self.setWindowTitle("Administrativo opciones")
			
			self.btEstudiantes= QPushButton("Estudiantes")
			self.btEstudiantes.setIcon(QIcon("Imagenes/estudiante.jpg"))
			self.btPersonas= QPushButton("Personas")
			self.btPersonas.setIcon(QIcon("Imagenes/persona.jpg"))
			self.btCursos= QPushButton("Cursos")
			self.btCursos.setIcon(QIcon("Imagenes/curso.jpg"))
			self.btMaterias= QPushButton("Materias")
			self.btMaterias.setIcon(QIcon("Imagenes/materia.jpg"))
			self.btFacturacion = QPushButton(u"Facturación")
			self.btFacturacion.setIcon(QIcon("Imagenes/factura.jpg"))

			
			for i in range(3):
				self.form_layout.addRow(QLabel("")) #estoy agregando filas vacias 				

			self.form_layout.addRow(self.btEstudiantes) #agrego botones
			self.form_layout.addRow(self.btPersonas)
			self.form_layout.addRow(self.btCursos)
			self.form_layout.addRow(self.btMaterias)
			self.form_layout.addRow(self.btFacturacion)


			hvbox= QVBoxLayout() #layout con disposicion vertical
			hvbox.addWidget(QLabel("               ")) #agrego un espacio
			
			self.contenedor.addLayout(hvbox)
			self.contenedor.addLayout(self.form_layout)
			self.contenedor.addLayout(hvbox)
			

			
			self.setCentralWidget(self.main_widget)
			self.main_widget.setLayout(self.contenedor)

			exitAction = QAction(QIcon('Imagenes/salir.jpg'), '&Salir', self)
			exitAction.setShortcut('Ctrl+Q')
			exitAction.setStatusTip('Exit application')
			exitAction.triggered.connect(qApp.quit)
			self.statusBar()
			menubar = self.menuBar()
			fileMenu = menubar.addMenu('&Archivo')
			fileMenu.addAction(exitAction)







			
			



app = QApplication(sys.argv)
vista1 = VistaPersAdm()
vista1.show()
app.exec_()