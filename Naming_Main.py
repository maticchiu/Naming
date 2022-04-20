# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QRegExp

import datetime
import os

import Naming_ui as ui
import NameCountResult as ncr
import SelectWord as sw
import SelectFullName as sfn

import Settings


###################################################
#                   Constant
###################################################

# 天 sky
# 地 ground
# 人 person
# 總 destiny
# 外 fate

# 金 gold
# 木 wood
# 水 water
# 火 fire
# 土 earth

aiElement5 = [4, 1, 0, 2, 3]
strElement5 = ["金", "木", "水", "火", "土"]


# NAME_COUNT_DESCRIPTION_PATH = "./Data/NameCountDescription.txt"
# self.checkbox_type5 = None
# self.name_count_description = None


###################################################
#                   Main class
###################################################
class Main(QMainWindow, ui.Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #
        # Parameters
        #
        Settings.init()                         # Global parameter initialization
        self.name_count_description = None      # to save description from text file
        self.name_count_result_list = []        # [[element5, name count, name count description], ...]
        self.checkbox_type5 = [[self.checkBox_Sky_Gold, self.checkBox_Sky_Wood, self.checkBox_Sky_Water, self.checkBox_Sky_Fire, self.checkBox_Sky_Earth], [self.checkBox_Ground_Gold, self.checkBox_Ground_Wood, self.checkBox_Ground_Water, self.checkBox_Ground_Fire, self.checkBox_Ground_Earth], [self.checkBox_Person_Gold, self.checkBox_Person_Wood, self.checkBox_Person_Water, self.checkBox_Person_Fire, self.checkBox_Person_Earth], [self.checkBox_Destiny_Gold, self.checkBox_Destiny_Wood, self.checkBox_Destiny_Water, self.checkBox_Destiny_Fire, self.checkBox_Destiny_Earth], [self.checkBox_Fate_Gold, self.checkBox_Fate_Wood, self.checkBox_Fate_Water, self.checkBox_Fate_Fire, self.checkBox_Fate_Earth]]
        self.last_name_count_list = []

        #
        # Connect
        #
        self.pushButton_GetNameCount.clicked.connect(self.button_GetNameCount)
        self.pushButton_SelectNameWord.clicked.connect(self.button_SelectNameWord)
        self.pushButton_SelectFullName.clicked.connect(self.button_SelectFullName)
        self.lineEdit_LastName.textChanged.connect(self.lineEdit_LastName_TextChanged)
        
        
        #
        # Sub Form
        #
        self.NameCountResult = ncr.Main()
        self.NameCountResult.remove_item_index_signal.connect(self.RemoveNameCountItem)
        
        self.SelectWord = sw.Main()
        
        self.SelectFullName = sfn.Main()
        
        if not os.path.isdir(Settings.USER_PATH):
            os.mkdir(Settings.USER_PATH)
        
        #
        # File Read
        #
        fNameCountDescription = open(Settings.NAME_COUNT_DESCRIPTION_PATH, 'r', encoding="utf-8")
        self.name_count_description = fNameCountDescription.readlines()
        fNameCountDescription.close()

        fLastNameCount = open(Settings.LAST_NAME_COUNT_PATH, 'r', encoding="utf-8")
        for line in fLastNameCount:
            self.last_name_count_list.append(line[:-1]) # Ignore '\n'
        fLastNameCount.close()

    #
    #   COMPONENT
    #
    def lineEdit_LastName_TextChanged(self):
        new_last_name = self.lineEdit_LastName.text()

        if len(new_last_name) == 0:
            self.spinBox_LastNameCount.setValue(0)
            return
            
        for last_name_index in range(len(self.last_name_count_list)):
            if new_last_name in self.last_name_count_list[last_name_index]:
                self.spinBox_LastNameCount.setValue(last_name_index + 1)
                break
        pass
    
    def button_SelectNameWord(self):
        self.SelectWord.show()
        pass

    def button_GetNameCount(self):
    
        hit_count = 0
        hit_count_list = []
        element5_chinese = ["金", "木", "水", "火", "土"]
        result_description = ""
        self.name_count_result_list = []
        
        name_count_list = []
    
        for name1_count in range(self.spinBox_NameCount_Min.value(), self.spinBox_NameCount_Max.value()+1):
            for name2_count in range(self.spinBox_NameCount_Min.value(), self.spinBox_NameCount_Max.value()+1):
                for sky_index in range(5):
                    if self.checkbox_type5[0][sky_index].isChecked() == False:
                        continue
                    name_count = self.spinBox_LastNameCount.value() + 1
                    name_count = ((name_count % 10) + 1) // 2 % 5
                
                    if aiElement5[sky_index] != name_count:
                        continue
                    # print("sky_index = ", sky_index)
                    for ground_index in range(5):
                        # print("ground_index = ", ground_index)
                        if self.checkbox_type5[1][ground_index].isChecked() == False:
                            continue
                        name_count = name1_count + name2_count
                        name_count = ((name_count % 10) + 1) // 2 % 5
                    
                        if aiElement5[ground_index] != name_count:
                            continue
                        # print("ground_index = ", ground_index)
                        for person_index in range(5):
                            
                            if self.checkbox_type5[2][person_index].isChecked() == False:
                                continue
                            name_count = self.spinBox_LastNameCount.value() + name1_count
                            name_count = ((name_count % 10) + 1) // 2 % 5
                        
                            if aiElement5[person_index] != name_count:
                                continue                        
                            # print("person_index = ", person_index)
                            for destiny_index in range(5):
                            
                                if self.checkbox_type5[3][destiny_index].isChecked() == False:
                                    continue
                                name_count = self.spinBox_LastNameCount.value() + name1_count + name2_count
                                name_count = ((name_count % 10) + 1) // 2 % 5
                            
                                if aiElement5[destiny_index] != name_count:
                                    continue
                                # print("destiny_index = ", destiny_index)
                                for fate_index in range(5):
                                    
                                    if self.checkbox_type5[4][fate_index].isChecked() == False:
                                        continue
                                        
                                    name_count = name2_count + 1
                                    name_count = ((name_count % 10) + 1) // 2 % 5
                                    # print("fate_index1 = ", fate_index)
                                    if aiElement5[fate_index] != name_count:
                                        # print("aiElement5[fate_index] = ", aiElement5[fate_index], "name_count = ", name_count)
                                        continue                                
                            
                                    # print("fate_index = ", fate_index)
                            
                                    name_count = self.spinBox_LastNameCount.value() + name1_count + name2_count
                                    if "（凶）" in self.name_count_description[name_count - 1] or "（半凶）" in self.name_count_description[name_count - 1]:
                                        continue
                                    if self.radioButton_Gender_Girl.isChecked() and "女性不宜此數" in self.name_count_description[name_count - 1]:
                                        continue
                                        
                                    if (self.checkBox_HalfLuck.isChecked() == True and "（半吉）" in self.name_count_description[name_count - 1]) or "（吉）" in self.name_count_description[name_count - 1]:
                                        if len(name_count_list) == 0 or (len(name_count_list) != 0 and name_count_list[-1] != [self.spinBox_LastNameCount.value(), name1_count, name2_count]):
                                            hit_count = hit_count + 1
                                            name_count_list.append([self.spinBox_LastNameCount.value(), name1_count, name2_count])
                                            if name1_count not in hit_count_list:
                                                hit_count_list.append(name1_count)
                                            if name2_count not in hit_count_list:
                                                hit_count_list.append(name2_count)
                                                
                                            element5_string = "[" + element5_chinese[sky_index] + ", " + element5_chinese[ground_index] + ", " + element5_chinese[person_index] + ", " + element5_chinese[destiny_index] + ", " + element5_chinese[fate_index] + "]"
                                            self.name_count_result_list.append([element5_string, name_count_list[-1], self.name_count_description[name_count - 1]])

                                        pass
                                            
                                    pass                             
                                pass                         
                            pass                     
                        pass                
                    pass
                pass        
        
            pass
    
        print("hit_count = ", hit_count)
        print("name_count_list = ", name_count_list)
        
        self.textEdit_Log.append(datetime.datetime.now().strftime("----- %Y/%m/%d %H:%M:%S -----"))
        self.textEdit_Log.append("共" + str(len(name_count_list)) + "組筆劃組合")
        self.textEdit_Log.append(str(name_count_list))
        self.textEdit_Log.append("整理筆劃如下：")
        self.textEdit_Log.append(str(self.NameCountSort(name_count_list)) + "\n")
    
        
        self.NameCountResult.show()
        self.NameCountResult.ShowNameCount(self.name_count_result_list)
        pass

    def button_SelectFullName(self):
        self.SelectFullName.show()
        self.SelectFullName.last_name = self.lineEdit_LastName.text()
        pass

    #
    #   FUNCTION IMPLEMENT
    #
    def NameCountSort(self, name_count_list):
        name_count_collect = []
        
        for item in name_count_list:
            if item[1] not in name_count_collect:
                name_count_collect.append(item[1])
            if item[2] not in name_count_collect:
                name_count_collect.append(item[2])
        return sorted(name_count_collect)

    def RemoveNameCountItem(self, index):
        # print("Main - remove = ", index)
        self.textEdit_Log.append(datetime.datetime.now().strftime("----- %Y/%m/%d %H:%M:%S -----"))
        self.textEdit_Log.append("刪除筆劃：\n"+self.name_count_result_list[index][0]+";"+str(self.name_count_result_list[index][1]))
        self.name_count_result_list.pop(index)
        self.textEdit_Log.append("整理筆劃如下：")
        name_count_list = [x[1] for x in self.name_count_result_list]
        self.textEdit_Log.append(str(self.NameCountSort(name_count_list)) + "\n")
        
        pass


###################################################
#                   Main function
###################################################
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
