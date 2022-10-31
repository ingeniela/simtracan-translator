# Import Tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk, font
from tkinter import filedialog

# Import Assets
from assets.setUp_functions import *
from assets.setUp_information import *

#--------------------------------------- Gui FUNCTIONS
#new window of information
def show_info():
    new_window = Tk()
    new_window.geometry("325x325")
    new_window.title("Simtracan Translator (SMTC 翻译) - Info")
    new_window.config(background="black")
    new_window.config(padx=10, pady=10)
    new_window.resizable(True, False)

    info_text = Text(new_window,
        font = (font_aspect, 12),
        fg = 'yellow',
        bg = "black",
        width = 150,
        height = 14)
    info_text.insert(INSERT, info.presentation)
    info_text.configure(wrap="word")
    info_text.pack()

    link_text = Text(new_window,
                      font=(font_aspect, 12),
                      fg='orange',
                      bg="black",
                      width=150,
                     height = 5)
    link_text.insert(INSERT, "Check the GitHub: \n github.com/danielabai/simtracan-translator")
    link_text.pack()

#text checker
def check_text():
    text_checker(input_text.get("1.0", END))

#language A selectiion
def select_languageA(self):
    if(clicked_langA.get() == (langA_list[1])):
        print("You selected Mandarin Chinese Simplified as the language of the text you input")
    elif(clicked_langA.get() == (langA_list[2])):
        print("You selected Mandarin Chinese Traditional as the language of the text you input")
    elif(clicked_langA.get() == (langA_list[3])):
        show_notification("Translating from Pinyin to any other language is a feature that is not accurate yet")
        print("You selected Mandarin Pinyin as the language of the text you input")
    elif(clicked_langA.get() == (langA_list[4])):
        print("You selected Cantonese as the language of the text you input")
    elif(clicked_langA.get() == (langA_list[5])):
        show_notification("Translating from Cantonese Pinyin/Jyutping to any other language is a feature that is not accurate yet")
        print("You selected Cantonese Pinyin as the language of the text you input")
    elif(clicked_langA.get() == (langA_list[6])):
        show_notification("Translating from Zhuyin to any other language is a feature that is not accurate yet")
        print("You selected Chinese Zhuyin as the language of the text you input")
    elif (clicked_langA.get() == (langA_list[7])):
        print("You selected Chinese Unicode as the language of the text you input")
#language B selectiion
def select_languageB(self):
    # clicked lang B
    if(clicked_langB.get() == (langB_list[1])):
        print("You selected Mandarin Chinese Simplified")
    elif(clicked_langB.get() == (langB_list[2])):
        print("You selected Mandarin Chinese Traditional")
    elif(clicked_langB.get() == (langB_list[3])):
        print("You selected Mandarin Pinyin")
    elif(clicked_langB.get() == (langB_list[4])):
        print("You selected Cantonese")
    elif(clicked_langB.get() == (langB_list[5])):
        print("You selected Cantonese Pinyin")
    elif(clicked_langB.get() == (langB_list[6])):
        print("You selected Chinese Zhuyin")
    elif (clicked_langA.get() == (langB_list[7])):
        print("You selected Chinese Unicode")

