#!/usr/bin/python
 
import MySQLdb
import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from VistaIngresoSist import*
from ManejadorBD import *

M=ManejadorBD()
M.imprimirTablas()
r=M.consulta("SELECT * FROM Reviewer")
print "Sin Condiciones"
for (a,b) in r:
	print a,",",b

r=M.consulta("SELECT * FROM Reviewer WHERE name like %s",("c%"))
print "Usando Condiciones"
for (a,b) in r:
	print a,",",b
app = QApplication(sys.argv)
vista1 = VistaIngresoSist()
vista1.show()
app.exec_()