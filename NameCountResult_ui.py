# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NameCountResult.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_NameCountResult(object):
    def setupUi(self, Form_NameCountResult):
        Form_NameCountResult.setObjectName("Form_NameCountResult")
        Form_NameCountResult.resize(726, 519)
        font = QtGui.QFont()
        font.setPointSize(9)
        Form_NameCountResult.setFont(font)
        self.textEdit_NameCountDescription = QtWidgets.QTextEdit(Form_NameCountResult)
        self.textEdit_NameCountDescription.setGeometry(QtCore.QRect(10, 10, 441, 501))
        self.textEdit_NameCountDescription.setObjectName("textEdit_NameCountDescription")
        self.listWidget_NameCount = QtWidgets.QListWidget(Form_NameCountResult)
        self.listWidget_NameCount.setGeometry(QtCore.QRect(466, 10, 256, 441))
        self.listWidget_NameCount.setObjectName("listWidget_NameCount")
        self.pushButton_Remove = QtWidgets.QPushButton(Form_NameCountResult)
        self.pushButton_Remove.setGeometry(QtCore.QRect(630, 460, 91, 51))
        self.pushButton_Remove.setObjectName("pushButton_Remove")

        self.retranslateUi(Form_NameCountResult)
        QtCore.QMetaObject.connectSlotsByName(Form_NameCountResult)

    def retranslateUi(self, Form_NameCountResult):
        _translate = QtCore.QCoreApplication.translate
        Form_NameCountResult.setWindowTitle(_translate("Form_NameCountResult", "Name Count Result"))
        self.pushButton_Remove.setText(_translate("Form_NameCountResult", "Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_NameCountResult = QtWidgets.QWidget()
    ui = Ui_Form_NameCountResult()
    ui.setupUi(Form_NameCountResult)
    Form_NameCountResult.show()
    sys.exit(app.exec_())
