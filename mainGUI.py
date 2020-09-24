# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/windowIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setStyleSheet("background-color:rgb(255, 85, 0);\n"
"min-height:40;\n"
"max-height:40;")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Logo = QtWidgets.QLabel(self.horizontalFrame)
        self.Logo.setStyleSheet("min-width:30px;\n"
"max-width:30px;\n"
"min-height:30px;\n"
"max-height:30px;")
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap(":/icons/icons/logo.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.horizontalLayout.addWidget(self.Logo, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.CodeGeneratorPushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.CodeGeneratorPushButton.setMinimumSize(QtCore.QSize(27, 27))
        self.CodeGeneratorPushButton.setMaximumSize(QtCore.QSize(27, 27))
        self.CodeGeneratorPushButton.setStyleSheet("QPushButton#CodeGeneratorPushButton {\n"
"    min-width: 25px;\n"
"    max-width: 25px;\n"
"    min-height: 25px;\n"
"    max-height: 25px;\n"
"    background-color: rgba(255, 255, 255, 0%);\n"
"    \n"
"    border:1px;\n"
"    border-color: rgb(255, 85, 0);\n"
"    border-style: solid;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius:5px;\n"
"}\n"
"\n"
"QPushButton#CodeGeneratorPushButton:hover {\n"
"    background:  rgb(255, 119, 51);\n"
"}\n"
"\n"
"QPushButton#CodeGeneratorPushButton:pressed {\n"
"    background: rgba(255, 255, 255, 0%);\n"
"}")
        self.CodeGeneratorPushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/code.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CodeGeneratorPushButton.setIcon(icon1)
        self.CodeGeneratorPushButton.setIconSize(QtCore.QSize(25, 25))
        self.CodeGeneratorPushButton.setObjectName("CodeGeneratorPushButton")
        self.horizontalLayout.addWidget(self.CodeGeneratorPushButton)
        self.RegexSheetPushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.RegexSheetPushButton.setMinimumSize(QtCore.QSize(27, 27))
        self.RegexSheetPushButton.setMaximumSize(QtCore.QSize(27, 27))
        self.RegexSheetPushButton.setStyleSheet("QPushButton#RegexSheetPushButton {\n"
"    min-width: 25px;\n"
"    max-width: 25px;\n"
"    min-height: 25px;\n"
"    max-height: 25px;\n"
"    background-color: rgba(255, 255, 255, 0%);\n"
"    \n"
"    border:1px;\n"
"    border-color: rgb(255, 85, 0);\n"
"    border-style: solid;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius:5px;\n"
"}\n"
"\n"
"QPushButton#RegexSheetPushButton:hover {\n"
"    background:  rgb(255, 119, 51);\n"
"}\n"
"\n"
"QPushButton#RegexSheetPushButton:pressed {\n"
"    background: rgba(255, 255, 255, 0%);\n"
"}")
        self.RegexSheetPushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/sheet.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RegexSheetPushButton.setIcon(icon2)
        self.RegexSheetPushButton.setIconSize(QtCore.QSize(25, 25))
        self.RegexSheetPushButton.setObjectName("RegexSheetPushButton")
        self.horizontalLayout.addWidget(self.RegexSheetPushButton)
        self.AboutPushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.AboutPushButton.setMinimumSize(QtCore.QSize(27, 27))
        self.AboutPushButton.setMaximumSize(QtCore.QSize(27, 27))
        self.AboutPushButton.setStyleSheet("QPushButton#AboutPushButton {\n"
"    min-width: 25px;\n"
"    max-width: 25px;\n"
"    min-height: 25px;\n"
"    max-height: 25px;\n"
"    background-color: rgba(255, 255, 255, 0%);\n"
"    \n"
"    border:1px;\n"
"    border-color: rgb(255, 85, 0);\n"
"    border-style: solid;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius:5px;\n"
"}\n"
"\n"
"QPushButton#AboutPushButton:hover {\n"
"    background:  rgb(255, 119, 51);\n"
"}\n"
"\n"
"QPushButton#AboutPushButton:pressed {\n"
"    background: rgba(255, 255, 255, 0%);\n"
"}")
        self.AboutPushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AboutPushButton.setIcon(icon3)
        self.AboutPushButton.setIconSize(QtCore.QSize(25, 25))
        self.AboutPushButton.setObjectName("AboutPushButton")
        self.horizontalLayout.addWidget(self.AboutPushButton)
        self.verticalLayout.addWidget(self.horizontalFrame, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("min-height:15;\n"
"max-height:15;\n"
"background-color: rgba(0, 0, 0, 0%);")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.RegexLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.RegexLineEdit.setFont(font)
        self.RegexLineEdit.setStyleSheet("QLineEdit {\n"
"    min-width:360px;\n"
"    min-height:30;\n"
"    margin-bottom:5px;\n"
"    \n"
"    padding-left: 5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(255,255,255,100%);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit::focus    {\n"
"    border-bottom-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QLineEdit::disabled    {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15);\n"
"}")
        self.RegexLineEdit.setObjectName("RegexLineEdit")
        self.horizontalLayout_3.addWidget(self.RegexLineEdit)
        self.ProcessPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ProcessPushButton.setStyleSheet("QPushButton#ProcessPushButton {\n"
"    min-width:60px;\n"
"    max-width:60px;\n"
"    min-height:30;\n"
"    margin-bottom:5px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(255,255,255,100%);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#ProcessPushButton:hover {\n"
"    background:  rgba(255,255,255,50%);\n"
"    border-bottom-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton#ProcessPushButton:pressed {\n"
"    background:  rgba(255,255,255,100%);\n"
"    border-bottom-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton#ProcessPushButton:disabled {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15); \n"
"}")
        self.ProcessPushButton.setObjectName("ProcessPushButton")
        self.horizontalLayout_3.addWidget(self.ProcessPushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("min-height:15;\n"
"max-height:15;\n"
"background-color: rgba(0, 0, 0, 0%);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.TestStringTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TestStringTextEdit.setFont(font)
        self.TestStringTextEdit.setStyleSheet("QPlainTextEdit {\n"
"    min-width:360px;\n"
"    min-height:30;\n"
"    \n"
"    padding-left: 5px;\n"
"    padding-top: 10px;\n"
"\n"
"    color: #495057;\n"
"\n"
"    background:  rgba(255,255,255,100%);\n"
"    border-bottom: 2px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgba(0,0,0,.3);\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"\n"
"QPlainTextEdit::focus    {\n"
"    border-bottom-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPlainTextEdit::disabled    {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15);\n"
"}")
        self.TestStringTextEdit.setObjectName("TestStringTextEdit")
        self.verticalLayout_4.addWidget(self.TestStringTextEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setStyleSheet("background-color: rgb(238, 238, 238);\n"
"min-width: 300;\n"
"max-width: 500;")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.verticalFrame)
        self.widget.setStyleSheet("background-color:rgb(249, 249, 249)")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("min-height:15;\n"
"max-height:15;\n"
"background-color: rgba(0, 0, 0, 0%);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.RresultScrollArea = QtWidgets.QScrollArea(self.widget)
        self.RresultScrollArea.setStyleSheet("border:No;")
        self.RresultScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RresultScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.RresultScrollArea.setWidgetResizable(True)
        self.RresultScrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.RresultScrollArea.setObjectName("RresultScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 300, 449))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.RresultScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.RresultScrollArea)
        self.verticalLayout_2.addWidget(self.widget)
        self.horizontalLayout_2.addWidget(self.verticalFrame)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyRex"))
        self.label.setText(_translate("MainWindow", "REGULAR EXPRESSION"))
        self.ProcessPushButton.setText(_translate("MainWindow", "Process"))
        self.ProcessPushButton.setShortcut(_translate("MainWindow", "Return"))
        self.label_2.setText(_translate("MainWindow", "TEST STRING"))
        self.TestStringTextEdit.setPlaceholderText(_translate("MainWindow", "insert your test string here"))
        self.label_3.setText(_translate("MainWindow", "REGULAR EXPRESSION"))
import src_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
