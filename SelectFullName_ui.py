# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectFullName.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_SelectFullName(object):
    def setupUi(self, Form_SelectFullName):
        Form_SelectFullName.setObjectName("Form_SelectFullName")
        Form_SelectFullName.resize(717, 305)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form_SelectFullName.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(Form_SelectFullName)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 675, 280))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(50, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.listWidget_Name1 = QtWidgets.QListWidget(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_Name1.setFont(font)
        self.listWidget_Name1.setObjectName("listWidget_Name1")
        self.verticalLayout_2.addWidget(self.listWidget_Name1)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 4, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(100, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.listWidget_NameCount = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget_NameCount.setObjectName("listWidget_NameCount")
        self.verticalLayout.addWidget(self.listWidget_NameCount)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Random = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_Random.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Random.setObjectName("pushButton_Random")
        self.horizontalLayout.addWidget(self.pushButton_Random)
        self.lineEdit_RandomName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_RandomName.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_RandomName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_RandomName.setObjectName("lineEdit_RandomName")
        self.horizontalLayout.addWidget(self.lineEdit_RandomName)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 1, 3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(50, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.listWidget_Name2 = QtWidgets.QListWidget(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_Name2.setFont(font)
        self.listWidget_Name2.setObjectName("listWidget_Name2")
        self.verticalLayout_3.addWidget(self.listWidget_Name2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(100, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.listWidget_FullName = QtWidgets.QListWidget(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_FullName.setFont(font)
        self.listWidget_FullName.setObjectName("listWidget_FullName")
        self.verticalLayout_4.addWidget(self.listWidget_FullName)
        self.pushButton_RemoveName = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_RemoveName.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_RemoveName.setFont(font)
        self.pushButton_RemoveName.setObjectName("pushButton_RemoveName")
        self.verticalLayout_4.addWidget(self.pushButton_RemoveName)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 8, 2, 1)
        self.pushButton_AddFullName = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_AddFullName.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton_AddFullName.setFont(font)
        self.pushButton_AddFullName.setObjectName("pushButton_AddFullName")
        self.gridLayout.addWidget(self.pushButton_AddFullName, 0, 7, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.listWidget_SelectedWord = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget_SelectedWord.setEnabled(True)
        self.listWidget_SelectedWord.setObjectName("listWidget_SelectedWord")
        self.verticalLayout_5.addWidget(self.listWidget_SelectedWord)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)

        self.retranslateUi(Form_SelectFullName)
        QtCore.QMetaObject.connectSlotsByName(Form_SelectFullName)

    def retranslateUi(self, Form_SelectFullName):
        _translate = QtCore.QCoreApplication.translate
        Form_SelectFullName.setWindowTitle(_translate("Form_SelectFullName", "Select Full Name"))
        self.label_6.setText(_translate("Form_SelectFullName", "Name 1"))
        self.label_5.setText(_translate("Form_SelectFullName", "Name Count"))
        self.pushButton_Random.setText(_translate("Form_SelectFullName", "Random"))
        self.label_7.setText(_translate("Form_SelectFullName", "Name 2"))
        self.label_2.setText(_translate("Form_SelectFullName", "=>"))
        self.label_8.setText(_translate("Form_SelectFullName", "Full Name"))
        self.pushButton_RemoveName.setText(_translate("Form_SelectFullName", "Remove"))
        self.pushButton_AddFullName.setText(_translate("Form_SelectFullName", "->"))
        self.label_4.setText(_translate("Form_SelectFullName", "Selected Words"))
        self.label_3.setText(_translate("Form_SelectFullName", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_SelectFullName = QtWidgets.QWidget()
    ui = Ui_Form_SelectFullName()
    ui.setupUi(Form_SelectFullName)
    Form_SelectFullName.show()
    sys.exit(app.exec_())