#language translation
def languages_translation():
    text_from_user = input_text.get("1.0", END)
    spaces_text = (" ".join(text_from_user))
    # Errors
    if (clicked_langA.get() == (langA_list[0])) or (clicked_langB.get() == (langB_list[0])):
        show_error("One of the options you input was incorrect. Please select a language.")
    # Simplified Mandarin TO...
    if (clicked_langA.get() == (langA_list[1])) and (clicked_langB.get() == (langB_list[1])):
        show_error("You selected the same language two times.")
    if (clicked_langA.get() == (langA_list[1])) and (clicked_langB.get() == (langB_list[2])):
        translate_text = (get_translation(text_from_user, sm2tm_dict))
        insert_text(translate_text)
        print(translate_text)
    if (clicked_langA.get() == (langA_list[1])) and (clicked_langB.get() == (langB_list[3])):
        translate_text = (get_translation(spaces_text, sm2mp_dict))
        insert_text(translate_text)
        print(translate_text)
    if (clicked_langA.get() == (langA_list[1])) and (clicked_langB.get() == (langB_list[4])):
        translate_text = (get_translation(text_from_user, sm2c_dict))
        insert_text(translate_text)
        print(translate_text)
    if (clicked_langA.get() == (langA_list[1])) and (clicked_langB.get() == (langB_list[5])):
        first_translation = (get_translation(spaces_text, sm2c_dict))
        second_translation = (get_translation(first_translation, c2cp_dict))
        insert_text(second_translation)
        print(second_translation)
    if (clicked_langA.get() == (langA_list[1])) and (clicked_langB.get() == (langB_list[6])):
        first_translation = (get_translation(spaces_text, sm2mp_dict))
        second_translation = (get_translation(first_translation, ch2cz_dict))
        correction = (get_translation(second_translation, incorrect2correct_dict))
        insert_text(correction)
        print(correction)
    if (clicked_langA.get() == (langA_list[1])) and (clicked_langB.get() == (langB_list[7])):
        translate_text = (get_translation(text_from_user, ch2cu_dict))
        insert_text(translate_text)
        print(translate_text)
    # Traditional Mandarin TO...
    if (clicked_langA.get() == (langA_list[2])) and (clicked_langB.get() == (langB_list[1])):
        translate_text = (get_translation(text_from_user, tm2sm_dict))
        insert_text(translate_text)
        print(translate_text)
    if (clicked_langA.get() == (langA_list[2])) and (clicked_langB.get() == (langB_list[2])):
        show_error("You selected the same language two times.")
    if (clicked_langA.get() == (langA_list[2])) and (clicked_langB.get() == (langB_list[3])):
        first_translation = (get_translation(spaces_text, tm2sm_dict))
        final_translation = (get_translation(first_translation, sm2mp_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[2])) and (clicked_langB.get() == (langB_list[4])):
        first_translation = (get_translation(text_from_user, tm2sm_dict))
        final_translation = (get_translation(first_translation, sm2c_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[2])) and (clicked_langB.get() == (langB_list[5])):
        first_translation = (get_translation(spaces_text, tm2sm_dict))
        second_translation = (get_translation(first_translation, sm2c_dict))
        final_translation = (get_translation(second_translation, c2cp_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[2])) and (clicked_langB.get() == (langB_list[6])):
        first_translation = (get_translation(text_from_user, tm2sm_dict))
        second_translation = (get_translation(first_translation, sm2mp_dict))
        final_translation = (get_translation(second_translation, ch2cz_dict))
        correction = (get_translation(final_translation, incorrect2correct_dict))
        insert_text(correction)
        print(correction)
    if (clicked_langA.get() == (langA_list[2])) and (clicked_langB.get() == (langB_list[7])):
        first_translation = (get_translation(text_from_user, ch2cu_dict))
        insert_text(first_translation)
        print(first_translation)
    # Mandarin Pinyin TO...
    if (clicked_langA.get() == (langA_list[3])) and (clicked_langB.get() == (langB_list[1])):
        first_translation = (get_translation(text_from_user, mp2sm_dict))
        insert_text(first_translation)
        print(first_translation)
    if (clicked_langA.get() == (langA_list[3])) and (clicked_langB.get() == (langB_list[2])):
        first_translation = (get_translation(text_from_user, mp2sm_dict))
        final_translation = (get_translation(first_translation, sm2tm_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[3])) and (clicked_langB.get() == (langB_list[3])):
        show_error("You selected the same language two times.")
    if (clicked_langA.get() == (langA_list[3])) and (clicked_langB.get() == (langB_list[4])):
        first_translation = (get_translation(text_from_user, mp2sm_dict))
        final_translation = (get_translation(first_translation, sm2c_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[3])) and (clicked_langB.get() == (langB_list[5])):
        first_translation = (get_translation(text_from_user, mp2sm_dict))
        second_translation = (get_translation(first_translation, sm2c_dict))
        final_translation = (get_translation(second_translation, c2cp_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[3])) and (clicked_langB.get() == (langB_list[6])):
        first_translation = (get_translation(text_from_user, ch2cz_dict))
        correction = (get_translation(first_translation, incorrect2correct_dict))
        insert_text(correction)
        print(correction)
    if (clicked_langA.get() == (langA_list[3])) and (clicked_langB.get() == (langB_list[7])):
        first_translation = (get_translation(text_from_user, mp2sm_dict))
        final_translation = (get_translation(first_translation, ch2cu_dict))
        insert_text(final_translation)
        print(final_translation)
    # Cantonese TO...
    if (clicked_langA.get() == (langA_list[4])) and (clicked_langB.get() == (langB_list[1])):
        translate_text = (get_translation(text_from_user, c2sm_dict))
        insert_text(translate_text)
    if (clicked_langA.get() == (langA_list[4])) and (clicked_langB.get() == (langB_list[2])):
        first_translation = (get_translation(text_from_user, c2sm_dict))
        final_translation = (get_translation(first_translation, sm2tm_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[4])) and (clicked_langB.get() == (langB_list[3])):
        first_translation = (get_translation(spaces_text, c2sm_dict))
        final_translation = (get_translation(first_translation, sm2mp_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[4])) and (clicked_langB.get() == (langB_list[4])):
        show_error("You selected the same language two times.")
    if (clicked_langA.get() == (langA_list[4])) and (clicked_langB.get() == (langB_list[5])):
        translate_text = (get_translation(spaces_text, c2cp_dict))
        insert_text(translate_text)
        print(translate_text)
    if (clicked_langA.get() == (langA_list[4])) and (clicked_langB.get() == (langB_list[6])):
        first_translation = (get_translation(text_from_user, c2sm_dict))
        second_translation = (get_translation(first_translation, sm2mp_dict))
        third_translation = (get_translation(second_translation, ch2cz_dict))
        correction = (get_translation(correction, incorrect2correct_dict))
        insert_text(correction)
        print(correction)
    if (clicked_langA.get() == (langA_list[4])) and (clicked_langB.get() == (langB_list[7])):
        first_translation = (get_translation(text_from_user, c2sm_dict))
        final_translation = (get_translation(first_translation, ch2cu_dict))
        insert_text(final_translation)
        print(final_translation)
    # Cantonese Pinyin TO...
    if (clicked_langA.get() == (langA_list[5])) and (clicked_langB.get() == (langB_list[1])):
        first_translation = (get_translation(text_from_user, cp2c_dict))
        final_translation = (get_translation(first_translation, c2sm_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[5])) and (clicked_langB.get() == (langB_list[2])):
        first_translation = (get_translation(text_from_user, cp2c_dict))
        second_translation = (get_translation(first_translation, c2sm_dict))
        final_translation = (get_translation(second_translation, sm2tm_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[5])) and (clicked_langB.get() == (langB_list[3])):
        first_translation = (get_translation(spaces_text, cp2c_dict))
        second_translation = (get_translation(first_translation, c2sm_dict))
        final_translation = (get_translation(second_translation, sm2mp_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[5])) and (clicked_langB.get() == (langB_list[4])):
        first_translation = (get_translation(text_from_user, cp2c_dict))
        insert_text(first_translation)
        print(first_translation)
    if (clicked_langA.get() == (langA_list[5])) and (clicked_langB.get() == (langB_list[5])):
        show_error("You selected the same language two times.")
    if (clicked_langA.get() == (langA_list[5])) and (clicked_langB.get() == (langB_list[6])):
        first_translation = (get_translation(text_from_user, cp2c_dict))
        second_translation = (get_translation(first_translation, c2sm_dict))
        third_translation = (get_translation(second_translation, sm2mp_dict))
        final_translation = (get_translation(third_translation, ch2cz_dict))
        correction = (get_translation(final_translation, incorrect2correct_dict))
        insert_text(correction)
        print(correction)
    if (clicked_langA.get() == (langA_list[5])) and (clicked_langB.get() == (langB_list[7])):
        first_translation = (get_translation(text_from_user, cp2c_dict))
        second_translation = (get_translation(first_translation, c2sm_dict))
        final_translation = (get_translation(second_translation, ch2cu_dict))
        insert_text(final_translation)
        print(final_translation)
    # Chinese Zhuyin TO...
    if (clicked_langA.get() == (langA_list[6])) and (clicked_langB.get() == (langB_list[1])):
        first_translation = (get_translation(text_from_user, cz2ch_dict))
        final_translation = (get_translation(first_translation, mp2sm_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[6])) and (clicked_langB.get() == (langB_list[2])):
        first_translation = (get_translation(text_from_user, cz2ch_dict))
        second_translation = (get_translation(first_translation, mp2sm_dict))
        final_translation = (get_translation(second_translation, sm2tm_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[6])) and (clicked_langB.get() == (langB_list[3])):
        first_translation = (get_translation(text_from_user, cz2ch_dict))
        insert_text(first_translation)
        print(first_translation)
    if (clicked_langA.get() == (langA_list[6])) and (clicked_langB.get() == (langB_list[4])):
        first_translation = (get_translation(text_from_user, cz2ch_dict))
        second_translation = (get_translation(first_translation, mp2sm_dict))
        final_translation = (get_translation(second_translation, sm2c_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[6])) and (clicked_langB.get() == (langB_list[5])):
        first_translation = (get_translation(text_from_user, cz2ch_dict))
        second_translation = (get_translation(first_translation, mp2sm_dict))
        third_translation = (get_translation(second_translation, sm2c_dict))
        final_translation = (get_translation(third_translation, c2cp_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[6])) and (clicked_langB.get() == (langB_list[6])):
        show_error("You selected the same language two times.")
    if (clicked_langA.get() == (langA_list[6])) and (clicked_langB.get() == (langB_list[7])):
        first_translation = (get_translation(text_from_user, cz2ch_dict))
        second_translation = (get_translation(first_translation, mp2sm_dict))
        final_translation = (get_translation(second_translation, ch2cu_dict))
        insert_text(final_translation)
        print(final_translation)
    # Chinese Unicode TO...
    if (clicked_langA.get() == (langA_list[7])) and (clicked_langB.get() == (langB_list[1])):
        translate_text = (get_translation(text_from_user, cu2ch_dict))
        insert_text(translate_text)
        print(translate_text)
    if (clicked_langA.get() == (langA_list[7])) and (clicked_langB.get() == (langB_list[2])):
        first_translation = (get_translation(text_from_user, cu2ch_dict))
        insert_text(first_translation)
        print(translate_text)
    if (clicked_langA.get() == (langA_list[7])) and (clicked_langB.get() == (langB_list[3])):
        first_translation = (get_translation(text_from_user, cu2ch_dict))
        final_translation = (get_translation(first_translation, sm2mp_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[7])) and (clicked_langB.get() == (langB_list[4])):
        first_translation = (get_translation(text_from_user, cu2ch_dict))
        final_translation = (get_translation(first_translation, sm2c_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[7])) and (clicked_langB.get() == (langB_list[5])):
        first_translation = (get_translation(text_from_user, cu2ch_dict))
        second_translation = (get_translation(first_translation, sm2c_dict))
        final_translation = (get_translation(second_translation, c2cp_dict))
        insert_text(final_translation)
        print(final_translation)
    if (clicked_langA.get() == (langA_list[7])) and (clicked_langB.get() == (langB_list[6])):
        first_translation = (get_translation(text_from_user, cu2ch_dict))
        second_translation = (get_translation(first_translation, sm2mp_dict))
        final_translation = (get_translation(second_translation, ch2cz_dict))
        correction = (get_translation(final_translation, incorrect2correct_dict))
        insert_text(correction)
        print(correction)
    if (clicked_langA.get() == (langA_list[7])) and (clicked_langB.get() == (langB_list[7])):
        show_error("You selected the same language two times.")

