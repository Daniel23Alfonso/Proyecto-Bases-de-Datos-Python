# -*- coding: utf-8 -*- 

import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *
from ManejadorBD import *

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
			tab_Nuevo=QWidget()
			tab_Editar=QWidget()
			#tab_CursoMateria=QWidget()
			tab_ProfesorMateria=QWidget()
			self.layoutNuevo=QVBoxLayout()
			self.layoutAgregar=QVBoxLayout()
			tab_Nuevo.setLayout(self.layoutNuevo)
			tab_widget.addTab(tab_Nuevo,"Curso")
			#tab_widget.addTab(tab_CursoMateria,"Agregar Materia")
			tab_widget.addTab(tab_ProfesorMateria,"Agregar Profesor a Materia")
			self.contenedorNuevo=QVBoxLayout()
			#botones
			self.btnCrear=QPushButton("Crear")
			self.btnActualizar=QPushButton("Actualizar")
			self.btnEliminar=QPushButton("Eliminar")
			#layaouts
			self.Cursos=MyTable(self)
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

			#agrego datos a la tabla
			self.manejador = ManejadorBD()
			self.HeadersCurso= [u"Código", u"Número", u"Año Lectivo", "Paralelo",
			u"Cédula Profesor"]
			self.Cursos.setHeader(self.HeadersCurso)
			self.Cursos.addTable(self.manejador.obtenerCursos())
			
			"""
			# agregar Materia Curso
			self.btnAgregar=QPushButton("<<")
			self.btnQuitar=QPushButton(">>")
			self.layoutAgregarMateria=QHBoxLayout()
			self.layoutAgregarMateria1=QVBoxLayout()
			self.layoutAgregarMateria2=QVBoxLayout()
			self.layoutAgregarMateria3=QVBoxLayout()
			self.MateriasCurso=MyTable(self)
			self.MateriasDisponible=MyTable(self)
			self.layoutAgregarMateria1.addWidget(QLabel("Materias Curso"))
			self.layoutAgregarMateria1.addWidget(self.MateriasCurso)
			self.layoutAgregarMateria2.addWidget(self.btnAgregar)
			self.layoutAgregarMateria2.addWidget(self.btnQuitar)
			self.layoutAgregarMateria3.addWidget(QLabel("Materias Disponible"))
			self.layoutAgregarMateria3.addWidget(self.MateriasDisponible)
			self.layoutAgregarMateria.addLayout(self.layoutAgregarMateria1)
			self.layoutAgregarMateria.addLayout(self.layoutAgregarMateria2)
			self.layoutAgregarMateria.addLayout(self.layoutAgregarMateria3)
			tab_CursoMateria.setLayout(self.layoutAgregarMateria)
			"""
			self.btnLigar=QPushButton("Ligar")
			self.btnDesLigar=QPushButton("DesLigar")
			self.layoutProfesorMateria=QHBoxLayout()
			self.MateriasSinProfesor=MyTable(self)
			self.MateriasProfesor=MyTable(self)
			self.Profesores=MyTable(self)
			self.layoutProfesorMateria1=QVBoxLayout()
			self.layoutProfesorMateria2=QVBoxLayout()
			self.layoutProfesorMateria3=QVBoxLayout()
			self.layoutProfesorMateria4=QVBoxLayout()
			self.layoutProfesorMateria1.addWidget(QLabel("Materias sin Profesor"))
			self.layoutProfesorMateria1.addWidget(self.MateriasSinProfesor)
			self.layoutProfesorMateria2.addWidget(QLabel("Profesores"))
			self.layoutProfesorMateria2.addWidget(self.Profesores)
			self.layoutProfesorMateria3.addWidget(self.btnLigar)
			self.layoutProfesorMateria3.addWidget(self.btnDesLigar)
			self.layoutProfesorMateria4.addWidget(QLabel("Materia Profesor"))
			self.layoutProfesorMateria4.addWidget(self.MateriasProfesor)
			self.layoutProfesorMateria.addLayout(self.layoutProfesorMateria1)
			self.layoutProfesorMateria.addLayout(self.layoutProfesorMateria2)
			self.layoutProfesorMateria.addLayout(self.layoutProfesorMateria3)
			self.layoutProfesorMateria.addLayout(self.layoutProfesorMateria4)
			tab_ProfesorMateria.setLayout(self.layoutProfesorMateria)