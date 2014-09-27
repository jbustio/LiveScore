import sys

from PyQt4 import QtGui
from Vistas.mainWindow import MainWindow


def main():
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
