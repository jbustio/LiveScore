from PyQt4.Qt import QDialog
from Vistas.Ui_ayudaDialog import Ui_Dialog


class AyudaDialog(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent) 
        self.setupUi(self)