#helper: insert text
def insert_text(text):
    text2use = text
    output_text.delete("1.0", END)
    output_text.insert(INSERT, text2use)

#clean box
def input_clean_box():
    input_text.delete("1.0", END)
def output_clean_box():
    output_text.delete("1.0", END)

#message box
def show_error(message):
    message2use = message
    messagebox.showerror(title='We found an error', message=message2use)
def show_notification(message):
    message2use = message
    messagebox.askokcancel(title='Notification', message=message2use)

#fielog methods
def open_file():
    filepath = filedialog.askopenfilename(title="Open a file to get the text", defaultextension='.txt',filetypes=[("Text file",".txt"),("HTML file", ".html")])
    file = open(filepath, 'r')
    input_text.insert(INSERT, (file.read()))
    file.close()
def save_file():
    file = filedialog.asksaveasfile(title="Save the translation in a file", defaultextension='.txt',filetypes=[("Text file",".txt"),("HTML file", ".html"),("All files", ".*")])
    if file is None:
        return
    filetext = str(output_text.get(1.0, END))
    file.write(filetext)
    file.close()

#--------------------------------------- Software WINDOW
# ASPECTS OF WINDOW
simtracan_bg = '#FF6A60'
font_aspect = ("Helvetica")

button_color = '#ff9d80'
button_activeColor = '#ffac94'
button_fg = 'black'

