#!/usr/bin/python
 
import MySQLdb
import sys
import time
import threading
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from VistaIngresoSist import*
 
bd = MySQLdb.connect("127.0.0.1","root","sasukekun30","BasePeliculas" )
 
# Preparamos el cursor que nos va a ayudar a realizar las operaciones con la base de datos
cursor = bd.cursor()

cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print "Version Base de Datos : %s " % data
print "Se conecto correctamente" 


cursor.execute("USE BasePeliculas")
cursor.execute("SHOW TABLES")
tables = cursor.fetchall() 
cont=0
for (table_name,) in cursor:
        cont+=1
        print(table_name)
print "numero de tablas: %d" %cont
 



 
bd.close()
app = QApplication(sys.argv)
vista1 = VistaIngresoSist()
vista1.show()
app.exec_()