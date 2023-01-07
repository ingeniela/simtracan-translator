![Simtracan Logo and Banner](README_SimtracanBanner.jpg)
---
Read in other languages: [English](README.md) · [Español](README.sp.md) · [简体中文](README.zh-s.md) · [繁體中文](README.zh-t.md).
---
## 🀄 Simtracan Translator

**Simtracan Translator** is a translation software that (at its 0.1.3 version) can translate between Mandarin Chinese Simplified, Mandarin Chinese Traditional, Mandarin Chinese Pinyin, Cantonese, Cantonese Pinyin, Chinese Zhuyin and Chinese Unicode Characters.

This software was developed in Python by Daniela Bai (Daniela Barazarte) and it’s main goal is to translate text in multiple derivations of Chinese language without limit of characters, without ads, with great translation and having multiple options in the same translator.

Right now it is able to translate most of the Chinese Characters as it contains a library of more than 18.000 汉字.

### Motivation

Almost two years ago I started to learn Mandarin Chinese and since I am so interested in the language I found some partners to practice with, one of them was a girl from Guangdong who, to play a joke on me, texts messages in Cantonese.

While improving my Chinese, I was also learning Python through a some Youtube tutorial and was willing to putting the knowledge into practice so…as before I couldn't find good translators who could give the translation from Cantonese to Simplified Mandarin to understand my partner's messages, why not build it myself? and that's how Simtracan Translator came to mind.

It was hard at first, considering that I am very new to the programming aspect and not good at Cantonese at all, but even with that I decided to build it.

I started the project and made the decision to call it “Simtracan Translator” as it includes Simplified, Traditional and Cantonese Chinese. Now I am very excited to show this project.

## 🚀 Installation

### Pre-requisites

Python 3.x.x

The only aditional Library that his software use is Regex that comes as default in most of the Python versions.

> After version 1.2.0 it uses Tkinter
> 

### Installation

1. Download the ZIP of this repositor

![How to Download GITHUB ZIP](README_DownloadZip.png)

1. Extract the ZIP you downloaded
2. Use Simtracan Translator Freely
    - You can use the Python Module mode on the version 0.1.3
    - You can use the .exe (Python GUI) mode on the version 0.2.0

## 💻 Usage

### ❗ Please be aware that

Please, be aware that Simtracan Translator’s software could include technical or typographical errors. Also, Simtracan Translator does not warrant that the translations that occur in the software are accurate and/or complete.

---

### Python Module mode

- Open your Python Terminal/Console
- Add the folder of the version you need
- Run the code
    - If you have problems/error in this step, please [contact me](simtracan-translator%20819d2e8f30024ea3833e508558ff7bee.md)
- Start to follow the instructions

**Explanation** 

*(This is the explanation of version 0.1.3, different versions work similar)*

You’ll need to input the text you want to translate

> The software will automatically check the text that you input with a Regex Function
> 

Select a number that tells in what language is that text that you input

Select other number and select the language you want to receive the translation.

> If you selected an option incorrectly, or if you selected the same language twice, the software will display an error message and let you select an option (you have three tries to select the option correctly)
> 

Receive your translation

### Python GUI mode

- Open the .exe
    - If you have problems/error in this step, please [contact me](simtracan-translator%20819d2e8f30024ea3833e508558ff7bee.md)
- Use the translator

**Explanation**

With an interactive interface you’ll need the text you want to translate. You can paste the text on the Text Area, or get it from a file on your computer. 

You can also check the text you input.

> It will count how many characters do your text has, and also tell you whether it is on Pinyin or in Chinese Characters
> 

Then you must select in the option menu what language is that text that you input.

Select in other option menu the language you want to receive the translation

Click on “Translate” and receive your translation

> If you selected an option incorrectly, or if you selected the same language twice, the software will display an error message and let you select an option again
> 

Save your translation by saving it to a file that can be .txt or .html

## 📄 Code

### Glossary

| Abbreviation | Full Word | Meaning |
| --- | --- | --- |
| FL or lang_A | First Language or Language A | is the language you will use to input the text you want to translate |
| SL or lang_B | Second Language or Language B | is the language that the software will choose to generate the translation |
| 1 or SM | Simplified Mandarin | 普通话简体字 - Mandarin Chinese Simplified characters |
| 2 or TM | Traditional Mandarin | 普通话繁體字 - Mandarin Chinese Traditional characters |
| 3 or MP | Mandarin Pinyin | 普通话拼音 - Mandarin Pinyin letters |
| 4 or C | Cantonese | 广东话/粵語 - Cantonese Chinese (dialect from Guangdong) characters |
| 5 or CP | Cantonese Pinyin | 粵拼 - Cantonese Pinyin (Jyutping) letters |
| 6 or CZ | Chinese Zhuyin | ㄅㄆㄇㄈ - Mandarin Chinese Zhuyin ( Bopomofo) |
| 7 or CU | Chinese Unicode | 中文统一码 - Chinese Chracter Encoding |