optionMenu_color = '#ff5a4f'
optionMenu_activeColor = '#fc6a60'
buttonMain_color = '#bf7a5a'
buttonMain_activeColor = '#d48763'
buttonMain_fg = 'white'

textArea_color = 'white'

## Tkinter Window
simtracan = Tk()
simtracan.geometry("800x600")
simtracan.config(padx=30, pady=30)
simtracan.title("Simtracan Translator (SMTC 翻译) - Daniela Bai")
simtracan.config(background=simtracan_bg)

#Logo
simtracan_icon = PhotoImage(file='gui/logoHD.png')
simtracan.iconphoto(True, simtracan_icon)

#Reasize configurations
simtracan.resizable(True, True)
simtracan.rowconfigure(0, weight=0)
simtracan.rowconfigure(1, weight=2)
simtracan.rowconfigure(2, weight=0)
simtracan.rowconfigure(3, weight=0)
simtracan.rowconfigure(4, weight=0)
simtracan.rowconfigure(5, weight=2)
simtracan.rowconfigure(6, weight=0)
simtracan.rowconfigure(7, weight=0)
simtracan.columnconfigure(0, weight=1)
simtracan.columnconfigure(1, weight=1)

#--------------------------------------- Title
title_label = Label(simtracan,
                    text = "Simtracan Translator (SMTC 翻译)",
                    font=(font_aspect, 20),
                    fg= "white",
                    bg= simtracan_bg)
