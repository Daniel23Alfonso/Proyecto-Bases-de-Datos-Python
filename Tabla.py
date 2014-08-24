# -*- coding: utf-8 -*- 
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
		self.resizeColumnsToContents()
		self.resizeRowsToContents()
		self.emit(SIGNAL("DataChanged()"))
		self.emit(SIGNAL("LayoutAboutToBeChanged()"))
 		#self.arraydata = datain
 		self.emit(SIGNAL("LayoutChanged()"))
 		self.setItemDelegate(ValidatedItemDelegate())
 		#self.dataChanged.emit(self.createIndex(0, 0),self.createIndex(self.rowCount(0),self.columnCount(0)))
 		#self.emit(SIGNAL("DataChanged(QModelIndex,QModelIndex)"),self.createIndex(0, 0),self.createIndex(self.rowCount(0),self.columnCount(0)))
		self.row=0
		self.columnas=0

	def setHeader(self,listaCabezeras):
		self.cabezeras=listaCabezeras
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
		i=self.row
		for i in range(len(listaDatos)):
			self.modelo.setItem(self.row,i,QStandardItem(QString(str(listaDatos[i]))))
		self.row=self.row+1		

	def getSize(self):
		return self.modelo.rowCount()

	def deleteRow(self,indice):
		if self.getSize()>0:
			self.modelo.removeRow(indice)
			self.row-=1

	def deleteData(self):#deja la tabla en blanco
		self.modelo=QStandardItemModel(self.ventana)
		self.proxy.setSourceModel(self.modelo)
		self.setModel(self.proxy)
		self.setHeader(self.cabezeras)
		self.row=0

	def getRegister(self,fila):#retorna el registro de la posicion-fila dentro de la tabla
		registro=[]
		#index = self.currentIndex()
		top_left = self.modelo.index(0, 0)
		bottom_right = self.modelo.index(self.row - 1,self.columnas- 1)
		self.emit(SIGNAL("DataChanged(QModelIndex,QModelIndex)"),top_left,bottom_right)
		if(self.modelo.setData(QModelIndex(),QVariant())):
			print "entro"
		else:
			print "no entro"

		#self.modelo.dataChanged.emit(top_left, bottom_right)
		#self.layoutChanged.emit()
		for col in range(self.columnas):
			
			item=self.modelo.item(fila,col)#item es de tipo QStandardItem y retorna la referencia a la celda de la posicion fila,col
			
			if item != None:
				texto=item.text()#texto es de tipo QString y obtiene el texto de la celda
				registro.append(texto)
		return registro

	def getSelectedRegister(self):#obtiene todos los registros seleccionados
		filasSeleccionadas=self.getIndexSelected()#retorna una lista con todos las filas seleccionadas dentro de la tabla
		registros=[]
		for i in range(len(filasSeleccionadas)):
			fila_actual=filasSeleccionadas[i]#objeto_actual es de tipo QModelIndex
			#fila_actual.row() retorna el indice perteneciente a esa fila en la tabla
			registros.append(self.getRegister(fila_actual.row()))
		#for registro in registros:
		#	self.printRegistro(registro)
		return registros

	def getIndexSelected(self):
		return self.selectedIndexes()
		
	def printRegistro(self,lista):
		for r in lista:
			print r

	def setEditable(self,flag):
		for i in range(self.row):
			for j in range(self.columnas):	
				item=self.modelo.item(i,j)
				item.setEditable(flag)


	#callback para los lineEdit
	def on_lineEdit_textChanged(self,text):
		search = QRegExp(text, Qt.CaseInsensitive,QRegExp.RegExp)
		self.proxy.setFilterRegExp(search)

	#callback para los combos
	def on_comboBox_currentIndexChanged(self, index):
		self.proxy.setFilterKeyColumn(index)


class ValidatedItemDelegate(QStyledItemDelegate):
	def createEditor(self, widget, option, index):
		if not index.isValid():
			return 0
		if index.column() == 0: #only on the cells in the first column
			editor = QLineEdit(widget)
			validator = QRegExpValidator(QtCore.QRegExp("[0-9]*"), editor)
			editor.setValidator(validator)
			return editor
		return super(ValidatedItemDelegate, self).createEditor(widget, option, index)

class Model(QAbstractTableModel):
    def __init__(self, parent=None):
        super(Model, self).__init__(parent)
        # list of lists containing [data for cell, changed]
        #self._data = [[['%d - %d' % (i, j), False] for j in range(10)] for i in range(10)]

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._data[0])

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable

    def data(self, index, role):
        if index.isValid():
            data, changed = self._data[index.row()][index.column()]

            if role in [QtCore.Qt.DisplayRole, QtCore.Qt.EditRole]:
                return data

            if role == QtCore.Qt.BackgroundRole and changed:
                return QtGui.QBrush(QtCore.Qt.darkBlue)

    def setData(self, index, value, role):
        if role == QtCore.Qt.EditRole:
            # set the new value with True `changed` status
            self._data[index.row()][index.column()] = [value.toString(), True]
            self.dataChanged.emit(index, index)
            return True
        return False

