# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp

import os

import NameCountResult_ui as ui

import Settings



class Main(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_Form_NameCountResult()
        self.ui.setupUi(self)

        self.ui.listWidget_NameCount.itemSelectionChanged.connect(self.listWidget_NameCount_SelectionChanged)
        self.ui.listWidget_NameCount.itemDoubleClicked.connect(self.listWidget_NameCount_DoubleClicked)
        self.ui.pushButton_Remove.clicked.connect(self.pushButton_Remove_Clicked)

        pass

    def RemoveItem(self, index):

        if index == -1:
            return

        self.ui.listWidget_NameCount.takeItem(index)
        del self.name_count_result_list[index]
        # print("len(self.name_count_result_list) = ", len(self.name_count_result_list))
    
        pass

    def pushButton_Remove_Clicked(self):
        selected_item_index = self.ui.listWidget_NameCount.currentRow()
        self.RemoveItem(selected_item_index)

    def listWidget_NameCount_SelectionChanged(self):
        self.ShowNameCount(self.ui.listWidget_NameCount.currentRow())

    def listWidget_NameCount_DoubleClicked(self):
        self.ShowNameCount(-1)


    def showEvent(self, event):
        self.name_count_result_list = []
        if os.path.isfile(Settings.NAME_COUNT_RESULT_PATH):
            fNameCountResult = open(Settings.NAME_COUNT_RESULT_PATH, 'r', encoding="utf-8")
            for line_word in fNameCountResult:
                self.name_count_result_list.append(eval(line_word))
                pass
            fNameCountResult.close()
        else:
            print("File Not Exist: ", Settings.NAME_COUNT_RESULT_PATH)

        self.ui.listWidget_NameCount.clear()
        name_count_list = [x[0] for x in self.name_count_result_list]
        name_count_list_string = [str(x) for x in name_count_list]
        self.ui.listWidget_NameCount.addItems(name_count_list_string)

        self.ShowNameCount(-1)

        event.accept()

        
    def closeEvent(self, event):
        fNameCountResult = open(Settings.NAME_COUNT_RESULT_PATH, 'w', encoding="utf-8")
        for item in self.name_count_result_list:
            fNameCountResult.write(str(item) + "\n")
        fNameCountResult.close()
    
        event.accept() # let the window close

    def ShowNameCount(self, name_count_index):
        self.ui.textEdit_NameCountDescription.clear()

        if name_count_index == -1:
            show_name_count_list = self.name_count_result_list.copy()
        else:
            show_name_count_list = [self.name_count_result_list[name_count_index]]
            
        for item in show_name_count_list:
            item1_string = ""
            five_level_grade = 0
            count = 0
            for x in item[1]:
                item1_string = item1_string + str(x) + "\t"
                if count == 2 or count == 5:
                    item1_string = item1_string + "\n"
                five_level_grade = five_level_grade + x[0]
                count = count + 1
            description_string = str(item[0]) + ": " + str(five_level_grade) + "\n" + item1_string + str(item[2]) + "\n"
            self.ui.textEdit_NameCountDescription.append(description_string)

        self.ui.textEdit_NameCountDescription.verticalScrollBar().setValue(0);
        
        pass
        