### Detailed explanation

Even if different versions work slightly different, the way this software works in general is that you’ll input the text you want to translate, then select in what language is that text (lang_A) and then, select in what language you want that text to be translated (lang_B), then it will display the translation for you.

```python
#----------- stage 1
# Input from the user
user_input = "为" 

# Comment about the text user input
OUTPUT: "The text you input: \- Contain Hanzi \- Contains (1) character"

#----------- stage 2
# Selection from the user
from_lang = "1" # tranlation from Simplified Mandarin
to_lang = "2" # translation to Traditional Mandarin

#----------- stage 3
# Final Translation
OUTPUT: "Translation complete: 為"
```

- **Stage 1: Text input**
    
    When you input the text, it is automatically checked by a Regex Formula that will tell whether the text you input has Chinese Characters, Latin Script or Zhuyin, so it can try to guess in what language is the text you input.
    
    - (code)
        
        ```python
        # Example of user input
        user_input = "为"
        
        # Text checker is a checker that will automatically check a text and tell wether it has Chinese Characters, Latin Script or Zhuyin
        def text_checker(user_input):
            hanzi_list = "[\u4e00-\u9fff]+" # Hanzi (Chinese Characters) unicode list
            latin_list = "[\0000-\u007F]+" # Latin Script unicode list
            zhuyin_list = "[\u3100-\u31A0]+" # Zhuyin unicode list
        
            textLength = len(user_input) - 1 # checker of how many letters/character a text have
        
            if (re.search(hanzi_list, user_input)):
                print("The text you input: \- Contain Hanzi \- Contains (", textLength, ") characters")
                return("")
            else:
                pass
            if (re.search(zhuyin_list, user_input)):
                print("The text you input: \- Contain Zhuyin characters \- Contains (", textLength, ") characters")
                return ("")
            else:
                pass
            if (re.search(latin_list, user_input)):
                print("The text you input: \- Contain letters of Latin Script \- Contains (", textLength, ") letters")
                return ("")
            else:
                pass
        
        ```
        
- **Stage 2: Selection of lang_A and lang_B**
    
    When you select in what language is the text you input (lang_A) it will output/show the option you selected. Same case when you select in what language is the text you input (lang_B) it will output/show the option you selected
    
    A function will save your selection of lang_A and your selection of lang_B, this way will know what dictionary to use (langA_to_langB)
    
    - (code)
        
        ```python
        # Input from the user
        user_input = "为"
        
        # Selection from the user
        from_lang = "1" # in what language is the text user input
        to_lang = "2" # in what language user will receive the translation
        
        # Option Selection for languages
           if from_lang == '1' and to_lang == '2': # 1 is Simplified Mandarin, 2 is Traditional Mandarin
               translate_text = (get_translation(user_input, simplified2traditional_dictionary)) # it saves the text the user input and selects the dictionary for languages
               print("Translation done:")
               return(translate_text) # returns the text
        ```
        
- **Stage 3: Translation between lang_A and lang_B**
    
    Then the will pick the text you input and every single character/word will be replaced from the lang_A to lang_B by the .replace() method.
    
    - (code)
        
        ```python
        # Input from the user
        user_input = "为"
        
        # Example of dictionary
        simplified2traditional_dictionary = {'为':'為'}
        
        # Get translation
        def get_translation(user_input, dictionary): # will take the text from the user and also the dictionary that will be used for the translation
            for word, replace in dictionary.items(): # will replace every single character of the user input to one that it can finds in the dictionary
                text = text.replace(word, replace)
            return(text)
        ```
        
    
    The result of the .replace() will be output/show for you
    

## 💯 Sources used

I used multiple resources for making this software work, specially at the time of creating the character wordlist used for translation I needed multiple resources, so I’ll tag them here.

**Chinese Simplified Wordlist**

