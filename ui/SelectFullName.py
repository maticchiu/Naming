# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os.path
import random

from ui.form.SelectFullName_ui import Ui_Form_SelectFullName

import Settings


class Main(QWidget, Ui_Form_SelectFullName):
    
    def __init__(self):
        super().__init__()
        # self.ui = ui.Ui_Form_SelectFullName()
        self.setupUi(self)

        #
        # Parameters
        #
        self.selected_word = []
        self.last_name = ""

        #
        # Connect
        #
        self.listWidget_NameCount.itemSelectionChanged.connect(self.listWidget_NameCount_SelectionChanged)
        self.listWidget_FullName.itemDoubleClicked.connect(self.listWidget_FullName_DoubleClicked)
        self.pushButton_AddFullName.clicked.connect(self.button_AddFullName)
        self.pushButton_Random.clicked.connect(self.button_RandomName)
        self.pushButton_RemoveName.clicked.connect(self.button_RemoveName)

        #
        # File Read
        #

    def showEvent(self, event):
        self.selected_word = []
        if os.path.isfile(Settings.SELECTED_WORD_PATH):
            self.listWidget_SelectedWord.clear()
            fSelectedWord = open(Settings.SELECTED_WORD_PATH, 'r', encoding="utf-8")
            for line_word in fSelectedWord:
                self.listWidget_SelectedWord.addItem(line_word[:-1])
                self.selected_word.append(line_word[:-1].split("-"))
                pass
            fSelectedWord.close()
        else:
            print("File Not Exist: ", Settings.SELECTED_WORD_PATH)

        if os.path.isfile(Settings.SELECTED_NAME_COUNT_PATH):
            self.listWidget_NameCount.clear()
            fNameCountResult = open(Settings.SELECTED_NAME_COUNT_PATH, 'r', encoding="utf-8")
            for line_word in fNameCountResult:
                result_list = eval(line_word)
                self.listWidget_NameCount.addItem(str(result_list[0]))
                pass
            fNameCountResult.close()
        else:
            print("File Not Exist: ", Settings.SELECTED_NAME_COUNT_PATH)

        if os.path.isfile(Settings.FULL_NAME_PATH):
            self.listWidget_FullName.clear()
            fFullName = open(Settings.FULL_NAME_PATH, 'r', encoding="utf-8")
            for line_word in fFullName:
                self.listWidget_FullName.addItem(line_word[:-1])     # ignore '\n'
                pass
            fFullName.close()
        else:
            print("File Not Exist: ", Settings.FULL_NAME_PATH)

        event.accept()

    def closeEvent(self, event):
        fFullName = open(Settings.FULL_NAME_PATH, 'w', encoding="utf-8")
        for index in range(self.listWidget_FullName.count()):
            fFullName.write(self.listWidget_FullName.item(index).text() + "\n")
        fFullName.close()
        
        event.accept() # let the window close

    #------------------------------------------------------
    #               COMPONENT
    #------------------------------------------------------
    
    def button_RandomName(self):
        retry_count = 0
        while retry_count < 100:
            retry_count = retry_count + 1
            self.listWidget_NameCount.setCurrentRow(random.randrange(self.listWidget_NameCount.count()))
            if self.listWidget_Name1.count() and self.listWidget_Name2.count():
                break
        if retry_count == 100:
            self.listWidget_NameCount.setCurrentRow(-1)
            self.lineEdit_RandomName.setText("404")
            return
        self.listWidget_Name1.setCurrentRow(random.randrange(self.listWidget_Name1.count()))
        self.listWidget_Name2.setCurrentRow(random.randrange(self.listWidget_Name2.count()))
        
        self.lineEdit_RandomName.setText(self.last_name + self.listWidget_Name1.currentItem().text() + self.listWidget_Name2.currentItem().text())

    def button_AddFullName(self):
        if self.listWidget_Name1.currentRow() == -1 or self.listWidget_Name2.currentRow() == -1:
            return
        
        full_name = self.last_name + self.listWidget_Name1.currentItem().text() + self.listWidget_Name2.currentItem().text()
        matcheditems = self.listWidget_FullName.findItems(full_name, Qt.MatchExactly)
        if len(matcheditems) == 0:
            self.listWidget_FullName.addItem(full_name)

    def listWidget_NameCount_SelectionChanged(self):
    
        if self.listWidget_NameCount.currentRow() == -1:
            self.listWidget_Name1.clear()
            self.listWidget_Name2.clear()
            return
    
        name_count_list = eval(self.listWidget_NameCount.currentItem().text())
        # print("name_count_list = ", name_count_list)
        
        self.listWidget_Name1.clear()
        self.listWidget_Name2.clear()
        for word in self.selected_word:
            if int(word[1]) == name_count_list[1]:
                self.listWidget_Name1.addItem(word[0])
            if int(word[1]) == name_count_list[2]:
                self.listWidget_Name2.addItem(word[0])

    def button_RemoveName(self):
        if self.listWidget_FullName.currentRow() != -1:
            self.listWidget_FullName.takeItem(self.listWidget_FullName.currentRow())

    def listWidget_FullName_DoubleClicked(self):
        if self.listWidget_FullName.currentRow() != -1:
             self.listWidget_FullName.takeItem(self.listWidget_FullName.currentRow())
