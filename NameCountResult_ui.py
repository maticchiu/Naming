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
        Form_NameCountResult.resize(617, 519)
        font = QtGui.QFont()
        font.setPointSize(9)
        Form_NameCountResult.setFont(font)
        self.textEdit_NameCountDescription = QtWidgets.QTextEdit(Form_NameCountResult)
        self.textEdit_NameCountDescription.setGeometry(QtCore.QRect(10, 10, 441, 501))
        self.textEdit_NameCountDescription.setObjectName("textEdit_NameCountDescription")
        self.pushButton_Remove = QtWidgets.QPushButton(Form_NameCountResult)
        self.pushButton_Remove.setGeometry(QtCore.QRect(550, 220, 51, 41))
        self.pushButton_Remove.setObjectName("pushButton_Remove")
        self.listWidget_SelectedNameCount = QtWidgets.QListWidget(Form_NameCountResult)
        self.listWidget_SelectedNameCount.setGeometry(QtCore.QRect(460, 30, 141, 181))
        self.listWidget_SelectedNameCount.setObjectName("listWidget_SelectedNameCount")
        self.label = QtWidgets.QLabel(Form_NameCountResult)
        self.label.setGeometry(QtCore.QRect(460, 0, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form_NameCountResult)
        self.label_2.setGeometry(QtCore.QRect(450, 280, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.listWidget_SuggestNameCount = QtWidgets.QListWidget(Form_NameCountResult)
        self.listWidget_SuggestNameCount.setGeometry(QtCore.QRect(460, 310, 141, 201))
        self.listWidget_SuggestNameCount.setStatusTip("")
        self.listWidget_SuggestNameCount.setObjectName("listWidget_SuggestNameCount")
        self.pushButton_Add = QtWidgets.QPushButton(Form_NameCountResult)
        self.pushButton_Add.setGeometry(QtCore.QRect(460, 240, 51, 41))
        self.pushButton_Add.setObjectName("pushButton_Add")

        self.retranslateUi(Form_NameCountResult)
        QtCore.QMetaObject.connectSlotsByName(Form_NameCountResult)

    def retranslateUi(self, Form_NameCountResult):
        _translate = QtCore.QCoreApplication.translate
        Form_NameCountResult.setWindowTitle(_translate("Form_NameCountResult", "Name Count Result"))
        self.pushButton_Remove.setText(_translate("Form_NameCountResult", "Remove"))
        self.listWidget_SelectedNameCount.setToolTip(_translate("Form_NameCountResult", "<html><head/><body><p><span style=\" font-size:12pt;\">1. Press &quot;Remove&quot; button to remove selected item</span></p><p><span style=\" font-size:12pt;\">2. Click to show single name count description</span></p><p><span style=\" font-size:12pt;\">3. Double click to show all selected name count descriptions</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>"))
        self.label.setText(_translate("Form_NameCountResult", "Selected Name Count"))
        self.label_2.setText(_translate("Form_NameCountResult", "Suggest Name Count"))
        self.listWidget_SuggestNameCount.setToolTip(_translate("Form_NameCountResult", "<html><head/><body><p><span style=\" font-size:12pt;\">1. Press &quot;Add&quot; button to add name count</span></p><p><span style=\" font-size:12pt;\">2. Click to show single name count description</span></p><p><span style=\" font-size:12pt;\">3. Double click to show all selected name count descriptions</span></p></body></html>"))
        self.pushButton_Add.setText(_translate("Form_NameCountResult", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_NameCountResult = QtWidgets.QWidget()
    ui = Ui_Form_NameCountResult()
    ui.setupUi(Form_NameCountResult)
    Form_NameCountResult.show()
    sys.exit(app.exec_())
