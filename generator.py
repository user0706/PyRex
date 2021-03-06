# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generator.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CodeGenerator(object):
    def setupUi(self, CodeGenerator):
        CodeGenerator.setObjectName("CodeGenerator")
        CodeGenerator.resize(800, 333)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CodeGenerator.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CodeGenerator)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet("border-bottom: 2px;\n"
"border-style: solid;\n"
"border-bottom-color: rgb(255, 85, 0);")
        self.textEdit.setLineWidth(1)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.CopyPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.CopyPushButton.setStyleSheet("QPushButton#CopyPushButton {\n"
"    min-width:60px;\n"
"    max-width:60px;\n"
"    min-height:35;\n"
"    max-height:35;\n"
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
"QPushButton#CopyPushButton:hover {\n"
"    background:  rgba(255,255,255,50%);\n"
"    border-bottom-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton#CopyPushButton:pressed {\n"
"    background:  rgba(255,255,255,100%);\n"
"    border-bottom-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton#CopyPushButton:disabled {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15); \n"
"}")
        self.CopyPushButton.setObjectName("CopyPushButton")
        self.horizontalLayout.addWidget(self.CopyPushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ClosePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClosePushButton.setStyleSheet("QPushButton#ClosePushButton {\n"
"    min-width:60px;\n"
"    max-width:60px;\n"
"    min-height:35;\n"
"    max-height:35;\n"
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
"QPushButton#ClosePushButton:hover {\n"
"    background:  rgba(255,255,255,50%);\n"
"    border-bottom-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton#ClosePushButton:pressed {\n"
"    background:  rgba(255,255,255,100%);\n"
"    border-bottom-color:rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton#ClosePushButton:disabled {\n"
"    background:  rgba(0,0,0,.04);\n"
"    border-bottom-color: rgba(0,0,0,.15); \n"
"}")
        self.ClosePushButton.setObjectName("ClosePushButton")
        self.horizontalLayout.addWidget(self.ClosePushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        CodeGenerator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CodeGenerator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        CodeGenerator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CodeGenerator)
        self.statusbar.setObjectName("statusbar")
        CodeGenerator.setStatusBar(self.statusbar)

        self.retranslateUi(CodeGenerator)
        self.ClosePushButton.clicked.connect(CodeGenerator.close)
        self.CopyPushButton.clicked.connect(self.textEdit.selectAll)
        self.CopyPushButton.clicked.connect(self.textEdit.copy)
        QtCore.QMetaObject.connectSlotsByName(CodeGenerator)

    def retranslateUi(self, CodeGenerator):
        _translate = QtCore.QCoreApplication.translate
        CodeGenerator.setWindowTitle(_translate("CodeGenerator", "PyRex Code Generaotr"))
        self.textEdit.setHtml(_translate("CodeGenerator", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">import re</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">regex = r&quot;&lt;CHANGE_ME&gt;pattern&lt;CHANGE_ME&gt;&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">test_str = &quot;&lt;CHANGE_ME&gt;string&lt;CHANGE_ME&gt;&quot;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">matches = re.finditer(regex, test_str, re.MULTILINE)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">for matchNum, match in enumerate(matches, start=1):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    print (&quot;Match {matchNum} was found at {start}-{end}: {match}&quot;.format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    for groupNum in range(0, len(match.groups())):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">        groupNum = groupNum + 1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">        print (&quot;Group {groupNum} found at {start}-{end}: {group}&quot;.format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))</span></p></body></html>"))
        self.CopyPushButton.setText(_translate("CodeGenerator", "Copy"))
        self.ClosePushButton.setText(_translate("CodeGenerator", "Close"))
import src_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CodeGenerator = QtWidgets.QMainWindow()
    ui = Ui_CodeGenerator()
    ui.setupUi(CodeGenerator)
    CodeGenerator.show()
    sys.exit(app.exec_())
