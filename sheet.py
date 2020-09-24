from sheetGUI import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
import sys

class SheetWin(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		#Brojac predstavlja index slobodnog elementa baze
		self.ui = Ui_SheetWindow()
		self.ui.setupUi(self)

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = SheetWin()
	myapp.show()
	sys.exit(app.exec_())