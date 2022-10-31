# Import
import re #regex
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Import Assets
from assets.lang_dictionaries import *
from assets.setUp_information import *

#--------------------------------------- setUP FUNCTIONS
#text checker
def text_checker(text2check):
    # A function that via Regex will check the text and will tell whether it has Hanzi Characters, Latin Characters or Zhuyin Characters. Also it will tell how many letters it does have
    hanzi_list = "[\u4e00-\u9fff]+"
    latin_list = "[\0000-\u007F]+"
    zhuyin_list = "[\u3100-\u31A0]+"

    textLength = len(text2check) - 1

    if (re.search(hanzi_list, text2check)):
        comment = "The text you input: \n- Contain Hanzi \n- Contains (", textLength, ") characters"
        messagebox.showinfo(title="Info about the text you input", message=comment)
    else:
        pass
    if (re.search(zhuyin_list, text2check)):
        comment = "The text you input: \n- Contain Zhuyin characters \n- Contains (", textLength, ") characters"
        messagebox.showinfo(title="Info about the text you input", message=comment)
    else:
        pass
    if (re.search(latin_list, text2check)):
        comment = "The text you input: \n- Contain letters of Latin Script \n- Contains (", textLength, ") letters"
        messagebox.showinfo(title="Info about the text you input", message=comment)
    else:
        pass
#separate letters
def separate_letters(text):
    # Put spaces after every single letter/character (this is useful when outputting pinyin or jyutping)
    with_spaces = (" ".join(text))
#get translation
def get_translation(text, dictionary):
    # Translate the text using a dictionary, the dictionary will help to replace all of the characters that can find in common between the text and the dictionary
    for word, replace in dictionary.items():
        text = text.replace(word, replace)
    print("Translation done successfully:")
    return(text)
