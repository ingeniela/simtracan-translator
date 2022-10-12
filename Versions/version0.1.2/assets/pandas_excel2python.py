import pandas as pd

### From Excel.xlsx to Python
original_file = pd.read_excel(r'C:\Users\Jose Barazarte\Downloads\chinesefontdesign.com-2017-08-27_10-21-34_952752/c22cp.xlsx')
to_python = original_file.to_dict('split') # split

print(to_python)
# Output: {'index': [0, 1], 'columns': ['Column A':'Column B'], 'data': [['Data from Column A':'Data from Column B']]}

### From Python to Dictionary Type
# Dictionary used in replace() {original values : replacement}
for_replacement = {"{'index': [": "{", ", 'columns': " : "",  ", 'data': [" : "", "]]}": "}", "', '": "': '", "], [": " ,  "}

to_dictionary = input("\n(From Python to Dictionary Type, please input the text):\n")

for value, replace in for_replacement.items():
    to_dictionary = to_dictionary.replace(value, replace)

print("\n", to_dictionary)
# Output: {[0, 1]['Column A':'Column B']['Data from Column A':'Data from Column B'}

### Delete numbers in Dictionary
# Dictionary used in replace() {original values : replacement}
numbers_delete = {"0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", ", , ,": "", "   ":"", "{  ]":"{", "][":"][{"}

clean_numbers = input("\n(Clean the numbers in Dictionary Type, please input the text)\n")

for value, replace in numbers_delete.items():
    clean_numbers = clean_numbers.replace(value, replace)

print("\n", clean_numbers)
# Output: {['Column A':'Column B'][{'Data from Column A':'Data from Column B'}