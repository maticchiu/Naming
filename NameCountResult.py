# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp

import NameCountResult_ui as ui

import Settings



class Main(QWidget):

    remove_item_index_signal = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_Form_NameCountResult()
        self.ui.setupUi(self)

        self.ui.listWidget_NameCount.itemDoubleClicked.connect(self.listWidget_NameCount_DoubleClicked)
        self.ui.pushButton_Remove.clicked.connect(self.pushButton_Remove_Clicked)
        pass

    def RemoveItem(self, index):

        if index == -1:
            return

        self.ui.listWidget_NameCount.takeItem(index)
        self.remove_item_index_signal.emit(index)
    
        pass

    def pushButton_Remove_Clicked(self):
        selected_item_index = self.ui.listWidget_NameCount.currentRow()
        self.RemoveItem(selected_item_index)

    def listWidget_NameCount_DoubleClicked(self):
        # self.ui.listWidget_NameCount.takeItem(self.ui.listWidget_NameCount.row(item))
        selected_item_index = self.ui.listWidget_NameCount.currentRow()
        self.RemoveItem(selected_item_index)
        
    def closeEvent(self, event):

        fNameCountResult = open(Settings.NAME_COUNT_RESULT_PATH, 'w', encoding="utf-8")
        for index in range(self.ui.listWidget_NameCount.count()):
            fNameCountResult.write(self.ui.listWidget_NameCount.item(index).text() + "\n")
        fNameCountResult.close()
    
        event.accept() # let the window close

    def ShowNameCount(self, name_count_list):
        self.ui.textEdit_NameCountDescription.clear()
        self.ui.listWidget_NameCount.clear()
        for name_count_description in name_count_list:
            self.ui.textEdit_NameCountDescription.append(name_count_description[0] + " - " + str(name_count_description[1]) + "\n" + name_count_description[2])
            self.ui.listWidget_NameCount.addItem(name_count_description[0] + "; " + str(name_count_description[1]))
        pass
        
