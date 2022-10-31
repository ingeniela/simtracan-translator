# Import Functions
import re

# Import Assets
from assets.setUp_information import *
from assets.lang_dictionaries import *

#--------------------------------------- setUP MAIN CLASS
class Simtracan:
    def welcome():
        print("\nWelcome to Simtracan Translator", "( Version: ", version_now, ")")
        return("")
    def start():
        print("x")
    def translation():
        print(lang_selection(user_input, a_input, b_input))
    def finish():
        print("\n----------------------------------------------")
        print("\nThanks for using Simtracan Translator")
        return("You can find more info about this software or of its creator Daniela Bai on the official GitHub page!: www.github.com/danielabai/simtracan-translator ")
    def error_found():
        print("(Sorry, we found an error and we couldn't advance more)")
        return(Simtracan.finish())

#--------------------------------------- setUP FUNCTIONS
selection_menu = [
   "✎1. Simplified Chinese \ ✎2. Traditional Chinese \ ✎3. Mandarin Pinyin \ ✎4. Cantonese \✎5. Cantonese Chinese Pinyin \ ✎6. Mandarin Chinese Zhuyin\ ✎7. Chinese Unicode",
"✎2. Traditional Chinese \ ✎3. Mandarin Pinyin \ ✎4. Cantonese \✎5. Cantonese Chinese Pinyin \ ✎6. Mandarin Chinese Zhuyin\ ✎7. Chinese Unicode",
"✎1. Simplified Chinese \ ✎3. Mandarin Pinyin \ ✎4. Cantonese \✎5. Cantonese Chinese Pinyin \ ✎6. Mandarin Chinese Zhuyin\ ✎7. Chinese Unicode",
"✎1. Simplified Chinese \ ✎2. Traditional Chinese \ ✎4. Cantonese \✎5. Cantonese Chinese Pinyin \ ✎6. Mandarin Chinese Zhuyin\ ✎7. Chinese Unicode",
"✎1. Simplified Chinese \ ✎2. Traditional Chinese \ ✎3. Mandarin Pinyin \✎5. Cantonese Chinese Pinyin \ ✎6. Mandarin Chinese Zhuyin\ ✎7. Chinese Unicode",
"✎1. Simplified Chinese \ ✎2. Traditional Chinese \ ✎3. Mandarin Pinyin \ ✎4. Cantonese \ ✎6. Mandarin Chinese Zhuyin\ ✎7. Chinese Unicode",
"✎1. Simplified Chinese \ ✎2. Traditional Chinese \ ✎3. Mandarin Pinyin \ ✎4. Cantonese \✎5. Cantonese Chinese Pinyin \ ✎7. Chinese Unicode",
"✎1. Simplified Chinese \ ✎2. Traditional Chinese \ ✎3. Mandarin Pinyin \ ✎4. Cantonese \✎5. Cantonese Chinese Pinyin \ ✎6. Mandarin Chinese Zhuyin"]
# option selection (LANG A)
def languageA_comment(choice, text):
    if choice == "1":
        languageA_comment.selection = "SM"
        print("\nYou selected Simplified Mandarin Chinese")
        text_checker(text)
        return(selection_menu[1])
    elif choice == "2":
        languageA_comment.selection = "TM"
        print("\nYou selected Traditional Mandarin Chinese")
        text_checker(text)
        return(selection_menu[2])
    elif choice == "3":
        languageA_comment.selection = "MP"
        print("\nYou selected Pinyin Mandarin Chinese")
        text_checker(text)
        print(selection_menu[3])
    elif choice == "4":
        languageA_comment.selection = "C"
        print("\nYou selected Cantonese Chinese\n")
        text_checker(text)
        return(selection_menu[4])
    elif choice == "5":
        languageA_comment.selection = "CP"
        print("\nYou selected Cantonese/Jiutping Pinyin\n")
        text_checker(text)
        return(selection_menu[5])
    elif choice == "6":
        languageA_comment.selection = "CZ"
        print("\nYou selected Chinese Zhuyin\n")
        text_checker(text)
        return(selection_menu[6])
    elif choice == "7":
        languageA_comment.selection = "CU"
        print("\nYou selected Chinese Unicode\n")
        text_checker(text)
        return(selection_menu[7])
    else:
        languageA_comment.selection = "error"
        return("\nWe couldn't understand what you meant. Please try again\n")