- [**10.000 character wordlist**](https://www.chinese-forums.com/forums/topic/42692-spreadsheet-of-10000-most-frequent-chinese-words-2397-characters/#replyForm) ([Chinese Forums](https://www.chinese-forums.com/), [user Sparrow](https://www.chinese-forums.com/profile/53860-sparrow/))
- **[中文汉字大全](http://www.ku51.net/hanzi/hanzi1.html)** ([KU51.net](http://www.ku51.net/))

**Chinese Traditional Wordlist**

- [**Chinese Conversion Simplified <> Traditional Characters**](https://www.lexilogos.com/keyboard/chinese_conversion.htm) ([lexilogos.com](https://www.lexilogos.com/))
- **[简体繁体字转换器](http://www.ku51.net/)** ([KU51.net](http://www.ku51.net/))

**Chinese Mandarin Pinyin Wordlist**

- [**Pinyin Conversion Tone Marks <> Numbers](https://www.lexilogos.com/keyboard/pinyin_conversion.htm)** ([lexilogos.com](https://www.lexilogos.com/))
- **[Chinese to Pinyin Converter](http://www.meetmandarin.com/resources/pinyin-converter.html)** ([meetmandarin.com](http://www.meetmandarin.com/))

**Chinese Cantonese and Cantonese Pinyin Wordlist**

- [**Cantonese to Jyutping Converter**](https://www.branah.com/cantonese-to-jyutping) ([branah.com](https://www.branah.com/))
- **[漢字→廣東話/粵語拼音轉換工具](https://hongkongvision.com/tool/cc_py_conv_zh)** ([hongkongvision.com](https://hongkongvision.com/tool/cc_py_conv_zh))

**Chinese Zhuyin Wordlist**

- [Zhuyin fuhao / Bopomofo](https://omniglot.com/chinese/zhuyin.htm) ([omniglot.com](https://omniglot.com/chinese/zhuyin.htm))

**Chinese Unicode Wordlist**

- [**Chinese to Unicode**](https://www.chinese-tools.com/tools/converter-unicode.html) ([chinese-tools.com](https://www.chinese-tools.com/))

---

I input all of the wordlist in a Excel File, but as I needed to transform it from Excel File to a Dictionary in Python, I used the [PANDAS](https://pandas.pydata.org/) library in order to do it

## 🆙 Version history

### 0.2.0

> Published on October 31. 2022
> 

**Main improvements**

- **Python GUI/Tkinter library**

(plus 0.1.3 version features)

### 0.1.3

> Published on October 31. 2022
> 

**Main improvements**
- Able to translate 20000 of the most common Chinese Characters
- Addition of new languages:
    - Chinese Zhuyin
    - Chinese Unicode
  
**Other improvements**
    - Better checker of the inputted text (Chinese Character, Latin letters or Zhuyin)
    - Creation of system for traslations using less space
    - Cleaner functions for translation
    - Better system for translation
    - Cleaner and lighter code

(plus 0.1.2 version features)

### 0.1.2

> Published on October 12. 2022
> 

**Main improvements**
- Able to translate 12000 of the most common Chinese Characters

**Other improvements**
    - Checker of the inputted text (Chinese Character or not)
    - Better functions fo translation
    - Cleaner and lighter code
    - Addition of OOP concepts

(plus 0.1.1 version features)

### 0.1.1

> Published on October 4. 2022
> 
- First initial version
- **Python Module Software**
- Able to translate 8000 most common Chinese Characters
- Able to translate in:
    - Mandarin Chinese Simplified
    - Mandarin Chinese Traditional
    - Mandarin Chinese Pinyin
    - Cantonese
    - Cantonese Pinyin

## 🌱 Plan for the future

I plan to focus on other projects but I still have some ideas for this one, like:

- More accurate translation
- Text-to-Speech
- More Chinese Dialects
- Voice recognition and input

and others!

### Contribution

If you want to contribute something, report problems or add features, you are totally welcome!

### Support

Star ⭐ this repository if my project helped you!

## ©️ License

**MIT License** - Simtracan Translator - Daniela Bai - Year 2022

## 👩🏼‍💻 Author

Daniela Bai (Daniela Barazarte)

- Twitter [@danielabai8](https://twitter.com/@danielabai8)
- Github [@danielabai](https://github.com/danielabai/)

### Special thanks

Thanks to my friend **Marco Aurelio L**. for giving me active feedback on my code, as giving me recommendations and new ideas for the project. Thanks to my Chinese partner from Guangdong **Avery** for (unconsciously) giving me this idea. Thanks to my **mom** and anyone else who has always support me during this project. Also thanks to the tutorials I followed in order to complete this project!

Thanks to **FreeCodeCamp** and their tutorials of:

- [Python Beginner Course](https://www.youtube.com/watch?v=rfscVS0vtbw)
- [Tkinter GUI Beginner Course](https://www.youtube.com/watch?v=YXPyB4XeYLA)

Thanks to **[Bro Code](https://www.youtube.com/c/BroCodez)** and his tutorials of:

- [Python Beginner Course](https://www.youtube.com/watch?v=XKHEtdqhLK8)
- [Tkinter GUI Beginner Course](https://www.youtube.com/watch?v=TuLxsvK4svQ)


<p align="center">
<img height="auto" width="5%" alt="Daniela Bai Logo (in GIF)" src="https://github.com/danielabai/danielabai/blob/main/logo/gif/Black2White.gif?raw=true"/>
</p>
