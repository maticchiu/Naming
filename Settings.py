# -*- coding: utf-8 -*-

def init():
    DATA_PATH = "./Data/"
    global NAME_COUNT_DESCRIPTION_PATH
    NAME_COUNT_DESCRIPTION_PATH = DATA_PATH + "NameCountDescription.txt"
    global NAME_WORDS_PATH
    NAME_WORDS_PATH = DATA_PATH + "NameWords.txt"
    global LAST_NAME_COUNT_PATH
    LAST_NAME_COUNT_PATH = DATA_PATH + "LastNameCount.txt"
    
    global USER_PATH
    USER_PATH = "./User/"
    global SELECTED_NAME_COUNT_PATH
    SELECTED_NAME_COUNT_PATH = USER_PATH + "SelectedNameCount.txt"
    global SELECTED_WORD_PATH
    SELECTED_WORD_PATH = USER_PATH + "SelectedWords.txt"
    global FULL_NAME_PATH
    FULL_NAME_PATH = USER_PATH + "FullName.txt"
