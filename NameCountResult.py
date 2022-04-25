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

        self.suggest_name_count_list = []
        self.selected_name_count_list = []

        self.ui.listWidget_SelectedNameCount.itemSelectionChanged.connect(self.listWidget_SelectedNameCount_SelectionChanged)
        self.ui.listWidget_SuggestNameCount.itemSelectionChanged.connect(self.listWidget_SuggestNameCount_SelectionChanged)

        self.ui.listWidget_SelectedNameCount.itemDoubleClicked.connect(self.listWidget_SelectedNameCount_DoubleClicked)
        self.ui.listWidget_SuggestNameCount.itemDoubleClicked.connect(self.listWidget_SuggestNameCount_DoubleClicked)

        self.ui.pushButton_Add.clicked.connect(self.pushButton_Add_Clicked)
        self.ui.pushButton_Remove.clicked.connect(self.pushButton_Remove_Clicked)

        pass

    def pushButton_Add_Clicked(self):
        add_item_text = self.ui.listWidget_SuggestNameCount.currentItem().text()
        
        matcheditems = self.ui.listWidget_SelectedNameCount.findItems(add_item_text, Qt.MatchExactly)
        if len(add_item_text) != 0 and len(matcheditems) == 0:
            self.ui.listWidget_SelectedNameCount.addItem(add_item_text)

            add_list_item = self.suggest_name_count_list[self.ui.listWidget_SuggestNameCount.currentRow()]
            self.selected_name_count_list.append(add_list_item)


    def pushButton_Remove_Clicked(self):
        selected_item_index = self.ui.listWidget_SelectedNameCount.currentRow()
        if selected_item_index == -1:
            return

        self.ui.listWidget_SelectedNameCount.takeItem(selected_item_index)
        del self.selected_name_count_list[selected_item_index]

    def listWidget_SelectedNameCount_SelectionChanged(self):
        self.ShowSelectedNameCount(self.ui.listWidget_SelectedNameCount.currentRow())

    def listWidget_SuggestNameCount_SelectionChanged(self):
        self.ShowSuggestNameCount(self.ui.listWidget_SuggestNameCount.currentRow())

    def listWidget_SelectedNameCount_DoubleClicked(self):
        self.ShowSelectedNameCount(-1)

    def listWidget_SuggestNameCount_DoubleClicked(self):
        self.ShowSuggestNameCount(-1)

    def showEvent(self, event):
        self.selected_name_count_list = []
        if os.path.isfile(Settings.SELECTED_NAME_COUNT_PATH):
            fNameCountResult = open(Settings.SELECTED_NAME_COUNT_PATH, 'r', encoding="utf-8")
            for line_word in fNameCountResult:
                self.selected_name_count_list.append(eval(line_word))
                pass
            fNameCountResult.close()
        else:
            print("File Not Exist: ", Settings.SELECTED_NAME_COUNT_PATH)

        self.ui.listWidget_SelectedNameCount.clear()
        name_count_list = [x[0] for x in self.selected_name_count_list]
        name_count_list_string = [str(x) for x in name_count_list]
        self.ui.listWidget_SelectedNameCount.addItems(name_count_list_string)

        event.accept()

        
    def closeEvent(self, event):
        fNameCountResult = open(Settings.SELECTED_NAME_COUNT_PATH, 'w', encoding="utf-8")
        for item in self.selected_name_count_list:
            fNameCountResult.write(str(item) + "\n")
        fNameCountResult.close()
    
        event.accept() # let the window close

    #
    # suggest_name_count_list = []    # item = [[last_name_count, name1_count, name2_count], grade_list[grade, grade_string], name_count_description]
    #
    def SetSuggestNameCount(self, suggest_name_count_list):

        self.suggest_name_count_list = suggest_name_count_list.copy()

        self.ui.listWidget_SuggestNameCount.clear()
        name_count_list = [x[0] for x in suggest_name_count_list]
        name_count_list_string = [str(x) for x in name_count_list]
        self.ui.listWidget_SuggestNameCount.addItems(name_count_list_string)

        self.ShowSuggestNameCount(-1)
        
        pass

    def ShowSelectedNameCount(self, name_count_index):
        self.ShowNameCount(name_count_index, self.selected_name_count_list)
        
    def ShowSuggestNameCount(self, name_count_index):
        self.ShowNameCount(name_count_index, self.suggest_name_count_list)

    def ShowNameCount(self, name_count_index, name_count_list):
        self.ui.textEdit_NameCountDescription.clear()

        if name_count_index == -1:
            show_name_count_list = name_count_list.copy()
        else:
            show_name_count_list = [name_count_list[name_count_index]]
            
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
        
