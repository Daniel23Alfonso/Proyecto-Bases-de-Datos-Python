import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
#data = {'col1':['1','2','3'], 'col2':['4','5','6'], 'col3':['7','8','9']}
 
class MyTable(QTableWidget):
	def __init__(self,*args):
		QTableWidget.__init__(self, *args)
        #tableWidget.setRowCount(len(entries))
		self.rows=0
	
	def setHeader(self,header):
		cad=""
		for l in header:
			cad=cad+";"+l
		self.setColumnCount(len(header))
		self.setHorizontalHeaderLabels(QString(cad[1:]).split(";"))
		
	
	def vaciar(self):
		self.clear()

	def addRow(self,l):
		i=0
		self.insertRow(self.rows)
		for elemento in l:
			self.setItem(self.rows,i,QTableWidgetItem(QString("%1").arg(elemento)))
			i=i+1
		self.rows=self.rows+1


 

#app = QApplication(sys.argv)
#table = MyTable()
#table.show()
#sys.exit(app.exec_())
 
