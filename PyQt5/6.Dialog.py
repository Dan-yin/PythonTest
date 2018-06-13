
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, 
    QInputDialog, QApplication)
 
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
 
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        self.le = QLineEdit(self)
        self.le.move(130, 22)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()
        
        
    def showDialog(self):
        
        m = text, oik = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        #print(m)

        if oik:
            self.le.setText(str(text))

from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, 
    QColorDialog, QApplication)
from PyQt5.QtGui import QColor
 
 
class Example1(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
 
        col = QColor(0, 0, 0) 
 
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
 
        self.btn.clicked.connect(self.showDialog)
 
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" 
            % col.name())
        self.frm.setGeometry(130, 22, 100, 100)            
        
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()
        
        
    def showDialog(self):
      
        col = QColorDialog.getColor()
 
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % col.name())
        
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
    QSizePolicy, QLabel, QFontDialog, QApplication)
 
 
class Example2(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
 
        vbox = QVBoxLayout()
 
        btn = QPushButton('Dialog', self)
        #btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        btn.move(20, 20)
 
        vbox.addWidget(btn)
 
        btn.clicked.connect(self.showDialog)
        
        #self.lbl = QLabel('Knowledge only matters', self)
        self.lbl = QLabel("水",self)
        self.lbl.move(130, 20)
 
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)          
        
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()
        
        
    def showDialog(self):
 
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example2()
    sys.exit(app.exec_())