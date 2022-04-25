# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp

import os.path
import random

import SelectFullName_ui as ui

import Settings


class Main(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_Form_SelectFullName()
        self.ui.setupUi(self)

        #
        # Parameters
        #
        self.selected_word = []
        self.last_name = ""

        #
        # Connect
        #
        self.ui.listWidget_NameCount.itemSelectionChanged.connect(self.listWidget_NameCount_SelectionChanged)
        self.ui.pushButton_AddFullName.clicked.connect(self.button_AddFullName)
        self.ui.pushButton_Random.clicked.connect(self.button_RandomName)


        #
        # File Read
        #

        pass

    def button_RandomName(self):
        retry_count = 0
        while retry_count < 100:
            retry_count = retry_count + 1
            self.ui.listWidget_NameCount.setCurrentRow(random.randrange(self.ui.listWidget_NameCount.count()))
            if self.ui.listWidget_Name1.count() and self.ui.listWidget_Name2.count():
                break
        if retry_count == 100:
            self.ui.listWidget_NameCount.setCurrentRow(-1)
            self.ui.lineEdit_RandomName.setText("404")
            return
        self.ui.listWidget_Name1.setCurrentRow(random.randrange(self.ui.listWidget_Name1.count()))
        self.ui.listWidget_Name2.setCurrentRow(random.randrange(self.ui.listWidget_Name2.count()))
        
        self.ui.lineEdit_RandomName.setText(self.last_name + self.ui.listWidget_Name1.currentItem().text() + self.ui.listWidget_Name2.currentItem().text())
        
        pass

    def button_AddFullName(self):
        if self.ui.listWidget_Name1.currentRow() == -1 or self.ui.listWidget_Name2.currentRow() == -1:
            return
        
        full_name = self.last_name + self.ui.listWidget_Name1.currentItem().text() + self.ui.listWidget_Name2.currentItem().text()
        matcheditems = self.ui.listWidget_FullName.findItems(full_name, Qt.MatchExactly)
        if len(matcheditems) == 0:
            self.ui.listWidget_FullName.addItem(full_name)

        pass

    def listWidget_NameCount_SelectionChanged(self):
    
        if self.ui.listWidget_NameCount.currentRow() == -1:
            self.ui.listWidget_Name1.clear()
            self.ui.listWidget_Name2.clear()
            return
    
        name_count_list = eval(self.ui.listWidget_NameCount.currentItem().text())
        # print("name_count_list = ", name_count_list)
        
        self.ui.listWidget_Name1.clear()
        self.ui.listWidget_Name2.clear()
        for word in self.selected_word:
            if int(word[1]) == name_count_list[1]:
                self.ui.listWidget_Name1.addItem(word[0])
            if int(word[1]) == name_count_list[2]:
                self.ui.listWidget_Name2.addItem(word[0])
       
        pass

    def showEvent(self, event):
        self.selected_word = []
        if os.path.isfile(Settings.SELECTED_WORD_PATH):
            self.ui.listWidget_SelectedWord.clear()
            fSelectedWord = open(Settings.SELECTED_WORD_PATH, 'r', encoding="utf-8")
            for line_word in fSelectedWord:
                self.ui.listWidget_SelectedWord.addItem(line_word[:-1])
                self.selected_word.append(line_word[:-1].split("-"))
                pass
            fSelectedWord.close()
        else:
            print("File Not Exist: ", Settings.SELECTED_WORD_PATH)

        if os.path.isfile(Settings.SELECTED_NAME_COUNT_PATH):
            self.ui.listWidget_NameCount.clear()
            fNameCountResult = open(Settings.SELECTED_NAME_COUNT_PATH, 'r', encoding="utf-8")
            for line_word in fNameCountResult:
                result_list = eval(line_word)
                self.ui.listWidget_NameCount.addItem(str(result_list[0]))
                pass
            fNameCountResult.close()
        else:
            print("File Not Exist: ", Settings.SELECTED_NAME_COUNT_PATH)

        if os.path.isfile(Settings.FULL_NAME_PATH):
            self.ui.listWidget_FullName.clear()
            fFullName = open(Settings.FULL_NAME_PATH, 'r', encoding="utf-8")
            for line_word in fFullName:
                self.ui.listWidget_FullName.addItem(line_word[:-1])     # ignore '\n'
                pass
            fFullName.close()
        else:
            print("File Not Exist: ", Settings.FULL_NAME_PATH)


        event.accept()

    def closeEvent(self, event):
        fFullName = open(Settings.FULL_NAME_PATH, 'w', encoding="utf-8")
        for index in range(self.ui.listWidget_FullName.count()):
            fFullName.write(self.ui.listWidget_FullName.item(index).text() + "\n")
        fFullName.close()

        
        event.accept() # let the window close


    #
    #   COMPONENT
    #
        

