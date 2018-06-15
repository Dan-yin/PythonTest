
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
        '''
        SizePolicy

        A. Fixed：控件不能放大或者缩小，控件的大小就是它的sizeHint。

        B. Minimum：控件的sizeHint为控件的最小尺寸。控件不能小于这个sizeHint，但是可以

        放大。

        C. Maximum：控件的sizeHint为控件的最大尺寸，控件不能放大，但是可以缩小到它的最小

        的允许尺寸。

        D. Preferred：控件的sizeHint是它的sizeHint，但是可以放大或者缩小

        E. Expandint：控件可以自行增大或者缩小
        '''
        vbox = QVBoxLayout()
 
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
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
        
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
 
 
class Example3(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
 
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
 
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)
 
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
        
    def showDialog(self):
 
        #fname = QFileDialog.getOpenFileName(self, 'Open file', '/home','cssdwasdfv(*.csv)')
        fnames = QFileDialog.getOpenFileNames(self,'Open file1','/home','csv(*.csv)')
        
        for fname in fnames[0]:
            if fname:
                f = open(fname, 'r')
    
                with f:
                    data = f.read()
                    #self.textEdit.setText(data)  
                    self.textEdit.append(data)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example3()
    sys.exit(app.exec_())