title_label.grid(row=0, column=0, sticky = "NSE", pady=10, padx=30)

info_button = tk.Button(simtracan,
                        text="More info",
                        font = font_aspect,
                        fg = 'black',
                        activeforeground= 'black',
                        bg = 'white',
                        activebackground= 'grey',
                        command=show_info,
                        width = 20,
                        height = 1)
info_button.grid(row=0, column=1, sticky = "NSW", pady=20, padx=30)

#------------------------ LANG A OPTIONS
## OptionMenu from_language (langA)
langA_list = ["Select a language", "Simplified Mandarin", "Traditional Mandarin", "Mandarin Pinyin", "Cantonese", "Cantonese Pinyin/Jyutping", "Chinese Zhuyin", "Chinese Unicode"]
clicked_langA = StringVar()
clicked_langA.set(langA_list[0])

from_language = OptionMenu(simtracan, clicked_langA, *langA_list, command = select_languageA)
from_language.config(font = font_aspect,
                     fg = 'white',
                     activeforeground= 'white',
                     bg = optionMenu_color,
                     activebackground = optionMenu_activeColor,
                     height = 2,
                     width = 30)
from_language.grid(row=1, column=1, sticky = "WE", pady=30, padx=20)
## Input Text (langA)
input_text = Text(simtracan,
                  font=(font_aspect,12),
                  bg = textArea_color,
                  height=20,
                  width=70)
