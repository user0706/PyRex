from mainGUI import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
import sys

import re
import random

def Process(string, pattern, info):
	'''Processes the specified regex pattern

	:param pattern: Regex pattern
	:type pattern: str
	:param string: Test string
	:type string: str
	:returns info: Search result information
	:type info: list

	:Example:	string 	=> 	"HELLO world
							Great day"
				pattern =>	[A-Z]+.*
				info	=>	[]

		return	info	=>	[["Full match 1", "[0-10]", "HELLO world"]]					
	'''
	if pattern:
		try:
			regex = r"{}".format(str(pattern))
			matches = re.finditer(regex, string, re.MULTILINE)
			for match_num, match in enumerate(matches, start=1):
				info.append(['Full match '+str(match_num), str(match.start())+'-'+str(match.end()), str(match.group())])
				for group_num in range(0, len(match.groups())):
					group_num = group_num + 1
					info.append(['Group '+str(group_num), str(match.start(group_num))+'-'+str(match.end(group_num)), str(match.group(group_num))])
		except:
			pass
	return info

def GenerateGroupColor(color_spectrum, target):
	'''Color generator for groups

	:param target: Result info group name
	:type target: str
	:param color_spectrum: List of optional colors
	:type color_spectrum: list
	:returns: Selected rgb color
	:type: str
	'''
	if target == 'Group 1':
		color = color_spectrum[1]
	elif target == 'Group 2':
		color = color_spectrum[2]
	elif target == 'Group 3':
		color = color_spectrum[3]
	elif target == 'Group 4':
		color = color_spectrum[4]
	elif target == 'Group 5':
		color = color_spectrum[5]
	elif target == 'Group 6':
		color = color_spectrum[6]
	elif target == 'Group 7':
		color = color_spectrum[7]
	elif target == 'Group 8':
		color = color_spectrum[8]
	elif target == 'Group 9':
		color = color_spectrum[9]
	elif target == 'Group 10':
		color = color_spectrum[10]
	else:
		color = random.choice(color_spectrum)
	return color

def FullMatchTagUI(scroll_area, layout, tag):
	'''Full match tag header - The dynamic part of Qt ui
	
	:param scroll_area: QT ui scroll area
	:type: PyQt5.QtWidgets.QScrollArea
	:param layout: QT ui scroll area layout
	:type: PyQt5.QtWidgets.QHBoxLayout
	'''
	CollectionWidget = QtWidgets.QWidget(scroll_area)
	CollectionWidget.setMinimumSize(QtCore.QSize(300, 25))
	CollectionWidget.setMaximumSize(QtCore.QSize(500, 25))
	CollectionWidget.setObjectName("CollectionWidget")
	verticalLayout_6 = QtWidgets.QVBoxLayout(CollectionWidget)
	verticalLayout_6.setContentsMargins(0, 0, 0, 0)
	verticalLayout_6.setSpacing(0)
	verticalLayout_6.setObjectName("verticalLayout_6")
	CollectionLabel = QtWidgets.QLabel("Match {}".format(str(tag.split(' ')[-1])))
	font = QtGui.QFont()
	font.setPointSize(8)
	font.setBold(True)
	CollectionLabel.setFont(font)
	CollectionLabel.setStyleSheet("color: rgb(78, 123, 179);\nmargin-bottom:5px;\nmargin-top:10px;")
	CollectionLabel.setObjectName("CollectionLabel")
	verticalLayout_6.addWidget(CollectionLabel)
	CollectionLine = QtWidgets.QFrame(CollectionWidget)
	CollectionLine.setStyleSheet("background-color: rgba(199, 199, 199, 50%);\nmin-height:1px;\nmax-height:1px;")
	CollectionLine.setFrameShape(QtWidgets.QFrame.HLine)
	CollectionLine.setFrameShadow(QtWidgets.QFrame.Sunken)
	CollectionLine.setObjectName("CollectionLine")
	verticalLayout_6.addWidget(CollectionLine)
	layout.addWidget(CollectionWidget)

