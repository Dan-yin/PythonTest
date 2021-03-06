'''
所有的GUI程序都是事件驱动的。事件主要由用户触发，但也可能有其他触发方式：
例如网络连接、window manager或定时器。当我们调用QApplication的exec_()方法时会使程序进入主循环。主循环会获取并分发事件。

在事件模型中，有三个参与者：

事件源
事件对象
事件接收者


事件源是状态发生变化的对象。它会生成事件。事件(对象)封装了事件源中状态的变动。事件接收者是要通知的对象。
事件源对象将事件处理的工作交给事件接收者。

PyQt5有一个独特的signal&slot(信号槽)机制来处理事件。信号槽用于对象间的通信。
signal在某一特定事件发生时被触发，slot可以是任何callable对象。当signal触发时会调用与之相连的slot。
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
    QVBoxLayout, QApplication)
 
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        '''
        在这里我们将滚动条的valueChanged信号连接到lcd的display插槽。

        sender是发出信号的对象。receiver是接收信号的对象。slot(插槽)是对信号做出反应的方法。
        '''
        
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
 
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
 
        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()
        
 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
 
 
class Example1(QWidget):
    '''
    事件处理器keyPressEvent
    '''
    def __init__(self):
        super().__init__()
         
        self.initUI()
        
        
    def initUI(self):      
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()
        
        
    def keyPressEvent(self, e):
        
        if e.key() == Qt.Key_Escape:
            self.close()

from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
 
 
class Example2(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
 
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)
 
        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)
      
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
        
        
    def buttonClicked(self):
      
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication
 
 

    
 
class Example3(QMainWindow):
    '''
    pyqtSignal(parameter),obpyqtSignal.emit(parameter)
    '''
    class Communicate(QObject):
    
        closeApp = pyqtSignal() 
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
 
        self.c = self.Communicate()
        self.c.closeApp.connect(self.close)       
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
        
        
    def mousePressEvent(self, event):
        
        self.c.closeApp.emit()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example3()
    sys.exit(app.exec_())