# option selection (LANG B)
def languageB_comment(choice, text):
    if choice == "1":
        languageB_comment.selection = "SM"
        return("\nYou selected Simplified Mandarin Chinese")
    elif choice == "2":
        languageB_comment.selection = "TM"
        return("\nYou selected Traditional Mandarin Chinese")
    elif choice == "3":
        languageB_comment.selection = "MP"
        return("\nYou selected Pinyin Mandarin Chinese")
    elif choice == "4":
        languageB_comment.selection = "C"
        return("\nYou selected Cantonese Chinese\n")
    elif choice == "5":
        languageB_comment.selection = "CP"
        return("\nYou selected Cantonese/Jiutping Pinyin\n")
    elif choice == "6":
        languageB_comment.selection = "CZ"
        return("\nYou selected Chinese Zhuyin\n")
    elif choice == "7":
        languageB_comment.selection = "CU"
        return("\nYou selected Chinese Unicode\n")
    else:
        languageB_comment.selection = "error"
        return("\nWe couldn't understand what you meant. Please try again\n")
# text checker
def text_checker(text2check):
    hanzi_list = "[\u4e00-\u9fff]+"
    latin_list = "[\0000-\u007F]+"
    zhuyin_list = "[\u3100-\u31A0]+"

    textLength = len(text2check) - 1

    if (re.search(hanzi_list, text2check)):
        print("The text you input: \- Contain Hanzi \- Contains (", textLength, ") characters")
        return("")
    else:
        pass
    if (re.search(zhuyin_list, text2check)):
        print("The text you input: \- Contain Zhuyin characters \- Contains (", textLength, ") characters")
        return ("")
    else:
        pass
    if (re.search(latin_list, text2check)):
        print("The text you input: \- Contain letters of Latin Script \- Contains (", textLength, ") letters")
        return ("")
    else:
        pass
# separate letter
def separate_letters(text):
    # Put spaces after every single letter/character (this is useful when outputting pinyin or jyutping)
    with_spaces = (" ".join(text))

# get translations
def get_translation(text, dictionary):
    for word, replace in dictionary.items():
        text = text.replace(word, replace)
    return(text)

