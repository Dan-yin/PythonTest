import sys
from PyQt5.QtWidgets import QApplication,QWidget,QToolTip,QPushButton,QMessageBox,QDesktopWidget
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
    '''
    Qicon
    '''
    def __init__(self):
        super().__init__()
        self.unitUI()

    def unitUI(self):
        self.setGeometry(300,300,200,200)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        #self.setWindowIcon(QIcon(r'C:\Users\1744\Desktop\web2.png'))
        self.show()

class Example1(QWidget):
    '''
    Tooltip,pushbutton
    '''
    def __init__(self):
        super().__init__()
        self.unitUI()

    def unitUI(self):    
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Button',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Tooltips')
        self.show()

class Example2(QWidget):
    '''
    close widget
    '''
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qbtn = QPushButton('quit',self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle("Quit Button")
        self.show()

class Example3(QWidget):
    '''
    quit closeEvent
    center
    '''
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Message Box')
        self.center()
        self.show()

    def closeEvent(self,event):
        replay = QMessageBox.question(self,'Messagge',"Are you sure to quit",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        
        if replay == QMessageBox.Yes:
            event.accept    
        else:
            event.ignore
            #控制窗口显示在屏幕中心的方法    
    def center(self):
        
        #获得窗口
        qr = self.frameGeometry()
        #获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        #显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    """
    QWidget: Must construct a QApplication before a QWidget
    """
    
    app = QApplication(sys.argv)
    w = Example3()
    sys.exit(app.exec_())