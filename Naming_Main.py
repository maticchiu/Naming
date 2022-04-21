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
# 總 total
# 外 appearance

# 金 gold
# 木 wood
# 水 water
# 火 fire
# 土 earth

aiElement5 = [4, 1, 0, 2, 3]
strElement5 = ["金", "木", "水", "火", "土"]


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
        self.name_count_description = []        # to save description from text file
        self.name_count_result_list = []        # [[element5, name count, name count description], ...]
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
        for line in fNameCountDescription:
            self.name_count_description.append(line[:-1])   # Ignore '\n'
        fNameCountDescription.close()

        fLastNameCount = open(Settings.LAST_NAME_COUNT_PATH, 'r', encoding="utf-8")
        for line in fLastNameCount:
            self.last_name_count_list.append(line[:-1])     # Ignore '\n'
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
    
        # element5_chinese = ["金", "木", "水", "火", "土"]
        five_level_name_count_list = []
        self.name_count_result_list = []    # item = [[last_name_count, name1_count, name2_count], grade_list[grade, grade_string], name_count_description]
        
        # name_count_list = []
    
        #
        # Get name count list according to five level
        #
        five_level_name_count_list = self.FiveLevel_GetNameCount()
    
        #
        #Filter name count list via NameCountDescription
        #
        five_level_name_count_list = self.NameCoutDescription_FilterNameCountList(five_level_name_count_list)

        self.name_count_result_list = [[x[0], x[1], self.name_count_description[x[0][0] + x[0][1] + x[0][2] - 1]] for x in five_level_name_count_list]


        name_count_list = [x[0] for x in self.name_count_result_list]

        print("len(five_level_name_count_list) = ", len(five_level_name_count_list))
        print("name_count_list = ", name_count_list)
        print("self.name_count_result_list = ", self.name_count_result_list)
        
        self.textEdit_Log.append(datetime.datetime.now().strftime("----- %Y/%m/%d %H:%M:%S -----"))
        self.textEdit_Log.append("共" + str(len(self.name_count_result_list)) + "組筆劃組合")
        self.textEdit_Log.append(str(name_count_list))
        self.textEdit_Log.append("整理筆劃如下：")
        self.textEdit_Log.append(str(self.NameCountSort(name_count_list)) + "\n")

        fNameCountResult = open(Settings.NAME_COUNT_RESULT_PATH, 'w', encoding="utf-8")
        for item in self.name_count_result_list:
            fNameCountResult.write(str(item) + "\n")
        fNameCountResult.close()
    
        
        self.NameCountResult.show()
        # self.NameCountResult.ShowNameCount(self.name_count_result_list)
        pass

    def button_SelectFullName(self):
        self.SelectFullName.show()
        self.SelectFullName.last_name = self.lineEdit_LastName.text()
        pass

    #
    #   FUNCTION IMPLEMENT
    #
    def NameCoutDescription_FilterNameCountList(self, name_count_list):
        name_count_filtered_list = name_count_list.copy()
        for name_count_item in name_count_list:
            name_count = name_count_item[0][0] + name_count_item[0][1] + name_count_item[0][2]
            if "（凶）" in self.name_count_description[name_count - 1]:
                name_count_filtered_list.remove(name_count_item)
                continue
            if self.radioButton_Gender_Girl.isChecked() and "女性不宜此數" in self.name_count_description[name_count - 1]:
                name_count_filtered_list.remove(name_count_item)
                continue
            if (self.checkBox_HalfLuck.isChecked() == False and "（半吉）" in self.name_count_description[name_count - 1]):
                name_count_filtered_list.remove(name_count_item)
                continue
        return name_count_filtered_list
    
    #
    # type_index: 0: 天/人; 1: 人/地; 2: 人/外; 3: 地/外; 4: 人/總; 5: 地/總
    # level_1/level_2: element 5 for 5 level
    #
    def GradeCalculate(self, type_index, level_1, level_2):
        grade_list = [[90, 60, 50, 50, 80, "天", "人"], [60, 90, 65, 65, 70, "人", "地"], [60, 80, 55, 45, 75, "人", "外"], \
        [65, 75, 45, 45, 70, "地", "外"], [65, 90, 55, 30, 80, "人", "總"], [80, 70, 40, 55, 70, "地", "總"]]
    
        grade = grade_list[type_index][4]
        grade_string = grade_list[type_index][5] + grade_list[type_index][6] + "和"
        if (level_1 + 1) % 5 == level_2:
            grade = grade_list[type_index][0]
            grade_string = grade_list[type_index][5] + "生" + grade_list[type_index][6]
        elif (level_2 + 1) % 5 == level_1:
            grade = grade_list[type_index][1]
            grade_string = grade_list[type_index][6] + "生" + grade_list[type_index][5]
        elif (level_1 + 2) % 5 == level_2:
            grade = grade_list[type_index][2]
            grade_string = grade_list[type_index][5] + "剋" + grade_list[type_index][6]
        elif (level_2 + 2) % 5 == level_1:
            grade = grade_list[type_index][3]
            grade_string = grade_list[type_index][6] + "剋" + grade_list[type_index][5]

        return grade, grade_string

    
    def FiveLevel_GetNameCount(self):
        last_name_count = self.spinBox_LastNameCount.value()
        five_level_result_list = []
        for name1_count in range(self.spinBox_NameCount_Min.value(), self.spinBox_NameCount_Max.value()+1):
            for name2_count in range(self.spinBox_NameCount_Min.value(), self.spinBox_NameCount_Max.value()+1):
                sky_count = last_name_count
                person_count = last_name_count + name1_count
                ground_count = name1_count + name2_count
                appearance_count = name2_count + 1
                total_count = last_name_count + name1_count + name2_count
                
                sky_element = (sky_count % 10) + 1 // 2 % 5
                person_element = (person_count % 10) + 1 // 2 % 5
                ground_element = (ground_count % 10) + 1 // 2 % 5
                appearance_element = (appearance_count % 10) + 1 // 2 % 5
                total_element = (total_count % 10) + 1 // 2 % 5

                compare_list = [[0, sky_element, person_element], [1, person_element, ground_element], [2, person_element, appearance_element], \
                [3, ground_element, appearance_element], [4, person_element, total_element], [5, ground_element, total_element]]

                is_hit = True
                # result_string = ""
                grade_string = ""
                grade_total = 0
                grade_list = []
                for compare_item in compare_list:
                    grade, grade_string = self.GradeCalculate(compare_item[0], compare_item[1], compare_item[2])

                    if grade < self.spinBox_FiveLevel_Threshold.value():
                        is_hit = False
                        break
                    grade_total = grade_total + grade
                    
                    grade_list.append([grade, grade_string])
                if is_hit == False:
                    continue

                five_level_result_list.append([[last_name_count, name1_count, name2_count], grade_list])
                    
                # print("[12, " + str(name1) + ", " + str(name2) + "]: " + str (grade_total) + "\n" + result_string)
                # print("[12, " + str(name1) + ", " + str(name2) + "]: " + str (grade_total))

                pass        
        
            pass    
        return five_level_result_list
    
    
    
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
