import sys
import os

import PyQt5
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(800,600)
    w.setWindowTitle('simplewindows')
    w.show()
    sys.exit(app.exec_())

#os.system('pause')
