![Simtracan 标志和横幅](README_SimtracanBanner.jpg)
---
其他语言阅读：[English](README.md) · [Español](README.sp.md) · [简体中文](README.zh-s.md) · [繁体中文](README.zh-t.md)
---
## 🀄 Simtracan 翻译

**Simtracan Translator** (Simtracan 翻译) 是一款翻译软件（在其 0.1.3 版本中）可以在简体中文、繁体中文、普通话拼音、粤语、粤语拼音、中文注音和中文 Unicode 字符之间进行翻译。

该软件由 Daniela Bai (Daniela Barazarte) 用 Python 开发，其主要目标是翻译中文的多种派生文本，不受字符限制，无广告，翻译效果好，同一翻译器有多种选择。

现在它能够翻译大部分汉字，因为它包含一个超过 18.000 汉字的图书馆。

### 动机

大约两年前，我开始学习普通话，因为我对这门语言很感兴趣，所以我找了一些伙伴一起练习，其中一位是广东女孩，开玩笑说她用粤语发给我短信。

在提高我的中文水平的同时，我还通过一些 Youtube 教程学习了 Python，并愿意将所学知识付诸实践，所以……以前我找不到好的翻译人员可以将粤语翻译成简体中文来理解我伙伴的信息 ，为什么不自己建呢？ 于是想到了 Simtracan Translator。

一开始很难，考虑到我对编程方面很陌生，而且根本不擅长粤语，但即便如此我还是决定构建它。

我启动了这个项目，并决定将其称为“Simtracan Translator”，因为它包括简体中文、繁体中文和粤语。 现在我很高兴展示这个项目。

## 🚀 安装

###先决条件

Python 3.x.x

他的软件使用的唯一附加库是 Regex，它在大多数 Python 版本中都是默认的。

> 版本 1.2.0 之后使用 Tkinter
>

### 安装

1. 下载这个存储库的 ZIP

![如何下载 GITHUB ZIP](README_DownloadZip.png)

1.解压你下载的ZIP
2.自由使用Simtracan Translator
     - 您可以在 0.1.3 版本上使用 Python 模块模式
     - 您可以在 0.2.0 版本上使用 .exe（Python GUI）模式

## 💻 用法

### ❗请注意

请注意，Simtracan Translator 的软件可能包含技术或印刷错误。 此外，Simtracan Translator 不保证软件中出现的翻译是准确和/或完整的。

---

### Python模块模式

- 打开你的 Python 终端/控制台
- 添加你需要的版本的文件夹
- 运行代码
     - 如果您在此步骤中遇到问题/错误，请[联系我](simtracan-translator%20819d2e8f30024ea3833e508558ff7bee.md)
- 开始按照说明进行操作

**解释**

*（这是0.1.3版本的解释，不同版本作用相似）*

您需要输入要翻译的文本

> 软件会自动检查您输入的正则表达式文本
>

选择一个数字，告诉您输入的文字是什么语言

选择其他号码并选择您希望接收翻译的语言。

> 如果你选错了一个选项，或者你选择了同一种语言两次，软件会显示一个错误信息并让你选择一个选项（你有3次尝试正确选择选项）
>

收到您的翻译

### Python GUI mode

- 打开 .exe
     - 如果您在此步骤中遇到问题/错误，请[联系我](simtracan-translator%20819d2e8f30024ea3833e508558ff7bee.md)
- 使用翻译器

**解释**

使用交互式界面，您将需要要翻译的文本。 您可以将文本粘贴到文本区域，或从计算机上的文件中获取。

您还可以检查您输入的文本。

> 它会统计你的文字有多少个字，还会告诉你是拼音还是汉字
>

然后您必须在选项菜单中选择您输入的文本是什么语言。

在其他选项菜单中选择您想要接收翻译的语言

单击“翻译”并接收您的翻译

> 如果您选择了错误的选项，或者您选择了两次相同的语言，软件将显示错误消息并让您重新选择一个选项
>

通过将翻译保存到可以是 .txt 或 .html 的文件来保存您的翻译

## 📄 代码

### 词汇表

| 缩写 | 全词 | 含义 |
| --- | --- | --- |
| FL 或 lang_A | 第一语言或语言A | 是您将用来输入要翻译的文本的语言 |
| SL 或 lang_B | 第二语言或语言 B | 是软件将选择生成翻译的语言 |
| 1 或 SM | 简体中文 | 普通话简体字- 普通话简体字|
| 2 或以旧换新 | 繁体中文 | 普通话繁体字- 中文繁体字| 简体中文
| 3 或 MP | 普通话拼音 | 普通话拼音- 普通话拼音字母|
| 4 或 C | 粤语 | 广东话/粤语- Cantonese Chinese (广东方言) characters |
| 5 或 CP | 粤语拼音 | 粤拼 - 粤语拼音 (Jyutping) 字母 |
| 6 或 CZ | 中国注音 | ㄅㄆㄇㄈ - 中文注音 (Bopomofo) |
| 7 或 CU | 中文统一码 | 中文统一码 - Chinese Chacter Encoding |

### 详细解释

即使不同版本的工作方式略有不同，该软件的一般工作方式是您输入要翻译的文本，然后选择该文本的语言 (lang_A)，然后选择您想要该文本的语言 待翻译（lang_B），然后它会为您显示翻译。

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
 
## 💯 使用的资源

我使用了多种资源来使这个软件工作，特别是在创建用于翻译的字符词表时我需要多种资源，所以我将它们标记在这里。

