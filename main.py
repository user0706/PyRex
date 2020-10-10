from functions import *
from mainGUI import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
import sys

import os
import re


class MyWin(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.Pattern = ''
		self.TestString = ''

		self.ui.ProcessPushButton.clicked.connect(self.PatternChanged)

		self.ui.RegexSheetPushButton.clicked.connect(self.Sheet)
		self.ui.CodeGeneratorPushButton.hide()
		self.ui.AboutPushButton.hide()

		self.ResultWidget = None
		self.horizontalLayout_4 = None
		self.ResultTag = None
		self.ResultRange = None
		self.ResultText = None
		self.Info = []
		self.Match = []

		self.ColorList = ['rgb(198, 227, 255)','rgb(198, 233, 157)','rgb(245, 171, 165)','rgb(255, 191, 109)','rgb(193, 203, 235)','rgb(215, 253, 227)','rgb(227, 255, 172)','rgb(232, 141, 238)','rgb(207, 221, 103)','rgb(255, 172, 192)','rgb(132, 214, 238)']

	def UpdateInfo(self):
		'''Visual display of search results'''
		for i, v in enumerate(self.Info):
			if 'Full match' in v[0]:
				FullMatchTagUI(self.ui.scrollAreaWidgetContents, self.ui.verticalLayout_5, v[0])
				color = self.ColorList[0]
			else:
				color = GenerateGroupColor(self.ColorList, v[0])
			InfoUI(self.ResultWidget, self.horizontalLayout_4, self.ResultTag, self.ResultRange, self.ResultText, i, color, self.ui.scrollAreaWidgetContents, self.ui.verticalLayout_5, v)
		SpacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
		self.ui.verticalLayout_5.addItem(SpacerItem)

	def PatternChanged(self):
		'''Search for test text based on a pattern and display the results'''
		clearLayout(self.ui.verticalLayout_5)
		self.Info = []
		self.Pattern = self.ui.RegexLineEdit.text()
		self.TestString = self.ui.TestStringTextEdit.toPlainText()
		self.Info = Process(self.TestString, self.Pattern, self.Info)
		self.ResultWidget, self.horizontalLayout_4, self.ResultTag, self.ResultRange, self.ResultText = PreprocessInfo(self.Info)
		self.UpdateInfo()
		ClearHighlight(self.ui.TestStringTextEdit, self.TestString)
		for k, v in enumerate(self.Info):
			hrange = HighlightRange(v[1])
			if 'Full match' in v[0]:
				Highlight(self.ui.TestStringTextEdit, QColor(198, 227, 255), hrange[0], hrange[1])
			else:
				color = GenerateGroupColor(self.ColorList, v[0])
				r, g, b = strColorTolist(color)
				Highlight(self.ui.TestStringTextEdit, QColor(r,g,b), hrange[0], hrange[1])

	def Sheet(self):
		'''Open the sheet.py script'''
		os.system('python sheet.py')

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyWin()
	myapp.show()
	sys.exit(app.exec_())
