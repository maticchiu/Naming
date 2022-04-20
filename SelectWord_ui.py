# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectWord.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_SelectWord(object):
    def setupUi(self, Form_SelectWord):
        Form_SelectWord.setObjectName("Form_SelectWord")
        Form_SelectWord.resize(400, 712)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form_SelectWord.setFont(font)
        self.groupBox_2 = QtWidgets.QGroupBox(Form_SelectWord)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 371, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 331, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_SelectWord_Gold = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_SelectWord_Gold.setChecked(True)
        self.checkBox_SelectWord_Gold.setObjectName("checkBox_SelectWord_Gold")
        self.horizontalLayout.addWidget(self.checkBox_SelectWord_Gold)
        self.checkBox_SelectWord_Wood = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_SelectWord_Wood.setObjectName("checkBox_SelectWord_Wood")
        self.horizontalLayout.addWidget(self.checkBox_SelectWord_Wood)
        self.checkBox_SelectWord_Water = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_SelectWord_Water.setChecked(True)
        self.checkBox_SelectWord_Water.setObjectName("checkBox_SelectWord_Water")
        self.horizontalLayout.addWidget(self.checkBox_SelectWord_Water)
        self.checkBox_SelectWord_Fire = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_SelectWord_Fire.setObjectName("checkBox_SelectWord_Fire")
        self.horizontalLayout.addWidget(self.checkBox_SelectWord_Fire)
        self.checkBox_SelectWord_Earth = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_SelectWord_Earth.setChecked(True)
        self.checkBox_SelectWord_Earth.setObjectName("checkBox_SelectWord_Earth")
        self.horizontalLayout.addWidget(self.checkBox_SelectWord_Earth)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(60, 70, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox_NameCount = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_NameCount.setGeometry(QtCore.QRect(100, 70, 61, 41))
        self.comboBox_NameCount.setObjectName("comboBox_NameCount")
        self.pushButton_ListWord = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_ListWord.setGeometry(QtCore.QRect(210, 70, 91, 41))
        self.pushButton_ListWord.setObjectName("pushButton_ListWord")
        self.listWidget_WordList = QtWidgets.QListWidget(Form_SelectWord)
        self.listWidget_WordList.setGeometry(QtCore.QRect(10, 140, 131, 561))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_WordList.setFont(font)
        self.listWidget_WordList.setObjectName("listWidget_WordList")
        self.pushButton_AddWord = QtWidgets.QPushButton(Form_SelectWord)
        self.pushButton_AddWord.setGeometry(QtCore.QRect(160, 200, 71, 51))
        self.pushButton_AddWord.setObjectName("pushButton_AddWord")
        self.pushButton_RemoveWord = QtWidgets.QPushButton(Form_SelectWord)
        self.pushButton_RemoveWord.setGeometry(QtCore.QRect(160, 550, 71, 51))
        self.pushButton_RemoveWord.setObjectName("pushButton_RemoveWord")
        self.listWidget_SelectedWord = QtWidgets.QListWidget(Form_SelectWord)
        self.listWidget_SelectedWord.setGeometry(QtCore.QRect(250, 140, 131, 561))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_SelectedWord.setFont(font)
        self.listWidget_SelectedWord.setObjectName("listWidget_SelectedWord")

        self.retranslateUi(Form_SelectWord)
        QtCore.QMetaObject.connectSlotsByName(Form_SelectWord)

    def retranslateUi(self, Form_SelectWord):
        _translate = QtCore.QCoreApplication.translate
        Form_SelectWord.setWindowTitle(_translate("Form_SelectWord", "Select Words"))
        self.groupBox_2.setTitle(_translate("Form_SelectWord", "選取喜歡的字"))
        self.checkBox_SelectWord_Gold.setText(_translate("Form_SelectWord", "金"))
        self.checkBox_SelectWord_Wood.setText(_translate("Form_SelectWord", "木"))
        self.checkBox_SelectWord_Water.setText(_translate("Form_SelectWord", "水"))
        self.checkBox_SelectWord_Fire.setText(_translate("Form_SelectWord", "火"))
        self.checkBox_SelectWord_Earth.setText(_translate("Form_SelectWord", "土"))
        self.label_10.setText(_translate("Form_SelectWord", "筆劃"))
        self.pushButton_ListWord.setText(_translate("Form_SelectWord", "設定"))
        self.pushButton_AddWord.setText(_translate("Form_SelectWord", "Add ->"))
        self.pushButton_RemoveWord.setText(_translate("Form_SelectWord", "Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_SelectWord = QtWidgets.QWidget()
    ui = Ui_Form_SelectWord()
    ui.setupUi(Form_SelectWord)
    Form_SelectWord.show()
    sys.exit(app.exec_())
