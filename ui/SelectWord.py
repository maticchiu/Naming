# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os.path

from ui.form.SelectWord_ui import Ui_Form_SelectWord

import Settings


class Main(QWidget, Ui_Form_SelectWord):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #
        # Parameters
        #
        self.name_word_array = []
        self.checkbox_element = [self.checkBox_SelectWord_Gold, self.checkBox_SelectWord_Wood, self.checkBox_SelectWord_Water, self.checkBox_SelectWord_Fire, self.checkBox_SelectWord_Earth]

        #
        # Connect
        #
        self.pushButton_AddWord.clicked.connect(self.listWidget_WordList_DoubleClicked)
        self.pushButton_RemoveWord.clicked.connect(self.listWidget_SelectedWord_DoubleClicked)

        self.listWidget_WordList.itemDoubleClicked.connect(self.listWidget_WordList_DoubleClicked)
        self.listWidget_SelectedWord.itemDoubleClicked.connect(self.listWidget_SelectedWord_DoubleClicked)

        self.comboBox_NameCount.currentTextChanged.connect(self.UpdateWordList)

        self.checkBox_SelectWord_Gold.stateChanged.connect(self.UpdateWordList)
        self.checkBox_SelectWord_Wood.stateChanged.connect(self.UpdateWordList)
        self.checkBox_SelectWord_Water.stateChanged.connect(self.UpdateWordList)
        self.checkBox_SelectWord_Fire.stateChanged.connect(self.UpdateWordList)
        self.checkBox_SelectWord_Earth.stateChanged.connect(self.UpdateWordList)

        #
        # File Read
        #
        
        # Load NameWord
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

    def showEvent(self, event):
        # Read name count result for name count
        self.name_count_result_list = []
        if os.path.isfile(Settings.SELECTED_NAME_COUNT_PATH):
            fNameCountResult = open(Settings.SELECTED_NAME_COUNT_PATH, 'r', encoding="utf-8")
            for line_word in fNameCountResult:
                self.name_count_result_list.append(eval(line_word))
            fNameCountResult.close()
        else:
            print("File Not Exist: ", Settings.SELECTED_NAME_COUNT_PATH)

        # Add name count to combobox
        self.comboBox_NameCount.clear()
        name_count_list = [x[0] for x in self.name_count_result_list]
        name_count_list_str = [str(x) for x in self.NameCountSort(name_count_list)]
        self.comboBox_NameCount.addItems(name_count_list_str)

        # Read SelectWord setting
        if os.path.isfile(Settings.SELECT_WORD_SETTING_PATH):
            fSelectWordSetting = open(Settings.SELECT_WORD_SETTING_PATH, 'r', encoding="utf-8")
            data = fSelectWordSetting.readline()
            element5_list = eval(data)
            for index in range(5):
                self.checkbox_element[index].setChecked(element5_list[index])
            fSelectWordSetting.close()

        # Read selected words
        if os.path.isfile(Settings.SELECTED_WORD_PATH):
            self.listWidget_SelectedWord.clear()
            fSelectedWord = open(Settings.SELECTED_WORD_PATH, 'r', encoding="utf-8")
            for line_word in fSelectedWord:
                self.listWidget_SelectedWord.addItem(line_word[:-1])
            fSelectedWord.close()

        # Update WordList
        self.UpdateWordList()

        event.accept()

    def closeEvent(self, event):

        # Sort selected word list
        selected_word_list = []
        for index in range(self.listWidget_SelectedWord.count()):
            selected_word_list.append(self.listWidget_SelectedWord.item(index).text().split("-"))
        selected_word_list.sort(key = self.SelectedWord_SortFunc)
    
        # Save selected words
        fSelectedWord = open(Settings.SELECTED_WORD_PATH, 'w', encoding="utf-8")
        for item in selected_word_list:
            fSelectedWord.write(item[0] + "-" + item[1] + "-" + item[2] + "\n")
        fSelectedWord.close()
        
        # Save SelectWord setting
        fSelectWordSetting = open(Settings.SELECT_WORD_SETTING_PATH, 'w', encoding="utf-8")
        data = [x.isChecked() for x in self.checkbox_element]
        fSelectWordSetting.write(str(data))
        fSelectWordSetting.close()
        
        event.accept() # let the window close

    #------------------------------------------------------
    #               COMPONENT
    #------------------------------------------------------

    def listWidget_WordList_DoubleClicked(self):
    
        if self.listWidget_WordList.currentRow() == -1:
            return
            
        selected_word = self.listWidget_WordList.currentItem().text()
        matcheditems = self.listWidget_SelectedWord.findItems(selected_word, Qt.MatchExactly)
        if len(matcheditems) == 0:
            self.listWidget_SelectedWord.addItem(selected_word)
        
    def listWidget_SelectedWord_DoubleClicked(self):
    
        selected_word_index = self.listWidget_SelectedWord.currentRow()
        if selected_word_index == -1:
            return

        self.listWidget_SelectedWord.takeItem(selected_word_index)

    def button_WordList(self):
        
        if self.comboBox_NameCount.currentIndex() == -1:
            return
        
        element5_chinese = ["金", "木", "水", "火", "土"]
        
        name_count = int(self.comboBox_NameCount.currentText())

        self.listWidget_WordList.clear()
        
        for element_index in range(5):
            if self.checkbox_element[element_index].isChecked():
                for name_word in self.name_word_array[name_count-1][element_index]:
                    self.listWidget_WordList.addItem(name_word+"-"+str(name_count)+"-"+element5_chinese[element_index])

    #------------------------------------------------------
    #               FUNCTION IMPLEMENT
    #------------------------------------------------------

    def NameCountSort(self, name_count_list):
        name_count_collect = []
        
        for item in name_count_list:
            if item[1] not in name_count_collect:
                name_count_collect.append(item[1])
            if item[2] not in name_count_collect:
                name_count_collect.append(item[2])
        return sorted(name_count_collect)

    def SelectedWord_SortFunc(self, selected_word_item):
        return int(selected_word_item[1]) * 10 + ["金", "木", "水", "火", "土"].index(selected_word_item[2])

    def UpdateWordList(self):
        if self.comboBox_NameCount.currentIndex() == -1:
            return
        
        element5_chinese = ["金", "木", "水", "火", "土"]
        
        name_count = int(self.comboBox_NameCount.currentText())

        self.listWidget_WordList.clear()
        
        for element_index in range(5):
            if self.checkbox_element[element_index].isChecked():
                for name_word in self.name_word_array[name_count-1][element_index]:
                    self.listWidget_WordList.addItem(name_word+"-"+str(name_count)+"-"+element5_chinese[element_index])
