#!/usr/bin/python
 
import MySQLdb
import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from VistaIngresoSist import*
 
bd = MySQLdb.connect("localhost","root","sasukekun30","prueba_db" )
 
# Preparamos el cursor que nos va a ayudar a realizar las operaciones con la base de datos
cursor = bd.cursor()
 

cursor.execute("SELECT VERSION()")
 

data = cursor.fetchone()
 
print "Version Base de Datos : %s " % data
 
bd.close()
app = QApplication(sys.argv)
vista1 = VistaIngresoSist()
vista1.show()
app.exec_()