input_text.grid(row=1, column=0, sticky= "NWE", pady=5, padx=10)

#Clean Button
clean_button = Button(simtracan,
                      text="Clean box",
                      font = font_aspect,
                      fg = button_fg,
                      bg = button_color,
                      activebackground= button_activeColor,
                      command=input_clean_box)
clean_button.grid(row=2, column=0, sticky="NE", pady=5, padx=10)

#Check button
check_button = Button(simtracan,
                      text="Check text",
                      font = font_aspect,
                      fg = button_fg,
                      bg= button_color,
                      activebackground= button_activeColor,
                      command=check_text)
check_button.grid(row=2, column=0,  sticky= "NW", pady=5, padx=10)

#Open a File Button / Get text from a File
openFile_button = Button(simtracan,
                         text="Get text from a file",
                         font = font_aspect,
                         fg = button_fg,
                         bg= button_color,
                         activebackground=button_activeColor,
                         command=open_file)
openFile_button.grid(row=3, column=0,  sticky= "NW", pady=5, padx=10)

#------------------------ TRANSLATION AND OTHERS
## Translate Button
translate_button = Button(simtracan,
                          bg = buttonMain_color,
                          activebackground = buttonMain_activeColor,
                          text="Translate text",
                          font = font_aspect,
                          fg = buttonMain_fg,
                          activeforeground='white',
                          command=languages_translation,
                          width = 70)
translate_button.grid(row=4, column=0, columnspan = 1, sticky = "NWE", pady=30, padx=5)
#------------------------
## OptionMenu to_language (langB)
langB_list = ["Select a language","Simplified Mandarin", "Traditional Mandarin", "Mandarin Pinyin", "Cantonese", "Cantonese Pinyin/Jyutping", "Chinese Zhuyin", "Chinese Unicode"]
clicked_langB = StringVar()
clicked_langB.set(langB_list[0])

to_language = OptionMenu(simtracan, clicked_langB, *langB_list, command = select_languageB)
to_language.config(font = font_aspect,
                   fg = 'white',
                   activeforeground= 'white',
                   bg = optionMenu_color,
                   activebackground = optionMenu_activeColor,
                   height = 2,
                   width = 30)
to_language.grid(row=5, column=1, sticky = "WE", pady=30, padx=20)

## Output text (Output text in LangB)
output_text = Text(simtracan,
                   bg = textArea_color,
                   font=(font_aspect,12),
                   height=20,
                   width=70)
output_text.grid(row=5, column=0, sticky= "SWE", pady=5, padx=10)
output_text.insert(INSERT, "The translation will be shown here")

#Save file button
saveFile_button = Button(simtracan,
                         text="Save translation in a file",
                         font = font_aspect,
                         fg = button_fg,
                         bg= button_color,
                         activebackground= button_activeColor,
                         command=save_file)
saveFile_button.grid(row=6, column=0, sticky= "NW", pady=5, padx=10)

#Clean Box Button
clean_button = Button(simtracan,
                      text="Clean box",
                      font = font_aspect,
                      fg = button_fg,
                      bg = button_color,
                      activebackground= button_activeColor,
                      command=output_clean_box)
clean_button.grid(row=6, column=0, sticky="NE", pady=5, padx=10)

#---------------------------------------
#Window Mainloop
simtracan.mainloop()