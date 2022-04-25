# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp

import os.path

import SelectWord_ui as ui

import Settings


class Main(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_Form_SelectWord()
        self.ui.setupUi(self)

        #
        # Parameters
        #
        self.name_word_array = []
        
        self.checkbox_element = [self.ui.checkBox_SelectWord_Gold, self.ui.checkBox_SelectWord_Wood, self.ui.checkBox_SelectWord_Water, self.ui.checkBox_SelectWord_Fire, self.ui.checkBox_SelectWord_Earth]


        #
        # Connect
        #
        self.ui.pushButton_ListWord.clicked.connect(self.button_WordList)
        self.ui.pushButton_AddWord.clicked.connect(self.listWidget_WordList_DoubleClicked)
        self.ui.pushButton_RemoveWord.clicked.connect(self.listWidget_SelectedWord_DoubleClicked)

        self.ui.listWidget_WordList.itemDoubleClicked.connect(self.listWidget_WordList_DoubleClicked)
        self.ui.listWidget_SelectedWord.itemDoubleClicked.connect(self.listWidget_SelectedWord_DoubleClicked)

        self.ui.comboBox_NameCount.currentTextChanged.connect(self.comboBox_NameCount_TextChanged)

        #
        # File Read
        #
        fNameWords = open(Settings.NAME_WORDS_PATH, 'r', encoding="utf-8")
        for line_word in fNameWords:
            line_temp = line_word.split(")")
            if len(line_temp) == 1:
                break
            element_word = []
            for element_index in range(1, 5):
                element_word.append(line_temp[element_index][:-2])
            element_word.append(line_temp[5][:-1])
            self.name_word_array.append(element_word)
        fNameWords.close()

        if os.path.isfile(Settings.SELECTED_WORD_PATH):
            self.ui.listWidget_SelectedWord.clear()
            fSelectedWord = open(Settings.SELECTED_WORD_PATH, 'r', encoding="utf-8")
            for line_word in fSelectedWord:
                self.ui.listWidget_SelectedWord.addItem(line_word[:-1])
                pass
            fSelectedWord.close()

        pass

    def comboBox_NameCount_TextChanged(self):
        self.ui.pushButton_ListWord.click()

    def showEvent(self, event):
        self.name_count_result_list = []
        if os.path.isfile(Settings.SELECTED_NAME_COUNT_PATH):
            fNameCountResult = open(Settings.SELECTED_NAME_COUNT_PATH, 'r', encoding="utf-8")
            for line_word in fNameCountResult:
                self.name_count_result_list.append(eval(line_word))
                pass
            fNameCountResult.close()
        else:
            print("File Not Exist: ", Settings.SELECTED_NAME_COUNT_PATH)

        self.ui.comboBox_NameCount.clear()
        name_count_list = [x[0] for x in self.name_count_result_list]
        name_count_list_str = [str(x) for x in self.NameCountSort(name_count_list)]
        self.ui.comboBox_NameCount.addItems(name_count_list_str)

        event.accept()

    def closeEvent(self, event):
        fSelectedWord = open(Settings.SELECTED_WORD_PATH, 'w', encoding="utf-8")
        for index in range(self.ui.listWidget_SelectedWord.count()):
            fSelectedWord.write(self.ui.listWidget_SelectedWord.item(index).text() + "\n")
        fSelectedWord.close()
        
        event.accept() # let the window close


    #
    #   COMPONENT
    #
    def listWidget_WordList_DoubleClicked(self):
    
        if self.ui.listWidget_WordList.currentRow() == -1:
            return
            
        selected_word = self.ui.listWidget_WordList.currentItem().text()
        matcheditems = self.ui.listWidget_SelectedWord.findItems(selected_word, Qt.MatchExactly)
        if len(matcheditems) == 0:
            self.ui.listWidget_SelectedWord.addItem(selected_word)
        pass
     
        
    def listWidget_SelectedWord_DoubleClicked(self):
    
        selected_word_index = self.ui.listWidget_SelectedWord.currentRow()
        if selected_word_index == -1:
            return

        self.ui.listWidget_SelectedWord.takeItem(selected_word_index)
        pass

    def button_WordList(self):
        
        if self.ui.comboBox_NameCount.currentIndex() == -1:
            return
        
        element5_chinese = ["金", "木", "水", "火", "土"]
        
        name_count = int(self.ui.comboBox_NameCount.currentText())

        self.ui.listWidget_WordList.clear()
        
        for element_index in range(5):
            if self.checkbox_element[element_index].isChecked():
                for name_word in self.name_word_array[name_count-1][element_index]:
                    self.ui.listWidget_WordList.addItem(name_word+"-"+str(name_count)+"-"+element5_chinese[element_index])
        
        pass


    def NameCountSort(self, name_count_list):
        name_count_collect = []
        
        for item in name_count_list:
            if item[1] not in name_count_collect:
                name_count_collect.append(item[1])
            if item[2] not in name_count_collect:
                name_count_collect.append(item[2])
        return sorted(name_count_collect)

        