# lang selections
def lang_selection(text, from_lang, to_lang):
        text_from_user = text
        error_found = False
        spaces_text = (" ".join(text_from_user))

        # Errors
        if from_lang == to_lang:
            error_found = True
            error_description = "Selection of the same language"

        if error_found == True:
            print("ERROR:", error_description)
            return("")
        # Simplified Mandarin to ...
        if from_lang == '1' and to_lang == '2':
            translate_text = (get_translation(text_from_user, sm2tm_dict))
            print("Translation done:")
            return(translate_text)
        elif from_lang == '1' and to_lang == '3':
            translate_text = (get_translation(spaces_text, sm2mp_dict))
            print("Translation done:")
            return(translate_text)
        elif from_lang == '1' and to_lang == '4':
            translate_text = (get_translation(text_from_user, sm2c_dict))
            print("Translation done:")
            return(translate_text)
        elif from_lang == '1' and to_lang == '5':
            first_translation = (get_translation(spaces_text, sm2c_dict))
            second_translation = (get_translation(first_translation, c2cp_dict))
            print("Translation done:")
            return(second_translation)
        elif from_lang == '1' and to_lang == '6':
            first_translation = (get_translation(spaces_text, sm2mp_dict))
            second_translation = (get_translation(first_translation, ch2cz_dict))
            correction = (get_translation(second_translation, incorrect2correct_dict))
            print("Translation done:")
            return(correction)
        # Traditional Mandarin to ...
        if from_lang == '2' and to_lang == '1':
            translate_text = (get_translation(text_from_user, tm2sm_dict))
            print("Translation done:")
            return(translate_text)
        elif from_lang == '2' and to_lang == '3':
            first_translation = (get_translation(spaces_text, tm2sm_dict))
            final_translation = (get_translation(first_translation, sm2mp_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '2' and to_lang == '4':
            first_translation = (get_translation(text_from_user, tm2sm_dict))
            final_translation = (get_translation(first_translation, sm2c_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '2' and to_lang == '5':
            first_translation = (get_translation(spaces_text, tm2sm_dict))
            second_translation = (get_translation(first_translation, sm2c_dict))
            final_translation = (get_translation(second_translation, c2cp_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '2' and to_lang == '6':
            first_translation = (get_translation(text_from_user, tm2sm_dict))
            second_translation = (get_translation(first_translation, sm2mp_dict))
            final_translation = (get_translation(second_translation, ch2cz_dict))
            correction = (get_translation(final_translation, incorrect2correct_dict))
            print("Translation done:")
            return(correction)
        elif from_lang == '2' and to_lang == '7':
            first_translation = (get_translation(text_from_user, ch2cu_dict))
            print("Translation done:")
            return(first_translation)
        # Mandarin Pinyin to ...
        if from_lang == '3' and to_lang == '1':
            first_translation = (get_translation(text_from_user, mp2sm_dict))
            print("Translation done:")
            return(first_translation)
        elif from_lang == '3' and to_lang == '2':
            first_translation = (get_translation(text_from_user, mp2sm_dict))
            final_translation = (get_translation(first_translation, sm2tm_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '3' and to_lang == '4':
            first_translation = (get_translation(text_from_user, mp2sm_dict))
            final_translation = (get_translation(first_translation, sm2c_dict))
            insert_text(final_translation)
            print(final_translation)
        elif from_lang == '3' and to_lang == '5':
            first_translation = (get_translation(text_from_user, mp2sm_dict))
            second_translation = (get_translation(first_translation, sm2c_dict))
            final_translation = (get_translation(second_translation, c2cp_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '3' and to_lang == '6':
            first_translation = (get_translation(text_from_user, ch2cz_dict))
            correction = (get_translation(first_translation, incorrect2correct_dict))
            print("Translation done:")
            return(correction)
        elif from_lang == '3' and to_lang == '7':
            first_translation = (get_translation(text_from_user, mp2sm_dict))
            final_translation = (get_translation(first_translation, ch2cu_dict))
            print("Translation done:")
            return(final_translation)
        # Cantonese to ...
        if from_lang == '4' and to_lang == '1':
            translate_text = (get_translation(text_from_user, c2sm_dict))
            print("Translation done:")
            return(translate_text)
        elif from_lang == '4' and to_lang == '2':
            first_translation = (get_translation(text_from_user, c2sm_dict))
            final_translation = (get_translation(first_translation, sm2tm_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '4' and to_lang == '3':
            first_translation = (get_translation(spaces_text, c2sm_dict))
            final_translation = (get_translation(first_translation, sm2mp_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '4' and to_lang == '5':
            translate_text = (get_translation(spaces_text, c2cp_dict))
            print("Translation done:")
            return(translate_text)
        elif from_lang == '4' and to_lang == '6':
            first_translation = (get_translation(text_from_user, c2sm_dict))
            second_translation = (get_translation(first_translation, sm2mp_dict))
            third_translation = (get_translation(second_translation, ch2cz_dict))
            correction = (get_translation(third_translation, incorrect2correct_dict))
            print("Translation done:")
            return(correction)
        elif from_lang == '4' and to_lang == '7':
            first_translation = (get_translation(text_from_user, c2sm_dict))
            final_translation = (get_translation(first_translation, ch2cu_dict))
            print("Translation done:")
            return(final_translation)
        # Cantonese Pinyin to ...
        if from_lang == '5' and to_lang == '1':
            first_translation = (get_translation(text_from_user, cp2c_dict))
            final_translation = (get_translation(first_translation, c2sm_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '5' and to_lang == '2':
            first_translation = (get_translation(text_from_user, cp2c_dict))
            second_translation = (get_translation(first_translation, c2sm_dict))
            final_translation = (get_translation(second_translation, sm2tm_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '5' and to_lang == '3':
            first_translation = (get_translation(spaces_text, cp2c_dict))
            second_translation = (get_translation(first_translation, c2sm_dict))
            final_translation = (get_translation(second_translation, sm2mp_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '5' and to_lang == '4':
            first_translation = (get_translation(text_from_user, cp2c_dict))
            print("Translation done:")
            return(first_translation)
        elif from_lang == '5' and to_lang == '6':
            first_translation = (get_translation(text_from_user, cp2c_dict))
            second_translation = (get_translation(first_translation, c2sm_dict))
            third_translation = (get_translation(second_translation, sm2mp_dict))
            final_translation = (get_translation(third_translation, ch2cz_dict))
            correction = (get_translation(final_translation, incorrect2correct_dict))
            print("Translation done:")
            return(correction)
        elif from_lang == '5' and to_lang == '7':
            first_translation = (get_translation(text_from_user, cp2c_dict))
            second_translation = (get_translation(first_translation, c2sm_dict))
            final_translation = (get_translation(second_translation, ch2cu_dict))
            print("Translation done:")
            return(final_translation)
        # Chinese Zhuyin to ...
        if from_lang == '6' and to_lang == '1':
            first_translation = (get_translation(text_from_user, cz2ch_dict))
            final_translation = (get_translation(first_translation, mp2sm_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '6' and to_lang == '2':
            first_translation = (get_translation(text_from_user, cz2ch_dict))
            second_translation = (get_translation(first_translation, mp2sm_dict))
            final_translation = (get_translation(second_translation, sm2tm_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '6' and to_lang == '3':
            first_translation = (get_translation(text_from_user, cz2ch_dict))
            print("Translation done:")
            return(first_translation)
        elif from_lang == '6' and to_lang == '4':
            first_translation = (get_translation(text_from_user, cz2ch_dict))
            second_translation = (get_translation(first_translation, mp2sm_dict))
            final_translation = (get_translation(second_translation, sm2c_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '6' and to_lang == '5':
            first_translation = (get_translation(text_from_user, cz2ch_dict))
            second_translation = (get_translation(first_translation, mp2sm_dict))
            third_translation = (get_translation(second_translation, sm2c_dict))
            final_translation = (get_translation(third_translation, c2cp_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '6' and to_lang == '7':
            irst_translation = (get_translation(text_from_user, cz2ch_dict))
            second_translation = (get_translation(first_translation, mp2sm_dict))
            final_translation = (get_translation(second_translation, ch2cu_dict))
            print("Translation done:")
            return(final_translation)
        # Chinese Unicode to ...
        if from_lang == '7' and to_lang == '1':
            translate_text = (get_translation(text_from_user, cu2ch_dict))
            print("Translation done:")
            return(translate_text)
        elif from_lang == '7' and to_lang == '2':
            first_translation = (get_translation(text_from_user, cu2ch_dict))
            print("Translation done:")
            return(translate_text)
        elif from_lang == '7' and to_lang == '3':
            first_translation = (get_translation(text_from_user, cu2ch_dict))
            final_translation = (get_translation(first_translation, sm2mp_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '7' and to_lang == '4':
            first_translation = (get_translation(text_from_user, cu2ch_dict))
            final_translation = (get_translation(first_translation, sm2c_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '7' and to_lang == '5':
            first_translation = (get_translation(text_from_user, cu2ch_dict))
            second_translation = (get_translation(first_translation, sm2c_dict))
            final_translation = (get_translation(second_translation, c2cp_dict))
            print("Translation done:")
            return(final_translation)
        elif from_lang == '7' and to_lang == '6':
            first_translation = (get_translation(text_from_user, cu2ch_dict))
            second_translation = (get_translation(first_translation, sm2mp_dict))
            final_translation = (get_translation(second_translation, ch2cz_dict))
            correction = (get_translation(final_translation, incorrect2correct_dict))
            print("Translation done:")
            return(correction)

