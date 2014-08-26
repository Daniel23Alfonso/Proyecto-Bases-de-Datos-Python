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
			self.tab_widget = QTabWidget()
			tab_Nuevo=QWidget()
			self.tab_ElegirDirigente=QWidget()
			self.tab_ProfesorMateria=QWidget()

			self.layoutNuevo=QVBoxLayout()
			self.layoutAgregar=QVBoxLayout()
			tab_Nuevo.setLayout(self.layoutNuevo)
			self.tab_widget.addTab(tab_Nuevo,"Curso")
			self.tab_widget.addTab(self.tab_ProfesorMateria,"Asignar Profesor a Materias")
			self.tab_widget.addTab(self.tab_ElegirDirigente,"Asignar Dirigente a Curso")
			self.contenedorNuevo=QVBoxLayout()
			#botones
			self.btnCrear=QPushButton("Crear")
			self.connect(self.btnCrear,SIGNAL("clicked()"),self.accionCrear)
			self.btnActualizar=QPushButton("Guardar")
			self.connect(self.btnActualizar,SIGNAL("clicked()"),self.accionGuardar)
			self.btnCancelar=QPushButton("Cancelar")
			self.connect(self.btnCancelar,SIGNAL("clicked()"),self.accionCancelar)
			#layaouts
			self.Cursos=MyTable(self)
			self.contenedor.addWidget(QLabel("Cursos"))
			self.contenedor.addWidget(self.Cursos)

			self.botonCurso=QPushButton("Mostrar Informacion del Curso")
			self.connect(self.botonCurso,SIGNAL("clicked()"),self.obtenerInfoCurso)
			self.contenedor.addWidget(self.botonCurso)
			
			self.contenedor.addWidget(self.tab_widget)
			
			self.layoutCurso1=QFormLayout()
			self.layoutCurso2=QHBoxLayout()
			self.layoutNuevo.addLayout(self.layoutCurso1)
			self.layoutNuevo.addLayout(self.layoutCurso2)

			#definicion cajas de texto
			self.aLectivo=QLineEdit()
			self.curso=QComboBox()
			self.paralelo=QLineEdit()
			self.listaCurso=["Kinder","Primero","Segundo","Tercero","Cuarto","Quinto","Sexto","Septimo"]
			self.curso.addItems(self.listaCurso)
			#creacion de formulario
			self.layoutCurso1.addRow("Ano Lectivo: ",self.aLectivo)
			self.layoutCurso1.addRow("curso: ",self.curso)
			self.layoutCurso1.addRow("Paralelo: ",self.paralelo)
			self.layoutCurso2.addWidget(self.btnCrear)
			self.layoutCurso2.addWidget(self.btnActualizar)
			self.layoutCurso2.addWidget(self.btnCancelar)

			#agrego datos a la tabla
			self.manejador = ManejadorBD()
			self.HeadersCurso= [u"Código", u"Número", u"Año Lectivo", "Paralelo",u"Cédula Dirigente"]
			self.Cursos.setHeader(self.HeadersCurso)
			self.Cursos.addTable(self.manejador.obtenerCursos())
			self.Cursos.setEditable(False)

			self.btnLigar=QPushButton("Ligar")
			self.connect(self.btnLigar,SIGNAL("clicked()"),self.ligar)
			self.btnDesLigar=QPushButton("DesLigar")
			self.connect(self.btnDesLigar,SIGNAL("clicked()"),self.desligar)
			self.layoutProfesorMateria=QHBoxLayout()
			self.materiasConProfesor=[]#almacenara las tuplas Materia,Profesor que se debera cargar en la base de datos


			self.layoutProfesorMateria1=QVBoxLayout()
			self.layoutProfesorMateria2=QVBoxLayout()
			self.layoutProfesorMateria3=QVBoxLayout()
			self.layoutProfesorMateria4=QVBoxLayout()

			self.MateriasSinProfesor=MyTable(self.tab_widget)
			self.MateriasSinProfesor.setHeader(["Codigo","Nombre"])
			self.MateriasProfesor=MyTable(self.tab_widget)
			self.MateriasProfesor.setHeader(["","Materia Asignada","","Nombres del Profesor","Apellidos del Profesor"])
			self.MateriasProfesor.hideColumn(0)
			self.MateriasProfesor.hideColumn(2)

			self.Profesores=MyTable(self.tab_widget)
			self.Profesores.setHeader([u"Cédula","Nombre","Apellido"])
			self.Profesores.addTable(self.manejador.consultarProfesores())	
			self.Profesores.setEditable(False)		

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
			self.tab_ProfesorMateria.setLayout(self.layoutProfesorMateria)
			self.modoConsulta()
			self.paralelo.setEnabled(False)
			self.layoutDirigente=QHBoxLayout()
			self.ProfesoresDirigentes=MyTable(self.tab_widget)
			self.ProfesoresDirigentes.setHeader([u"Cédula","Nombre","Apellido"])
			self.ProfesoresDirigentes.addTable(self.manejador.consultarProfesores())
			self.btnAsignarDirigente=QPushButton("Asignar Dirigente")
			self.layoutDirigente.addWidget(self.ProfesoresDirigentes)
			self.layoutDirigente.addWidget(self.btnAsignarDirigente)
			self.tab_ElegirDirigente.setLayout(self.layoutDirigente)
			self.connect(self.btnAsignarDirigente,SIGNAL("clicked()"),self.ligarDirigente)

			
	def obtenerInfoCurso(self):
		self.modoConsulta()
		self.idCurso=0
		cursos=self.Cursos.getSelectedRegister()
		if len(cursos)>0:
			cursoSeleccionado=cursos[len(cursos)-1]#el primer registro seleccionado
			self.idCurso=cursoSeleccionado[0]#el primer atributo es el id, almacena la referencia del idCurso actual
			self.obtenerMateriasSinProfesor(self.idCurso)
			self.actualizarMateriasProfesor(self.idCurso)
			#llenamos la consulta
			self.aLectivo.setText(cursoSeleccionado[2])
			i=self.listaCurso.index(cursoSeleccionado[1])
			self.curso.setCurrentIndex(i)
			self.paralelo.setText(cursoSeleccionado[3])

	def obtenerMateriasSinProfesor(self,idCurso):#actualiza el grid con la informacion de las materias sin profesor
		materiasDelCurso=self.manejador.obtenerMateriasPorCurso(idCurso)#obtiene las materias sin profesor del curso
		self.MateriasSinProfesor.row=0
		self.MateriasSinProfesor.deleteData()
		self.MateriasSinProfesor.addTable(materiasDelCurso)#agrega las materias sin profesor
		self.MateriasSinProfesor.hideColumn(0)
		self.MateriasSinProfesor.setEditable(False)

	def actualizarMateriasProfesor(self,idCurso):#actualiza el grid con la informacion de las materias y sus profesores asignados
		resultados=self.manejador.obtenerMateriaCursoProfesor(idCurso)
		self.MateriasProfesor.deleteData()#Si existe informacion dentro del grid la borra para cargar nueva informacion
		self.MateriasProfesor.addTable(resultados)
		self.MateriasProfesor.setEditable(False)
		self.MateriasProfesor.hideColumn(0)
		self.MateriasProfesor.hideColumn(2)

	def ligar(self):
		try:
			#obtiene la materia seleccionada
			materiasSeleccionadas=self.MateriasSinProfesor.getSelectedRegister()
			if len(materiasSeleccionadas)>0:
				materia=materiasSeleccionadas[0]#el primer registro seleccionado
				idMateria=materia[0]
			#obtiene el profesor seleccionado
			profesoresSeleccionados=self.Profesores.getSelectedRegister()#el primer registro seleccionado		
			if len(profesoresSeleccionados)>0:
				profesor=profesoresSeleccionados[0]
				idProfesor=profesor[0]

			#agrega la informacion a la base de datos
			self.manejador.agregarProfesorAMateriaDeCurso(self.idCurso,idMateria,idProfesor)
			#actualizar la informacion de la gui
			self.actualizarMateriasProfesor(self.idCurso)
			self.obtenerMateriasSinProfesor(self.idCurso)
			QMessageBox.about(self,u'Actualización','Se ha asignado esta materia al profesor correctamente')
		except:
			QMessageBox.about(self,'Error!',u'No se ha podido registrar esta materia al profesor')


	def desligar(self):
		try:
			lista=self.MateriasProfesor.getSelectedRegister()
			if len(lista)>0:
				fila=lista[0]
				#obtengo la informacion de la tupla que fue seleccioanda 
				idMateriaSeleccionada=str(fila[0])
				cedulaProfesorSeleccionado=str(fila[2])
				#actualizar la base
				self.manejador.quitarProfesorDeMateria(self.idCurso,idMateriaSeleccionada,cedulaProfesorSeleccionado)
				#actualizar las materias sin profesor
				self.actualizarMateriasProfesor(self.idCurso)
				self.obtenerMateriasSinProfesor(self.idCurso)
				QMessageBox.about(self,u'Actualización','Se ha desvinculado al profesor de esta materia')
		except:
			QMessageBox.about(self,'Error!',u'No se ha podido desvincular al profesor de esta materia')



	def actualizarMaterias(self):
		filasSeleccionadas=self.MateriasSinProfesor.getIndexSelected()#obtiene curso seleccionado
		registro=filasSeleccionadas[0]
		indice=registro.row()#obtiene el indice del registro dentro del grid
		self.MateriasSinProfesor.deleteRow(indice)#borra la fila de la materia a la cual ya se le asigno un profesor
		self.MateriasSinProfesor.setEditable(False)

	def modoCrear(self):
		self.btnCrear.setEnabled(False)
		self.btnActualizar.setEnabled(True)
		self.btnCancelar.setEnabled(True)
		self.aLectivo.setEnabled(True)
		self.curso.setEnabled(True)
		self.paralelo.setEnabled(False)


	def modoConsulta(self):
		self.aLectivo.setText("")
		self.paralelo.setText("")
		self.btnCrear.setEnabled(True)
		self.btnActualizar.setEnabled(False)
		self.btnCancelar.setEnabled(False)
		self.aLectivo.setEnabled(False)
		self.curso.setEnabled(False)
		self.paralelo.setEnabled(False)

	def accionCrear(self):
		self.aLectivo.setText("")
		self.paralelo.setText("")
		self.modoCrear()

	def accionGuardar(self):
		datos=(self.curso.currentIndex()+1,self.aLectivo.displayText())
		try:
			if(self.validarAnoLectivo(self.aLectivo.displayText())):
				self.manejador.crearCurso(datos)
				QMessageBox.about(self,'Aviso!',u'Se ha creado el Curso Correctamente')
				self.modoConsulta()
				self.actualizarCursos()
			else:
				QMessageBox.about(self,'Error!',u'Año lectivo invalido')	
		except:
			QMessageBox.about(self,'Error!',u'No se ha podido Crear el Curso')

	def accionCancelar(self):
		self.aLectivo.setText("")
		self.paralelo.setText("")
		self.modoConsulta()

	def actualizarCursos(self):
		self.Cursos.deleteData()
		self.Cursos.addTable(self.manejador.obtenerCursos())


	def validarAnoLectivo(self,a):
		 anos= a.split('-')
		 if(len(anos)!=2):
		 	return False
		 else:
		 	try:
		 		ano1=int(anos[0])
		 		ano2=int(anos[1])
		 		if((ano2-ano1)==1):
		 			return True
		 		else:
		 			return False
		 	except Exception, e:
		 		return False


	def ligarDirigente(self):
		cursoSel=self.Cursos.getSelectedRegister()
		ProfSel=self.ProfesoresDirigentes.getSelectedRegister()
		if(len(cursoSel)>0 and len(ProfSel)>0):
			curso=cursoSel[len(cursoSel)-1]
			prof=ProfSel[len(ProfSel)-1]
			idCurso=curso[0]
			idProfesor=prof[0]
			datos=(idProfesor,idCurso)
			try:
				self.manejador.AsignarDirigente(datos)	
				self.actualizarCursos()		
			except Exception, e:
				QMessageBox.about(self,'Error!',u'No se puede Asignar el Dirigente al Curso')			
		else:
			QMessageBox.about(self,'Error!',u'No se ha escogido el profesor y el curso')
