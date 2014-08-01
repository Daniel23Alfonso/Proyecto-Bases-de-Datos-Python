from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys

def main():  
    app     = QApplication(sys.argv)
    table   = QTableWidget()
    tableItem   = QTableWidgetItem()
    
    table.setWindowTitle("Set QTableWidget Header Alignment")
    table.resize(500, 250)
    table.setColumnCount(3)
    table.setRowCount(1)
    
    table.setHorizontalHeaderLabels(QString("HEADER 1;HEADER 2;HEADER 3;HEADER 4").split(";"))

    table.setItem(0,0, QTableWidgetItem("THIS IS LONG TEXT 1"))
    table.setItem(0,1, QTableWidgetItem("THIS IS LONG TEXT 2"))
    table.setItem(0,2, QTableWidgetItem("THIS IS LONG TEXT 3"))    
    
    table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
    table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
    table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)    
    table.setColumnCount(5)
    table.resizeColumnsToContents();
    table.setHorizontalHeaderLabels(QString("HEADER 1;HEADER 2;HEADER 3;HEADER 4;HEADER5").split(";"))    
    table.show()
    return app.exec_()

if __name__ == '__main__':
    main()