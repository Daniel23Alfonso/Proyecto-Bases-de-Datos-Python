# -*- coding: utf-8 -*- 

import sys
import time
import threading
from VistaProfesor import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Tabla import *
from ManejadorBD import *

class VistaEstudiantes(QWidget):
	dimension_x=400
	dimension_y=500
	
	def __init__(self,*args):
			QWidget.__init__(self,*args)
			self.setGeometry(100,50,self.dimension_x,self.dimension_y)
			self.contenedor = QVBoxLayout() #layout principal de esta gui, los widgets se agregan de forma vertical
			self.setLayout(self.contenedor)


			#elementos de la tabla
			self.headersTabla = [u"Matrícula",u"Número de cédula", "Nombres", "Apellidos","Sexo", 
			"Estado Civil","Origen", "Etnia", "Fecha de Nacimiento"]
			self.manejadorBD = ManejadorBD() #manejador de la base de datos

			#componentes que iran en la ventana
			self.tipoBusqueda=[u"Matrícula",u"Cédula","Nombres","Apellidos"] #items del combo box
			self.paramBusqueda = QLineEdit() #entrada de texto usada para ingresar el parametro de busqueda seccion Consultas
			self.comboBusquedaEstudiante=QComboBox() #tipos de usuario mostrados en un combo box
			self.comboBusquedaEstudiante.addItems(self.tipoBusqueda)
			self.botonSeleccionar = QPushButton("Seleccionar") 


			#elementos de la pestaña de edicion
			self.btnEditar = QPushButton("Editar")
			self.btnEditar.setIcon(QIcon("Imagenes/editar.jpg"))
			self.connect(self.btnEditar,SIGNAL("clicked()"),self.activarEdicion)
			self.btnGuardar = QPushButton("Guardar")
			self.btnGuardar.setIcon(QIcon("Imagenes/guardar.jpg"))
			self.connect(self.btnGuardar,SIGNAL("clicked()"),self.accionGuadarEdicion)
			#labels que muestran informacion 
			self.labelsDatosEstudiantes = [QLabel(""),  QLabel(""), QLabel(""), QLabel(""), QLabel(""),QLabel(""), QLabel(""), QLabel(""), QLabel("") ]
			
			#lables que muestran informacion del padre

			self.labelsDatosPadre = [ QLabel(""), QLabel(""), QLabel(""), QLabel(""), QLabel(""),
			QLabel(""), QLabel(""), QLabel(""), QLabel(""), QLabel("") ]

			#labels que muestran informacion de la madre

			self.labelsDatosMadre = [ QLabel(""), QLabel(""), QLabel(""), QLabel(""), QLabel(""),
			QLabel(""), QLabel(""), QLabel(""), QLabel(""), QLabel("") ]
			
			#lables que muestran informacion del representante

			self.labelsDatosRep = [ QLabel(""), QLabel(""), QLabel(""), QLabel(""), QLabel(""),
			QLabel(""), QLabel(""), QLabel(""), QLabel(""), QLabel("") ]

			#variables de la pestaña de edicion
			self.listsexos=["Masculino","Femenino"] #lista para escoger el tipo de usuario
			self.listEstCivil = ["Soltero","Casado","Divorsiado","Union Libre","Viudo" ]
			self.listEtnia = ["BLANCO","MESTIZO","AFROECUATORIANO","INDIGENA", "MONTUBIO","NEGRO","MULATO","OTROS"]

			

			#lineas de texto para deditar al estudiante
			#se guardan en este orden los campos:
			#cedula, nombre, apellido,sexo(combobox), estadocivil(combobox), origen, etnia(combobox), fechanacimiento

			self.textDatosEstudiantes = [ QLineEdit(), QLineEdit(), QLineEdit(), QComboBox(), QComboBox(),
			QLineEdit(), QComboBox(), QLineEdit()]

			#expresiones regulares para los nombres
			self.regex = QRegExp(u"^[À-Ÿà-ÿA-Za-z\\s*\\u'\xf1'*]+$")
			self.validator = QRegExpValidator(self.regex)

			#expresiones regulares para la cedula
			self.regexN = QRegExp("[0-9]*")
			self.validatorN = QRegExpValidator(self.regexN)
						
			#itero los QLineEdit y les seteo la expresion regular y que sean solo de lectura
			for i in [0,1,2,5]:
				self.textDatosEstudiantes[i].setReadOnly(True)
			
			for i in [1,2,5]:
				self.textDatosEstudiantes[i].setValidator(self.validator)
			
			self.textDatosEstudiantes[0].setValidator(self.validatorN)

			
			#agrego la tabla de alumnos
			self.alumnos=MyTable(self)
			self.alumnos.setHeader(self.headersTabla)
			self.alumnos.addTable(self.manejadorBD.consultarEstudiante())
			self.paramBusqueda.textChanged.connect(self.alumnos.on_lineEdit_textChanged)
			self.comboBusquedaEstudiante.currentIndexChanged.connect(self.alumnos.on_comboBox_currentIndexChanged)
			self.alumnos.setEditable(False)
			
			
			# creacion de pestañas
			tab_widget = QTabWidget()
			tab_consultas = QScrollArea () #se crean dos pestañas
			tab_consultas.setWidget(QWidget())
			tab_consultas. setWidgetResizable ( True )
			tab_edicion = QScrollArea ()
			tab_edicion.setWidget(QWidget())
			tab_edicion.setWidgetResizable(True)
			
			#agrego las pestañas
			self.cont_consulta = QVBoxLayout(tab_consultas.widget()) #layout principal de esta gui, los widgets se agregan de forma horizontal
			self.cont_edicion = QVBoxLayout(tab_edicion.widget())
			
			tab_widget.addTab(tab_consultas,u"Consultas")
			tab_widget.addTab(tab_edicion,u"Edición")
			
			self.llenarTabConsultas()
			self.llenarTabEdicion()
			self.layoutBusqueda=QHBoxLayout()
			self.layoutBusqueda.addWidget(self.comboBusquedaEstudiante)
			self.layoutBusqueda.addWidget(self.paramBusqueda)
			self.contenedor.addLayout(self.layoutBusqueda)
			self.contenedor.addWidget(self.alumnos)
			self.contenedor.addWidget(tab_widget)

			self.connect(self.botonSeleccionar,SIGNAL("clicked()"),self.seleccionarEstudiante)
	
	def llenarTabConsultas(self):
		"""
		Esta funcion sirve para llenar los elementos de la pestaña consultas
		"""
		contenidoTab = self.cont_consulta
		
		# aqui estoy creando la primera fila de la pestaña
		primeraFila = QHBoxLayout()
		primeraFila.addWidget(self.botonSeleccionar)
		contenidoTab.addLayout(primeraFila)
		
		#creacion de la tercera fila
		terceraFila = QHBoxLayout()
		GBoxEstudianteInfo = QGroupBox ( "Estudiante" )
		vboxEstInfo = QFormLayout()
		GBoxEstudianteInfo.setLayout(vboxEstInfo)
		terceraFila.addWidget(GBoxEstudianteInfo)
		
		listDatosEst = [u"Número de matrícula",u"Cédula:","Nombres:","Apellidos:", "Sexo:","Estado Civil:","Origen:","Etnia:" ,"Fecha de nacimiento:"]
		
		for i in range (0,9):
			vboxEstInfo.addRow(listDatosEst[i], self.labelsDatosEstudiantes[i])


		GBoxPadreInfo = QGroupBox ( "Padre" )
		vboxPadreInfo = QFormLayout()
		GBoxPadreInfo.setLayout(vboxPadreInfo)
		terceraFila.addWidget(GBoxPadreInfo)
		
		listDatosPersona = [u"Cédula:","Nombres:","Apellidos:","Sexo:","Fecha de Nacimiento:","Estado Civil:",u"Ocupación",
		"Lugar de Trabajo:",u"Teléfono:", u"Dirección:"]

		for i in range (0,10):
			vboxPadreInfo.addRow(listDatosPersona[i], self.labelsDatosPadre[i])

		contenidoTab.addLayout(terceraFila)
		#cuarta fila
		cuartaFila = QHBoxLayout()
		GBoxMadreInfo = QGroupBox ( "Madre" )
		vboxMadreInfo = QFormLayout()
		GBoxMadreInfo.setLayout(vboxMadreInfo)
		cuartaFila.addWidget(GBoxMadreInfo)
		
		for i in range (0,10):
			vboxMadreInfo.addRow(listDatosPersona[i], self.labelsDatosMadre[i])

		GBoxRepInfo = QGroupBox ( "Representante" )
		vboxRepInfo = QFormLayout()
		GBoxRepInfo.setLayout(vboxRepInfo)
		cuartaFila.addWidget(GBoxRepInfo)
		contenidoTab.addLayout(cuartaFila)

		for i in range (0,10):
			vboxRepInfo.addRow(listDatosPersona[i], self.labelsDatosRep[i])



	def llenarTabEdicion(self):
		"""
		Esta funcion sirve para llenar los elementos de la pestaña consultas
		"""
		contenidoTab = self.cont_edicion
		listDatosEst = [u"Cédula","Nombres:","Apellidos:", "Sexo:","Estado Civil:","Origen:","Etnia:"]
		primerafila = QHBoxLayout();
		primerafila.addWidget(self.btnEditar)
		contenidoTab.addLayout(primerafila)
		form_layout = QFormLayout()

		for i in range (0,7):
			form_layout.addRow(listDatosEst[i], self.textDatosEstudiantes[i])

		self.fechaNacimiento=QCalendarWidget()
		self.fechaNacimiento.setMinimumDate(QDate(1940,1,1))
		self.fechaNacimiento.setMaximumDate(QDate(2015,1,1))
		self.fechaNacimiento.setGridVisible(False)
		fechacont = QVBoxLayout()
		fechacont.addWidget(self.textDatosEstudiantes[7])
		fechacont.addWidget(self.fechaNacimiento)

		form_layout.addRow("Fecha de Nacimiento", fechacont)
		contenidoTab.addLayout(form_layout)

		terceraFila = QHBoxLayout()
		terceraFila.addWidget(self.btnGuardar)
		terceraFila.addWidget(QLabel("                   "))

		contenidoTab.addLayout(terceraFila)
		self.textDatosEstudiantes[3].addItems(self.listsexos)
		self.textDatosEstudiantes[4].addItems(self.listEstCivil)
		self.textDatosEstudiantes[6].addItems(self.listEtnia)






	def activarEdicion(self):
		#obtengo los estudiantes de la tabla
		Listestudiante = self.alumnos.getSelectedRegister()
		
		if Listestudiante:
			estudiante = Listestudiante[-1]
			self.matricula = str(estudiante[0])
			cedula = str(estudiante[1])
			self.textDatosEstudiantes[0].setText(cedula) #seteo la cedula
			nombres = unicode(estudiante[2])
			self.textDatosEstudiantes[1].setText(nombres) #seteo los nombres
			apellidos = unicode(estudiante[3])
			self.textDatosEstudiantes[2].setText(apellidos) #seteo los apellidos

			#seteo el sexo
			sexo = str(estudiante[4])
			indiceComboSexo = self.listsexos.index(sexo)
			self.textDatosEstudiantes[3].setCurrentIndex(indiceComboSexo)

			#seteo el estado civil
			ecivil = str(estudiante[5])
			indiceComboEstCivil = self.listEstCivil.index(ecivil)
			self.textDatosEstudiantes[4].setCurrentIndex(indiceComboEstCivil)
			
			origen = unicode(estudiante[6])
			self.textDatosEstudiantes[5].setText(origen) #seteo el origen
			
			#seteo la etnia
			etnia = unicode(estudiante[7])
			indiceComboetnia = self.listEtnia.index(etnia)
			self.textDatosEstudiantes[6].setCurrentIndex(indiceComboetnia) #seteo los apellidos

			#seteo la fecha
			fecha = str(estudiante[8])
			self.textDatosEstudiantes[7].setText(fecha)
			self.cedulafact = str(estudiante[8])

			faux = fecha.split("-")
			anos = int(faux[0])
			mes = int(faux[1])
			dia = int(faux[2])
			self.fechaNacimiento.setSelectedDate(QDate(anos, mes, dia)) 
			

			for i in [0,1,2,5,7]:
				self.textDatosEstudiantes[i].setReadOnly(False)


	def accionGuadarEdicion(self):

		cedula = str(self.textDatosEstudiantes[0].displayText())
		nombre = unicode(self.textDatosEstudiantes[1].displayText())
		apellido = unicode(self.textDatosEstudiantes[2].displayText())
		sexo = str(self.textDatosEstudiantes[3].currentText())
		estado_civil = str(self.textDatosEstudiantes[4].currentText())
		origen = unicode(self.textDatosEstudiantes[5].displayText())
		etnia = str(self.textDatosEstudiantes[6].currentText())
		fecha = self.obtenerFechaString( self.fechaNacimiento.selectedDate())

		tupla = (self.matricula, cedula, nombre, apellido, sexo, estado_civil, origen, etnia, fecha)
		print tupla

		if (not(len(cedula)==10)):
			QMessageBox.about(self, 'Error',u'Cédula inválida: debe tener 10 dígitos')
		elif (cedula =="" or nombre == "" or apellido == "" or origen =="" ):
			QMessageBox.about(self, 'Error',u'Datos sin llenar: llene todos los datos')
		else:
			QMessageBox.about(self,"Aviso",u'Se han guardado los cambios con éxito')
			self.manejadorBD.editarEstudiante(tupla)
			for i in [0,1,2,5]:
				self.textDatosEstudiantes[i].setReadOnly(True)




	def seleccionarEstudiante(self):
		Listestudiante = self.alumnos.getSelectedRegister()
		
		#Si esa  lista no esta vacia se obtienen los datos
		if Listestudiante:
			estudiante = Listestudiante[-1]
			#lleno los campos de la seccion estudiante
			for i in range (len(self.labelsDatosEstudiantes )):
				label= self.labelsDatosEstudiantes[i]
				label.setText(estudiante[i])

			numMatricula= estudiante[0]
			result = self.manejadorBD.estudianteObtenerPersona(numMatricula, "Padre")
			
			if  result:
				datosPadre = list(result[0])
				for i in range (len(self.labelsDatosPadre )):
					label= self.labelsDatosPadre[i]
					label.setText(unicode(datosPadre[i]))
			else:
				for i in range (len(self.labelsDatosPadre )):
					label= self.labelsDatosPadre[i]
					label.setText("")


			result = self.manejadorBD.estudianteObtenerPersona(numMatricula, "Madre")
			if result:
				datosMadre = list(result[0])

				for i in range (len(self.labelsDatosMadre )):
					label= self.labelsDatosMadre[i]
					label.setText(unicode(datosMadre[i]))
			else:
				for i in range (len(self.labelsDatosMadre )):
					label= self.labelsDatosMadre[i]
					label.setText("")


			result = self.manejadorBD.estudianteObtenerPersona(numMatricula, "Representante")
			if result:
				datosRep = list(result[0])

				for i in range (len(self.labelsDatosRep )):
					label= self.labelsDatosRep[i]
					label.setText(unicode(datosRep[i]))
			else:

				for i in range (len(self.labelsDatosRep )):
					label= self.labelsDatosRep[i]
					label.setText("")


	def obtenerFechaString(self,date):
		dia=date.day()
		mes=date.month()
		anio=date.year()
		return "%d-%d-%d" %(anio,mes,dia)