**简体中文词汇表**

- [**万字词表**](https://www.chinese-forums.com/forums/topic/42692-spreadsheet-of-10000-most-frequent-chinese-words-2397-characters/#replyForm) ([中文论坛](https://www.chinese-forums.com/), [Sparrow User](https://www.chinese-forums.com/profile/53860-sparrow/))
- **[中文汉字大全](http://www.ku51.net/hanzi/hanzi1.html)** ([KU51.net](http://www.ku51.net/))

**繁体字表**

- [**中文转换简体<>繁体字**](https://www.lexilogos.com/keyboard/chinese_conversion.htm) ([lexilogos.com](https://www.lexilogos.com/))
- **[简体繁体字转换器](http://www.ku51.net/)** ([KU51.net](http://www.ku51.net/))

**中文普通话拼音词表**

- [**拼音转换声调标记 <> 数字](https://www.lexilogos.com/keyboard/pinyin_conversion.htm)** ([lexilogos.com](https://www.lexilogos.com/))
- **[中文拼音转换器](http://www.meetmandarin.com/resources/pinyin-converter.html)** ([meetmandarin.com](http://www.meetmandarin.com/))

**中文粤语及粤语拼音词表**

- [**粤语转粤拼转换器**](https://www.branah.com/cantonese-to-jyutping) ([branah.com](https://www.branah.com/))
- **[汉字→广东话/粤语拼音转换工具](https://hongkongvision.com/tool/cc_py_conv_zh)** ([hongkongvision.com](https://hongkongvision.com/tool/cc_py_conv_zh))

**中国注音词表**

- [注音符豪/Bopomofo](https://omniglot.com/chinese/zhuyin.htm) ([omniglot.com](https://omniglot.com/chinese/zhuyin.htm))

**中文 Unicode 字表**

- [**中文转 Unicode**](https://www.chinese-tools.com/tools/converter-unicode.html) ([chinese-tools.com](https://www.chinese-tools. com/))

---

我在 Excel 文件中输入了所有单词列表，但由于我需要将其从 Excel 文件转换为 Python 中的字典，因此我使用了 [PANDAS](https://pandas.pydata.org/) 库来完成 它

## 🆙 版本历史

### 0.2.0

> 发表于 2022 年 10 月 31 日
>

**主要改进**

- **Python GUI/Tkinter 库**

（加上0.1.3版本特性）

### 0.1.3

> 发表于 2022 年 10 月 31 日
>

**主要改进**
- 能翻译20000个最常用的汉字
- 添加新语言：
     - 中国注音
     - 中国统一码
  
**其他改进**
     - 更好地检查输入文本（汉字、拉丁字母或注音）
     - 创建使用更少空间的翻译系统
     - 更清晰的翻译功能
     - 更好的翻译系统
     - 更干净、更轻便的代码

（加上0.1.2版本特性）

### 0.1.2

> 发表于 2022 年 10 月 12 日
>

**主要改进**
- 能翻译12000个最常用的汉字

**其他改进**
     - 输入文本的检查器（汉字或非汉字）
     - 更好的翻译功能
     - 更干净、更轻便的代码
     - 添加 OOP 概念

（加上0.1.1版本特性）

### 0.1.1

> 发表于 2022 年 10 月 4 日
>
- 第一个初始版本
- **Python 模块软件**
- 能翻译8000个最常用的汉字
- 能够翻译成：
     - 简体中文
     - 繁体中文
     - 普通话汉语拼音
     - 广东话
     - 粤语拼音

## 🌱 计划未来

我计划专注于其他项目，但我对这个项目仍有一些想法，例如：

- 更准确的翻译
- 文字转语音
- 更多中国方言
- 语音识别和输入

和别的！

### 贡献

如果您想贡献一些东西，报告问题或添加功能，我们完全欢迎您！

### 支持

如果我的项目对您有帮助，请星标 ⭐ 这个存储库！

## ©️ 许可证

**麻省理工学院许可证** - Simtracan Translator / Daniela Bai - 2022年

## 👩🏼‍💻 作者

Daniela Bai (Daniela Barazarte)

- Twitter [@danielabai8](https://twitter.com/@danielabai8)
- Github [@danielabai](https://github.com/danielabai/)

### 特别感谢

感谢我的朋友 **Marco Aurelio L**。 为我的代码提供积极的反馈，为我提供项目的建议和新想法。 感谢我来自广东的中国伙伴**Avery**（不知不觉中）给了我这个想法。 感谢我的**妈妈**以及在这个项目期间一直支持我的任何其他人。 还要感谢我为了完成这个项目而遵循的教程！

感谢 **FreeCodeCamp** 和他们的教程：

- [Python 入门教程](https://www.youtube.com/watch?v=rfscVS0vtbw)
- [Tkinter GUI 初学者课程](https://www.youtube.com/watch?v=YXPyB4XeYLA)

感谢 **[Bro Code](https://www.youtube.com/c/BroCodez)** 和他的教程：

- [Python 入门教程](https://www.youtube.com/watch?v=XKHEtdqhLK8)
- [Tkinter GUI 初学者课程](https://www.youtube.com/watch?v=TuLxsvK4svQ)


<p align="center">
<img height="auto" width="5%" alt="Daniela Bai Logo (in GIF)" src="https://github.com/danielabai/danielabai/blob/main/logo/gif/Black2White.gif?raw=true"/>
</p>
