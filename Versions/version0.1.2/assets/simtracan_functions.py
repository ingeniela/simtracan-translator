import re
from assets.dictionaries_for_languages import *

# translation and language selection function
class simtracan:
    def option_selection(choice):
        option_error = False
        if choice == "SM":  # Simplified Mandarin Chinese
            lang_name = "Simplified Mandarin Chinese"
            return ("You just selected:", lang_name)
        elif choice == "TM":  # Traditional Mandarin Chinese
            lang_name = "Traditional Mandarin Chinese"
            return("You just selected:", lang_name)
        elif choice == "MP":  # Mandarin Chinese Pinyin
            lang_name = "Mandarin Chinese Pinyin"
            return("You just selected:", lang_name)
        elif choice == "C":  # Cantonese Chinese
            lang_name = "Cantonese Chinese"
            return("You just selected:", lang_name)
        elif choice == "CP":  # Cantonese Chinese Pinyin
            lang_name = "Cantonese Chinese Pinyin"
            return("You just selected:", lang_name)
        else:
            return("Sorry, we couldn't understand the option you selected")
            option_error = True

    def get_translation(from_lang, to_lang, text):
        # language selection
        translation = True   # It can go to translate directly, in case of error, it will go to 'False'
        # Possible User Errors
        if from_lang == to_lang:
            translation = False
            error_found = "Error: You selected the same language twice"
        else:
            pass
        #if from_lang or to_lang == "SM" or "TM" or "MP" or "C" or "CP":
            #pass
        #else:
            #translation = False
            #error_found = "Error: There was an error while selecting the first language"
        # Simplified Mandarin to ...
        if from_lang == 'SM' and to_lang == 'TM':
            dictionary = sm2tm_dict
        elif from_lang == 'SM' and to_lang == 'MP':
            dictionary = sm2mp_dict
        elif from_lang == 'SM' and to_lang == 'C':
            dictionary = sm2c_dict
        # Traditional Mandarin to ...
        if from_lang == 'TM' and to_lang == 'SM':
            dictionary = tm2sm_dict
        elif from_lang == 'TM' and to_lang == 'MP':
            dictionary = tm2mp_dict
        elif from_lang == 'TM' and to_lang == 'C':
            dictionary = tm2c_dict
        # Mandarin Pinyin to ...
        if from_lang == 'MP' and to_lang == 'SM':
            dictionary = mp2sm_dict
        elif from_lang == 'MP' and to_lang == 'TM':
            dictionary = mp2tm_dict
        elif from_lang == 'MP' and to_lang == 'C':
            dictionary = mp2c_dict
        # Cantonese to ...
        if from_lang == 'C' and to_lang == 'TM':
            dictionary = c2tm_dict
        elif from_lang == 'C' and to_lang == 'SM':
            dictionary = c2sm_dict
        elif from_lang == 'C' and to_lang == 'CP':
            dictionary = c2cp_dict
        # Cantonese Pinyin to ...
        if from_lang == 'CP' and to_lang == 'SM':
            dictionary = cp2sm_dict
        elif from_lang == 'CP' and to_lang == 'TM':
            dictionary = cp2tm_dict
        elif from_lang == 'CP' and to_lang == 'C':
            dictionary = cp2c_dict
        # translation
        if translation == True:
            chinese_characters = "[\u4e00-\u9fff]+"  # chinese characters
            if (re.search(chinese_characters, text)):
                # verification for chinese characters
                for word, replace in dictionary.items():
                    text = text.replace(word, replace)
                print("\nTranslation done!:")
                return(text)
            else:
                return("Translation error: Your text doesn't contain Chinese characters!")
        else:
            return(error_found)