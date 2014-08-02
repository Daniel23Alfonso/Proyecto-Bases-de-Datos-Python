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
app = QApplication(sys.argv)
vista1 = VistaIngresoSist()
vista1.show()
app.exec_()