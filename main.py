from mainGUI import *
from function import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
import sys

import os
import re
import random

class MyWin(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		#Brojac predstavlja index slobodnog elementa baze
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.Pattern = ''
		self.TestString = ''

		self.ui.ProcessPushButton.clicked.connect(self.PatternChanged)
		self.ui.TestStringTextEdit.textChanged.connect(self.TestStringChanged)

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

	def Process(self):
		if self.Pattern:
			try:
				
				regex = r"{}".format(str(self.Pattern))

				matches = re.finditer(regex, self.TestString, re.MULTILINE)

				for matchNum, match in enumerate(matches, start=1):
					self.Info.append(['Full match '+str(matchNum), str(match.start())+'-'+str(match.end()), str(match.group())])

					for groupNum in range(0, len(match.groups())):
						groupNum = groupNum + 1
						
						self.Info.append(['Group '+str(groupNum), str(match.start(groupNum))+'-'+str(match.end(groupNum)), str(match.group(groupNum))])

			except:
				pass
		else:
			pass

	def UpdateInfo(self):
		ColorList = ['rgb(198, 227, 255)','rgb(198, 233, 157)','rgb(245, 171, 165)','rgb(255, 191, 109)','rgb(193, 203, 235)','rgb(215, 253, 227)','rgb(227, 255, 172)','rgb(232, 141, 238)','rgb(207, 221, 103)','rgb(255, 172, 192)','rgb(132, 214, 238)']
		for i, v in enumerate(self.Info):
			print(v[0])
			if 'Full match' in v[0]:
				self.CollectionWidget = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
				self.CollectionWidget.setMinimumSize(QtCore.QSize(300, 25))
				self.CollectionWidget.setMaximumSize(QtCore.QSize(500, 25))
				self.CollectionWidget.setObjectName("CollectionWidget")
				self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.CollectionWidget)
				self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
				self.verticalLayout_6.setSpacing(0)
				self.verticalLayout_6.setObjectName("verticalLayout_6")
				self.CollectionLabel = QtWidgets.QLabel("Match {}".format(str(v[0].split(' ')[-1])))
				font = QtGui.QFont()
				font.setPointSize(8)
				font.setBold(True)
				self.CollectionLabel.setFont(font)
				self.CollectionLabel.setStyleSheet("color: rgb(78, 123, 179);\nmargin-bottom:5px;\nmargin-top:10px;")
				self.CollectionLabel.setObjectName("CollectionLabel")
				self.verticalLayout_6.addWidget(self.CollectionLabel)
				self.CollectionLine = QtWidgets.QFrame(self.CollectionWidget)
				self.CollectionLine.setStyleSheet("background-color: rgba(199, 199, 199, 50%);\nmin-height:1px;\nmax-height:1px;")
				self.CollectionLine.setFrameShape(QtWidgets.QFrame.HLine)
				self.CollectionLine.setFrameShadow(QtWidgets.QFrame.Sunken)
				self.CollectionLine.setObjectName("CollectionLine")
				self.verticalLayout_6.addWidget(self.CollectionLine)
				self.ui.verticalLayout_5.addWidget(self.CollectionWidget)
				color = ColorList[0]
			elif v[0] == 'Group 1':
				color = ColorList[1]
			elif v[0] == 'Group 2':
				color = ColorList[2]
			elif v[0] == 'Group 3':
				color = ColorList[3]
			elif v[0] == 'Group 4':
				color = ColorList[4]
			elif v[0] == 'Group 5':
				color = ColorList[5]
			elif v[0] == 'Group 6':
				color = ColorList[6]
			elif v[0] == 'Group 7':
				color = ColorList[7]
			elif v[0] == 'Group 8':
				color = ColorList[8]
			elif v[0] == 'Group 9':
				color = ColorList[9]
			elif v[0] == 'Group 10':
				color = ColorList[10]
			else:
				color = random.choice(ColorList)

			self.ResultWidget[i] = QtWidgets.QWidget(self.ui.scrollAreaWidgetContents)
			self.ResultWidget[i].setObjectName("ResultWidget")
			self.horizontalLayout_4[i] = QtWidgets.QHBoxLayout(self.ResultWidget[i])
			self.horizontalLayout_4[i].setContentsMargins(0, 7, 0, 0)
			self.horizontalLayout_4[i].setObjectName("horizontalLayout_4")
			if 'Full match' in v[0]:
				self.ResultTag[i] = QtWidgets.QLabel(' '.join(v[0].split(' ')[:-1]))
			else:
				self.ResultTag[i] = QtWidgets.QLabel(v[0])
			self.ResultTag[i].setStyleSheet("min-width:60px;\nmax-width:60px;\nmin-height:20px;\nmax-height:20px;\nbackground-color: {};\nborder:2px;\nborder-radius:3px;\ncolor:  rgb(54, 54, 54);\n".format(color))
			self.ResultTag[i].setAlignment(QtCore.Qt.AlignCenter)
			self.ResultTag[i].setObjectName("ResultTag")
			self.horizontalLayout_4[i].addWidget(self.ResultTag[i], 0, QtCore.Qt.AlignTop)
			self.ResultRange[i] = QtWidgets.QLabel(v[1])
			self.ResultRange[i].setStyleSheet("min-width:60px;\nmax-width:60px;\nmin-height:20px;\nmax-height:20px;\ncolor: rgb(54, 54, 54);\n")
			self.ResultRange[i].setAlignment(QtCore.Qt.AlignCenter)
			self.ResultRange[i].setWordWrap(True)
			self.ResultRange[i].setObjectName("ResultRange")
			self.horizontalLayout_4[i].addWidget(self.ResultRange[i], 0, QtCore.Qt.AlignTop)
			self.ResultText[i] = QtWidgets.QLabel(v[2])
			self.ResultText[i].setStyleSheet("min-width:200px;\nmin-height:20px;\npadding-left:5px;\nbackground-color: rgba(98, 98, 98, 10%);\nborder:2px;\nborder-radius:3px;\ncolor: rgb(54, 54, 54);\n")
			self.ResultText[i].setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
			self.ResultText[i].setWordWrap(True)
			self.ResultText[i].setObjectName("ResultText")
			self.horizontalLayout_4[i].addWidget(self.ResultText[i], 0, QtCore.Qt.AlignTop)
			self.ui.verticalLayout_5.addWidget(self.ResultWidget[i])
		SpacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
		self.ui.verticalLayout_5.addItem(SpacerItem)


	def ProcessInfo(self):
		self.ResultWidget = list(range(len(self.Info)))
		self.horizontalLayout_4 = list(range(len(self.Info)))
		self.ResultTag = list(range(len(self.Info)))
		self.ResultRange = list(range(len(self.Info)))
		self.ResultText = list(range(len(self.Info)))

	def clearLayout(self, layout):
		while layout.count():
			child = layout.takeAt(0)
			if child.widget():
				child.widget().deleteLater()

	def PatternChanged(self):
		self.clearLayout(self.ui.verticalLayout_5)
		self.Info = []
		self.Pattern = self.ui.RegexLineEdit.text()
		self.Process()
		self.ProcessInfo()
		self.UpdateInfo()
	def TestStringChanged(self):
		self.TestString = self.ui.TestStringTextEdit.toPlainText()

	def Sheet(self):
		os.system('python sheet.py')

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyWin()
	myapp.show()
	sys.exit(app.exec_())