def InfoUI(res_widget, res_layout, res_tag, res_range, res_text, res_index, res_color, scroll_area, layout, tag):
	'''UI information widget element - The dynamic part of Qt ui

	:param res_widget: A list where the i-th element is the i-th Qt widget
	:type res_widget: list
	:param res_layout: A list where the i-th element is the i-th Qt H layout
	:type res_layout: list
	:param res_tag: A list where the i-th element is the i-th tag
	:type res_tag: list
	:param res_range: A list where the i-th element is the i-th range
	:type res_range: list
	:param res_text: A list where the i-th element is the i-th text
	:type res_text: list
	:param res_index: Current element-widget
	:type res_index: int
	:param res_color: Tag background color
	:type res_color: str
	:param scroll_area: Qt ui scroll area
	:type scroll_area: PyQt5.QtWidgets.QScrollArea
	:param layout: Qt ui scroll area layout
	:type layout: PyQt5.QtWidgets.QHBoxLayout
	:param tag: Tag name
	:type tag: str
	'''
	res_widget[res_index] = QtWidgets.QWidget(scroll_area)
	res_widget[res_index].setObjectName("ResultWidget")
	res_layout[res_index] = QtWidgets.QHBoxLayout(res_widget[res_index])
	res_layout[res_index].setContentsMargins(0, 7, 0, 0)
	res_layout[res_index].setObjectName("horizontalLayout_4")
	if 'Full match' in tag[0]:
		res_tag[res_index] = QtWidgets.QLabel(' '.join(tag[0].split(' ')[:-1]))
	else:
		res_tag[res_index] = QtWidgets.QLabel(tag[0])
	res_tag[res_index].setStyleSheet("min-width:60px;\nmax-width:60px;\nmin-height:20px;\nmax-height:20px;\nbackground-color: {};\nborder:2px;\nborder-radius:3px;\ncolor:  rgb(54, 54, 54);\n".format(res_color))
	res_tag[res_index].setAlignment(QtCore.Qt.AlignCenter)
	res_tag[res_index].setObjectName("ResultTag")
	res_layout[res_index].addWidget(res_tag[res_index], 0, QtCore.Qt.AlignTop)
	res_range[res_index] = QtWidgets.QLabel(tag[1])
	res_range[res_index].setStyleSheet("min-width:60px;\nmax-width:60px;\nmin-height:20px;\nmax-height:20px;\ncolor: rgb(54, 54, 54);\n")
	res_range[res_index].setAlignment(QtCore.Qt.AlignCenter)
	res_range[res_index].setWordWrap(True)
	res_range[res_index].setObjectName("ResultRange")
	res_layout[res_index].addWidget(res_range[res_index], 0, QtCore.Qt.AlignTop)
	res_text[res_index] = QtWidgets.QLabel(tag[2])
	res_text[res_index].setStyleSheet("min-width:200px;\nmin-height:20px;\npadding-left:5px;\nbackground-color: rgba(98, 98, 98, 10%);\nborder:2px;\nborder-radius:3px;\ncolor: rgb(54, 54, 54);\n")
	res_text[res_index].setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
	res_text[res_index].setWordWrap(True)
	res_text[res_index].setObjectName("ResultText")
	res_layout[res_index].addWidget(res_text[res_index], 0, QtCore.Qt.AlignTop)
	layout.addWidget(res_widget[res_index])

def PreprocessInfo(info):
	'''Define the length of the list of variables for those used in UpdateInfo

	:return res_widget: list with the same length as info parameter
	:rtype res_widget: list
	:return res_layout: list with the same length as info parameter
	:rtype res_layout: list
	:return res_tag: list with the same length as info parameter
	:rtype res_tag: list
	:return res_range: list with the same length as info parameter
	:rtype res_range: list
	:return res_text: list with the same length as info parameter
	:rtype res_text: list
	'''
	res_widget = list(range(len(info)))
	res_layout = list(range(len(info)))
	res_tag = list(range(len(info)))
	res_range = list(range(len(info)))
	res_text = list(range(len(info)))
	return res_widget, res_layout, res_tag, res_range, res_text

def clearLayout(layout):
	'''Cleaning the previous state of Layout

	:param layout: Layout to be cleaned
	:type layout: PyQt5.QtWidgets.QHBoxLayout
	'''
	while layout.count():
		child = layout.takeAt(0)
		if child.widget():
			child.widget().deleteLater()

def Highlight(plain_edit, color, start, end):
	'''Highlights/marks the appropriate substring of the test string
	
	:param plain_edit: Plain edit component. NOT text from plain edit
	:type plain_edit: PyQt5.QtWidgets.QPlainTextEdit
	:param color: Matching color for the background of the corresponding group - tag result
	:type color: str
	:param start: Starting position/index of substring for marking.
	:type start: int
	:param end: Ending position/index of substring for marking.
	:type end: int
	'''
	fmt = QTextCharFormat()
	fmt.setBackground(color)
	cursor = QTextCursor(plain_edit.document())
	cursor.setPosition(start, QTextCursor.MoveAnchor)
	cursor.setPosition(end, QTextCursor.KeepAnchor)
	cursor.setCharFormat(fmt)

def ClearHighlight(plain_edit, plain_edit_text):
	'''Reset all highlighted/marked substrings from the test string

	:param plain_edit: Plain edit component. NOT text from plain edit
	:type plain_edit: PyQt5.QtWidgets.QPlainTextEdit
	:param plain_edit_text: Text from plaind edit
	:type plain_edit_text: str
	'''
	fmt = QTextCharFormat()
	fmt.setBackground(QColor(Qt.white))
	cursor = QTextCursor(plain_edit.document())
	cursor.setPosition(0, QTextCursor.MoveAnchor)
	cursor.setPosition(len(list(plain_edit_text)), QTextCursor.KeepAnchor)
	cursor.setCharFormat(fmt)

def HighlightRange(string):
	'''Convert a range from a string type to a list of integers
	
	:param string: The range of substring to be highlighted
	:type string: str
	:return : The range of substring to be highlighted
	:rtype : list

	:Example:	string	=>	"[2-9]"
		return			=>	[2,9]
	'''
	return [int(re.sub(r'(\[|\])','',i)) for i in string.split('-')]

def strColorTolist(string):
	'''Convert string type rgb colors to separate integer values of red - green - blue

	:param string: Rgb color as a string
	:type string: str
	:return colorList[0]: Red value
	:rtype colorList[0]: int
	:return colorList[1]: Green value
	:rtype colorList[1]: int
	:return colorList[2]: Blue value
	:rtype colorList[2]: int

	:Example:	string			=>	"rgb(255,100,50)"
		return	colorList[0]	=>	255
		return	colorList[1]	=>	100
		return	colorList[2]	=>	50
	'''
	colorList = [int(i) for i in re.sub(r'(rgb\(|\))','',string).split(', ')]
	return colorList[0],colorList[1],colorList[2]