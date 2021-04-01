# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(654, 524)
        self.display = QtWidgets.QLabel(Form)
        self.display.setGeometry(QtCore.QRect(30, 20, 601, 421))
        self.display.setScaledContents(True)
        self.display.setObjectName("display")
        self.back = QtWidgets.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(50, 470, 101, 31))
        self.back.setObjectName("back")
        self.frward = QtWidgets.QPushButton(Form)
        self.frward.setGeometry(QtCore.QRect(470, 470, 91, 31))
        self.frward.setObjectName("frward")
        self.result = QtWidgets.QLabel(Form)
        self.result.setGeometry(QtCore.QRect(200, 470, 231, 31))
        self.result.setObjectName("result")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.display.setText(_translate("Form", "Please load your files test folder!"))
        self.back.setText(_translate("Form", "Back"))
        self.frward.setText(_translate("Form", "Forward"))
        self.result.setText(_translate("Form", "Your class name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
