import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MyTable(QTableView):

	def __init__(self,ventana):
		QTableView.__init__(self,ventana)
		self.proxy = QSortFilterProxyModel(ventana)
		self.ventana=ventana
		self.modelo=QStandardItemModel(self.ventana)
		self.proxy.setSourceModel(self.modelo)
		self.setModel(self.proxy)
		self.labels=QStringList()
		self.row=0

	def setHeader(self,listaCabezeras):
		self.labels=QStringList()
		col=0
		for i in range(len(listaCabezeras)):
			self.labels.append(QString(listaCabezeras[i]))
			col+=1
		self.modelo.setHorizontalHeaderLabels(self.labels)
		self.columnas=col
	
	def addCol(self,col):
		self.labels.append(QString(col))
		self.modelo.setHorizontalHeaderLabels(self.labels)


	def addTable(self,listaTuplas):

		for registro in listaTuplas:
			self.addRow(registro)

	def addRow(self,listaDatos):
		for i in range(len(listaDatos)):
			self.modelo.setItem(self.row,i,QStandardItem(QString(str(listaDatos[i]))))
		self.row=self.row+1		


	def getRegister(self,fila):#retorna el registro de la posicion-fila dentro de la tabla
		registro=[]
		for col in range(self.columnas):
			item=self.modelo.item(fila,col)#item es de tipo QStandardItem y retorna la referencia a la celda de la posicion fila,col
			texto=item.text()#texto es de tipo QString y obtiene el texto de la celda
			registro.append(texto)
		#self.printRegistro(registro)
		return registro

	def getSelectedRegister(self):#obtiene todos los registros seleccionados
		filasSeleccionadas=self.selectedIndexes()#retorna una lista con todos las filas seleccionadas dentro de la tabla
		registros=[]
		for i in range(len(filasSeleccionadas)):
			fila_actual=filasSeleccionadas[i]#objeto_actual es de tipo QModelIndex
			#fila_actual.row() retorna el indice perteneciente a esa fila en la tabla
			registros.append(self.getRegister(fila_actual.row()))
		for registro in registros:
			self.printRegistro(registro)
		return registros


	def printRegistro(self,lista):
		for r in lista:
			print r

	#callback para los lineEdit
	def on_lineEdit_textChanged(self,text):
		search = QRegExp(text, Qt.CaseInsensitive,QRegExp.RegExp)
		self.proxy.setFilterRegExp(search)

	#callback para los combos
	def on_comboBox_currentIndexChanged(self, index):
		self.proxy.setFilterKeyColumn(index)

