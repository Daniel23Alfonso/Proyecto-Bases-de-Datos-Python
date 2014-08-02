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
		self.row=0


	def setHeader(self,listaCabezeras):
		labels=QStringList()
		for i in range(len(listaCabezeras)):
			labels.append(QString(listaCabezeras[i]))
		self.modelo.setHorizontalHeaderLabels(labels)


	def addTable(self,listaTuplas):
		for registro in listaTuplas:
			self.addRow(registro)

	def addRow(self,listaDatos):
		for i in range(len(listaDatos)):
			self.modelo.setItem(self.row,i,QStandardItem(QString(str(listaDatos[i]))))
		self.row=self.row+1		

	#callback para los lineEdit
	def on_lineEdit_textChanged(self,text):
		search = QRegExp(text, Qt.CaseInsensitive,QRegExp.RegExp)
		self.proxy.setFilterRegExp(search)

	#callback para los combos
	def on_comboBox_currentIndexChanged(self, index):
		self.proxy.setFilterKeyColumn(index)



