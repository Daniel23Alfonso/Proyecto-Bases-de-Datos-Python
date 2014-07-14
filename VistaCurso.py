import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *

class VistaCurso(QWidget):
	dimension_x=400
	dimension_y=500

	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.setLayout(self.contenedor)
			#creamos las opciones
			tab_widget = QTabWidget()
			tab_Nuevo=QTabWidget()
			tab_Editar=QWidget()
			tab_CursoMateria=QWidget()
			self.layoutNuevo=QVBoxLayout()
			self.layoutAgregar=QVBoxLayout()
			tab_Nuevo.setLayout(self.layoutNuevo)
			tab_widget.addTab(tab_Nuevo,"Curso")
			tab_widget.addTab(tab_CursoMateria,"Agregar Materia")
			self.contenedorNuevo=QVBoxLayout()
			#botones
			self.btnCrear=QPushButton("Crear")
			self.btnActualizar=QPushButton("Actualizar")
			self.btnEliminar=QPushButton("Eliminar")

			self.Cursos=MyTable()
			self.contenedor.addWidget(QLabel("Cursos"))
			self.contenedor.addWidget(self.Cursos)
			self.contenedor.addWidget(tab_widget)
			self.layoutCurso1=QFormLayout()
			self.layoutCurso2=QHBoxLayout()
			self.layoutNuevo.addLayout(self.layoutCurso1)
			self.layoutNuevo.addLayout(self.layoutCurso2)
			#definicion cajas de texto
			self.aLectivo=QLineEdit()
			self.curso=QComboBox()
			self.paralelo=QComboBox()
			self.curso.addItems(["Kinder","Primero","Segundo","Tercero","Cuarto","Quinto","Sexto","Septimo"])
			#creacion de formulario
			self.layoutCurso1.addRow("Ano Lectivo: ",self.aLectivo)
			self.layoutCurso1.addRow("curso: ",self.curso)
			self.layoutCurso1.addRow("Paralelo: ",self.paralelo)
			self.layoutCurso2.addWidget(self.btnCrear)
			self.layoutCurso2.addWidget(self.btnActualizar)
			self.layoutCurso2.addWidget(self.btnEliminar)



