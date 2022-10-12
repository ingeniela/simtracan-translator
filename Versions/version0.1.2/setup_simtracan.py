## set up: import files
from assets.simtracan_functions import *
from assets.simtracan_information import *

### set up / Screen: Welcoming
print("\nWelcome to Simtracan Translator", "(Version: ", version_now, ")\n")

###  set up / Screen: Options
selection_menu = [
    "\n✎SM: Simplified Mandarin Chinese\n✎TM: Traditional Mandarin Chinese\n✎MP: Mandarin Chinese Pinyin\n✎C: Cantonese Chinese\n✎CP: Cantonese Chinese Pinyin",
    ]

# user input text to translate
user_input = str(input("Please, input the text you want to translate\n")) #个 個 from_TM
setup_error = False
# language A selection: input_text language
print('\nIn what language is the text', '(', user_input, ')', 'you just input?', selection_menu[0])
lang_a = str(input("Please select a code (like SM, TM, MP, C, CP): "))
print(simtracan.option_selection(lang_a))
# language B selection: translation language
print('\nIn what language do you want to translate the text?', selection_menu[0])
lang_b = str(input("Please select a code (like SM, TM, MP, C, CP): "))
print(simtracan.option_selection(lang_b))

###  set up / Screen: Translation Done
if setup_error == True:
    print("\nThere was an error found during the process:")
    print("error found")

if setup_error == False:
    print(simtracan.get_translation(lang_a, lang_b, user_input))

### set up / Screen: Goodbye
print("\n----------------------------------------------")
print("\nThanks for using Simtracan Translator")
print("You can find more info about this software or of its creator Daniela Bai on the official GitHub page!: www.github.com/danielabai/simtracan-translator ")