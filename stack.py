# Form implementation generated from reading ui file 'stack.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(382, 564)
        self.add = QtWidgets.QPushButton(Dialog)
        self.add.setGeometry(QtCore.QRect(285, 215, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.add.setFont(font)
        self.add.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.add.setStyleSheet("QPushButton{\n"
"background-color:rgb(240,123,44);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}")
        self.add.setObjectName("add")
        self.sub = QtWidgets.QPushButton(Dialog)
        self.sub.setGeometry(QtCore.QRect(285, 300, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.sub.setFont(font)
        self.sub.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sub.setStyleSheet("QPushButton{\n"
"background-color:rgb(240,123,44);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}")
        self.sub.setObjectName("sub")
        self.mul = QtWidgets.QPushButton(Dialog)
        self.mul.setGeometry(QtCore.QRect(285, 385, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(36)
        self.mul.setFont(font)
        self.mul.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.mul.setStyleSheet("QPushButton{\n"
"background-color:rgb(240,123,44);\n"
"color:black;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}\n"
"")
        self.mul.setObjectName("mul")
        self.div = QtWidgets.QPushButton(Dialog)
        self.div.setGeometry(QtCore.QRect(285, 470, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.div.setFont(font)
        self.div.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.div.setStyleSheet("QPushButton{\n"
"background-color:rgb(240,123,44);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}")
        self.div.setObjectName("div")
        self.equal = QtWidgets.QPushButton(Dialog)
        self.equal.setGeometry(QtCore.QRect(200, 470, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.equal.setFont(font)
        self.equal.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.equal.setStyleSheet("QPushButton{\n"
"background-color:rgb(240,123,44);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}")
        self.equal.setObjectName("equal")
        self.rightbrack = QtWidgets.QPushButton(Dialog)
        self.rightbrack.setGeometry(QtCore.QRect(115, 130, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.rightbrack.setFont(font)
        self.rightbrack.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.rightbrack.setStyleSheet("QPushButton{\n"
"background-color:rgb(98,86,86);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}\n"
"")
        self.rightbrack.setObjectName("rightbrack")
        self.dele = QtWidgets.QPushButton(Dialog)
        self.dele.setGeometry(QtCore.QRect(200, 130, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.dele.setFont(font)
        self.dele.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.dele.setStyleSheet("QPushButton{\n"
"background-color:rgb(98,86,86);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}\n"
"")
        self.dele.setObjectName("dele")
        self.leftbrack = QtWidgets.QPushButton(Dialog)
        self.leftbrack.setGeometry(QtCore.QRect(30, 130, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.leftbrack.setFont(font)
        self.leftbrack.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.leftbrack.setStyleSheet("QPushButton{\n"
"background-color:rgb(98,86,86);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}\n"
"\n"
"")
        self.leftbrack.setObjectName("leftbrack")
        self.ac = QtWidgets.QPushButton(Dialog)
        self.ac.setGeometry(QtCore.QRect(285, 130, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.ac.setFont(font)
        self.ac.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ac.setStyleSheet("QPushButton{\n"
"background-color:rgb(98,86,86);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}\n"
"")
        self.ac.setObjectName("ac")
        self.dot = QtWidgets.QPushButton(Dialog)
        self.dot.setGeometry(QtCore.QRect(115, 470, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.dot.setFont(font)
        self.dot.setStyleSheet("QPushButton{\n"
"background-color:rgb(28,23,26);\n"
"color:white;\n"
"border-radius:35px;\n"
"}")
        self.dot.setObjectName("dot")
        self.btn0 = QtWidgets.QPushButton(Dialog)
        self.btn0.setGeometry(QtCore.QRect(30, 470, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn0.setFont(font)
        self.btn0.setStyleSheet("QPushButton{\n"
"background-color:rgb(28,23,26);\n"
"color:white;\n"
"border-radius:35px;\n"
"}")
        self.btn0.setObjectName("btn0")
        self.btn7 = QtWidgets.QPushButton(Dialog)
        self.btn7.setGeometry(QtCore.QRect(30, 385, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn7.setFont(font)
        self.btn7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn7.setStyleSheet("QPushButton{\n"
"background-color:rgb(28,23,26);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}")
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(Dialog)
        self.btn8.setGeometry(QtCore.QRect(115, 385, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn8.setFont(font)
        self.btn8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn8.setStyleSheet("QPushButton{\n"
"background-color:rgb(28,23,26);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}")
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(Dialog)
        self.btn9.setGeometry(QtCore.QRect(200, 385, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn9.setFont(font)
        self.btn9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn9.setStyleSheet("QPushButton{\n"
"background-color:rgb(28,23,26);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}")
        self.btn9.setObjectName("btn9")
        self.btn4 = QtWidgets.QPushButton(Dialog)
        self.btn4.setGeometry(QtCore.QRect(30, 300, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn4.setFont(font)
        self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn4.setStyleSheet("QPushButton{\n"
"background-color:rgb(28,23,26);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}")
        self.btn4.setObjectName("btn4")
        self.btn6 = QtWidgets.QPushButton(Dialog)
        self.btn6.setGeometry(QtCore.QRect(200, 300, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn6.setFont(font)
        self.btn6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn6.setStyleSheet("QPushButton{\n"
"background-color:rgb(28,23,26);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}")
        self.btn6.setObjectName("btn6")
        self.btn5 = QtWidgets.QPushButton(Dialog)
        self.btn5.setGeometry(QtCore.QRect(115, 300, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn5.setFont(font)
        self.btn5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn5.setStyleSheet("QPushButton{\n"
"background-color:rgb(28,23,26);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}")
        self.btn5.setObjectName("btn5")
        self.btn1 = QtWidgets.QPushButton(Dialog)
        self.btn1.setGeometry(QtCore.QRect(30, 215, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn1.setFont(font)
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn1.setMouseTracking(True)
        self.btn1.setStyleSheet("QPushButton{\n"
"background-color:rgb(28,23,26);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}")
        self.btn1.setObjectName("btn1")
        self.btn3 = QtWidgets.QPushButton(Dialog)
        self.btn3.setGeometry(QtCore.QRect(200, 215, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn3.setFont(font)
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn3.setStyleSheet("QPushButton{\n"
"background-color:rgb(28,23,26);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}")
        self.btn3.setObjectName("btn3")
        self.btn2 = QtWidgets.QPushButton(Dialog)
        self.btn2.setGeometry(QtCore.QRect(115, 215, 70, 70))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn2.setFont(font)
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn2.setStyleSheet("QPushButton{\n"
"background-color:rgb(28,23,26);\n"
"color:white;\n"
"border-radius:35px;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/\n"
"background-color:rgb(122,105,97);\n"
"}\n"
"QPushButton:pressed{/*鼠标按下*/\n"
"background-color:rgb(122,105,97);\n"
"border:2px black;\n"
"border-style:outset;\n"
"}")
        self.btn2.setObjectName("btn2")
        self.display = QtWidgets.QTextEdit(Dialog)
        self.display.setGeometry(QtCore.QRect(30, 20, 241, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(48)
        font.setItalic(False)
        self.display.setFont(font)
        self.display.setObjectName("display")
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(285, 30, 70, 51))
        self.exit.setCheckable(False)
        self.exit.setObjectName("exit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add.setText(_translate("Dialog", "➕"))
        self.sub.setText(_translate("Dialog", "➖"))
        self.mul.setText(_translate("Dialog", "X"))
        self.div.setText(_translate("Dialog", "➗"))
        self.equal.setText(_translate("Dialog", "🟰"))
        self.rightbrack.setText(_translate("Dialog", ")"))
        self.dele.setText(_translate("Dialog", "DEL"))
        self.leftbrack.setText(_translate("Dialog", "("))
        self.ac.setText(_translate("Dialog", "AC"))
        self.dot.setText(_translate("Dialog", "."))
        self.btn0.setText(_translate("Dialog", "0"))
        self.btn7.setText(_translate("Dialog", "7"))
        self.btn8.setText(_translate("Dialog", "8"))
        self.btn9.setText(_translate("Dialog", "9"))
        self.btn4.setText(_translate("Dialog", "4"))
        self.btn6.setText(_translate("Dialog", "6"))
        self.btn5.setText(_translate("Dialog", "5"))
        self.btn1.setText(_translate("Dialog", "1"))
        self.btn3.setText(_translate("Dialog", "3"))
        self.btn2.setText(_translate("Dialog", "2"))
        self.display.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Trebuchet MS\'; font-size:48pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.exit.setText(_translate("Dialog", "退出"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())