# -*- coding: utf-8 -*- 
#!/usr/bin/python
import MySQLdb
import sys
from VistaIngresoSist import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

db = MySQLdb.connect(user="root", # your username
                      passwd="", # your password
                      db="prueba") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM primera")

# print all the first cell of all the rows
cur.execute("SELECT VERSION()")
for row in cur.fetchall() :
    print row[0]

login = VistaIngresoSist()




