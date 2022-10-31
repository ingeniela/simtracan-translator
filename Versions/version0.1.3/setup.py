# Import Assets
from assets.lang_dictionaries import *
from assets.setUp_functions import *
from assets.setUp_information import *

#----------- setUP WELCOMING
print(Simtracan.welcome())

#----------- setUP SELECTION
# user input text to translate
user_input = str(input("Please, input the text you want to translate\n"))
print(text_checker(user_input))
print('In what language is the text', '(', user_input, ')', 'you just input?')
print(selection_menu[0])

# language A selection: input_text language
a_input = input(str("\nPlease select an option (like 1, 2, 3, 4, 5, 6, 7):  "))
print(languageA_comment(a_input, user_input))

# error when selecting, first opportunity
if languageA_comment.selection == "error":
    a_input = input(str("Please select an option (like 1, 2, 3, 4, 5, 6, 7):  "))
    print(languageA_comment(a_input, user_input))
else:
    pass
# error when selecting, second opportunity
if languageA_comment.selection == "error":
    a_input = input(str("Please select an option (like 1, 2, 3, 4, 5):  "))
    print(languageA_comment(a_input, user_input))
else:
    pass

# language B selection: translate text language
b_input = input(str("\nPlease select in what language you want to translate the text you input:  "))
print(languageB_comment(b_input, user_input))

# error when selecting, first opportunity
if languageB_comment.selection == "error":
    b_input = input(str("\nPlease select an option (like 1, 2, 3, 4, 5, 6, 7):  "))
    print(languageB_comment(b_input, user_input))
else:
    pass
# error when selecting, second opportunity
if languageB_comment.selection == "error":
    b_input = input(str("\nPlease select an option (like 1, 2, 3, 4, 5, 6, 7):  "))
    print(languageB_comment(b_input, user_input))
else:
    pass

#----------- setUP TRANSLATION DONE
if languageA_comment.selection == "error" or languageB_comment.selection == "error":
    print(Simtracan.error_found())
else:
    print(lang_selection(user_input, a_input, b_input))
    print(Simtracan.finish())
