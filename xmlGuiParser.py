from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import sys
import xml.etree.ElementTree as ET

class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(550,200,800,600)
        self.setWindowTitle("SS XML Parser")
        self.label = QtWidgets.QLabel(self)
        self.label.setText("XML Parser")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.adjustSize()
        self.label.move(20,10)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText("Choose a file to parse")
        self.label_2.setGeometry(QtCore.QRect(30, 165, 311, 101))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.adjustSize()

        
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setGeometry(QtCore.QRect(30, 200, 111, 31))
        self.b1.setText("Open File")
        self.b1.clicked.connect(self.clicked)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setGeometry(QtCore.QRect(200, 200, 111, 31))
        self.b2.setText("Parse")
        self.b2.clicked.connect(self.parser)

    def clicked(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file',"c:\"")
        self.update(self.fname)
    
    
    def update(self,fname):
        self.label_2.setText(fname[0])
        self.label_2.setStyleSheet('QLabel { color:red;}')
        self.label_2.adjustSize()
    
    def parser(self,fname):
        
        tree = ET.parse(str(self.fname[0]))
        root = tree.getroot()
        try:
            f=open("test.txt",mode = 'w',encoding= 'utf-8')
            
        # all items data
            f.write("PARSED DATA\n")
            f.write("\nROOT NODE-" + root.tag)
            f.write("\n")
            for elem in root:
                f.write("\n" + elem.tag + "-" + elem.get("id"))
            for subelem in elem:
                f.write("\n" + subelem.tag + "-" + subelem.text)
            f.write("\n")
            f.write("\n")
        finally:
            f.close()
            self.show_popup()
    
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Parsing of XML File completed")
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()  # this will show our messagebox
        return 




def window():
    app = QApplication(sys.argv)
    win = myWindow()
    
    

    
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()