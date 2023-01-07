![Logotipo y pancarta de Simtracan](README_SimtracanBanner.jpg)
---
Leer en otros idiomas: [English](README.md) · [Español](README.sp.md) · [简体中文](README.zh-s.md) · [繁體中文](README.zh-t. Maryland).
---
## 🀄 Traductor Simtracán

**Simtracan Traductor** es un software de traducción que (en su versión 0.1.3) puede traducir entre chino mandarín simplificado, chino mandarín tradicional, chino mandarín pinyin, cantonés, cantonés pinyin, chino zhuyin y caracteres chinos Unicode.

Este software fue desarrollado en Python por Daniela Bai (Daniela Barazarte) y su objetivo principal es traducir texto en múltiples derivaciones del idioma chino sin límite de caracteres, sin anuncios, con gran traducción y teniendo múltiples opciones en el mismo traductor.

En este momento, puede traducir la mayoría de los caracteres chinos, ya que contiene una biblioteca de más de 18,000 汉字.

### Motivación

Hace casi dos años comencé a aprender chino mandarín y como estoy tan interesado en el idioma encontré algunos compañeros para practicar, uno de ellos era una chica de Guangdong que, para jugarme una broma, me envía mensajes de texto en cantonés.

Mientras mejoraba mi chino, también estaba aprendiendo Python a través de un tutorial de Youtube y estaba dispuesto a poner en práctica el conocimiento, así que… como antes, no podía encontrar buenos traductores que pudieran dar la traducción del cantonés al mandarín simplificado para entender los mensajes de mi pareja. , ¿por qué no construirlo yo mismo? y así es como me vino a la mente Simtracan Traductor.

Fue difícil al principio, considerando que soy muy nuevo en el aspecto de la programación y no soy bueno en cantonés en absoluto, pero incluso con eso decidí construirlo.

Empecé el proyecto y tomé la decisión de llamarlo “Traductor de Simtracan”, ya que incluye chino simplificado, tradicional y cantonés. Ahora estoy muy emocionada de mostrar este proyecto.

## 🚀 Instalación

### Requisitos previos

Python 3.x.x

La única biblioteca adicional que usa su software es Regex que viene por defecto en la mayoría de las versiones de Python.

> Después de la versión 1.2.0 usa Tkinter
>

### Instalación

1. Descarga el ZIP de este repositorio

![Cómo descargar GITHUB ZIP](README_DownloadZip.png)

1. Extraiga el ZIP que descargó
2. Utilice Simtracan Traductor libremente
     - Puedes usar el modo Python Module en la versión 0.1.3
     - Puede usar el modo .exe (Python GUI) en la versión 0.2.0

## 💻 Uso

### ❗ Tenga en cuenta que

Tenga en cuenta que el software de Simtracan Traductor podría incluir errores técnicos o tipográficos. Además, Simtracan Traductor no garantiza que las traducciones que se realizan en el software sean precisas y/o completas.

---

### Modo Módulo de Python

- Abra su Terminal/Consola de Python
- Agrega la carpeta de la versión que necesitas
- Ejecutar el código
     - Si tiene problemas o errores en este paso, [póngase en contacto conmigo] (simtracan-translator%20819d2e8f30024ea3833e508558ff7bee.md)
- Empezar a seguir las instrucciones.

**Explicación**

*(Esta es la explicación de la versión 0.1.3, las diferentes versiones funcionan de manera similar)*

Deberá ingresar el texto que desea traducir

> El software verificará automáticamente el texto que ingresa con una función Regex
>

Seleccione un número que indique en qué idioma está el texto que ingresa

Seleccione otro número y seleccione el idioma en el que desea recibir la traducción.

> Si seleccionó una opción incorrectamente, o si seleccionó el mismo idioma dos veces, el software mostrará un mensaje de error y le permitirá seleccionar una opción (tiene tres intentos para seleccionar la opción correctamente)
>

Recibe tu traducción

### Modo de GUI de Python

- Abre el .exe
     - Si tiene problemas o errores en este paso, [póngase en contacto conmigo] (simtracan-translator%20819d2e8f30024ea3833e508558ff7bee.md)
- Usa el traductor

**Explicación**

Con una interfaz interactiva, necesitará el texto que desea traducir. Puede pegar el texto en el Área de texto u obtenerlo de un archivo en su computadora.

También puede verificar el texto que ingresa.

> Contará cuántos caracteres tiene tu texto y también te dirá si está en Pinyin o en caracteres chinos
>

Luego debes seleccionar en el menú de opciones en qué idioma está ese texto que ingresas.

Seleccione en otro menú de opciones el idioma en el que desea recibir la traducción

Haga clic en "Traducir" y reciba su traducción

> Si seleccionó una opción incorrectamente, o si seleccionó el mismo idioma dos veces, el software mostrará un mensaje de error y le permitirá seleccionar una opción nuevamente
>

Guarde su traducción guardándola en un archivo que puede ser .txt o .html

## 📄 Código

### Glosario

| Abreviatura | Palabra completa | Significado |
| --- | --- | --- |
| FL o lang_A | Primer Idioma o Idioma A | es el idioma que usará para ingresar el texto que desea traducir |
| SL o lang_B | Segundo Idioma o Idioma B | es el idioma que el software elegirá para generar la traducción |
| 1 o SM | mandarín simplificado | 普通话简体字 - Caracteres simplificados del chino mandarín |
| 2 o TM | mandarín tradicional | 普通话繁體字 - Tradición del chino mandarín

l personajes |
| 3 o PM | mandarín pinyin | 普通话拼音 - letras mandarín pinyin |
| 4 o C | cantonés | 广东话/粵語 - Caracteres del chino cantonés (dialecto de Guangdong) |
| 5 o PC | pinyin cantonés | 粵拼 - letras cantonesas pinyin (jyutping) |
| 6 o CZ | Zhuyin chino | ㄅㄆㄇㄈ - Chino mandarín Zhuyin (Bopomofo) |
| 7 o CU | Unicode chino | 中文统一码 - Codificación de caracteres chinos |

### Explicación detallada

Incluso si las diferentes versiones funcionan ligeramente diferentes, la forma en que este software funciona en general es que ingresará el texto que desea traducir, luego seleccionará en qué idioma está ese texto (lang_A) y luego, seleccionará en qué idioma desea ese texto. para ser traducido (lang_B), luego mostrará la traducción para usted.

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
        
    
     El resultado de .replace() se generará/se mostrará para usted
   
## 💯 Fuentes utilizadas

Utilicé múltiples recursos para hacer que este software funcionara, especialmente en el momento de crear la lista de palabras de caracteres utilizada para la traducción. Necesitaba múltiples recursos, así que los etiquetaré aquí.

**Lista de palabras en chino simplificado**

- [**Lista de palabras de 10 000 caracteres**](https://www.chinese-forums.com/forums/topic/42692-spreadsheet-of-10000-most-frequent-chinese-words-2397-characters/#replyForm) ([Foros chinos](https://www.chinese-forums.com/), [usuario Sparrow](https://www.chinese-forums.com/profile/53860-sparrow/))
- **[中文汉字大全](http://www.ku51.net/hanzi/hanzi1.html)** ([KU51.net](http://www.ku51.net/))

**Lista de palabras en chino tradicional**

- [**Conversión de chino simplificado <> Caracteres tradicionales**](https://www.lexilogos.com/keyboard/chinese_conversion.htm) ([lexilogos.com](https://www.lexilogos.com/))
- **[简体繁体字转换器](http://www.ku51.net/)** ([KU51.net](http://www.ku51.net/))

**Lista de palabras en chino mandarín pinyin**

- [**Pinyin Conversion Tone Marks <> Números](https://www.lexilogos.com/keyboard/pinyin_conversion.htm)** ([lexilogos.com](https://www.lexilogos.com/))
- **[Convertidor chino a pinyin](http://www.meetmandarin.com/resources/pinyin-converter.html)** ([meetmandarin.com](http://www.meetmandarin.com/))

**Lista de palabras en chino cantonés y pinyin cantonés**

- [**Convertidor de cantonés a jyutping**](https://www.branah.com/cantonese-to-jyutping) ([branah.com](https://www.branah.com/))
- **[漢字→廣東話/粵語拼音轉換工具](https://hongkongvision.com/tool/cc_py_conv_zh)** ([hongkongvision.com](https://hongkongvision.com/tool/cc_py_conv_zh))

**Lista de palabras en chino Zhuyin**

- [Zhuyin fuhao / Bopomofo](https://omniglot.com/chinese/zhuyin.htm) ([omniglot.com](https://omniglot.com/chinese/zhuyin.htm))

**Lista de palabras Unicode en chino**

- [**Chino a Unicode**](https://www.chinese-tools.com/tools/converter-unicode.html) ([chinese-tools.com](https://www.chinese-tools. com/))

---

Ingresé toda la lista de palabras en un archivo de Excel, pero como necesitaba transformarlo de un archivo de Excel a un diccionario en Python, usé la biblioteca [PANDAS](https://pandas.pydata.org/) para hacer eso

## 🆙 Historial de versiones

### 0.2.0

> Publicado el 31 de octubre de 2022
>

**Principales mejoras**

- **Biblioteca Python GUI/Tkinter**

(más características de la versión 0.1.3)

### 0.1.3

> Publicado el 31 de octubre de 2022
>

**Principales mejoras**
- Capaz de traducir 20000 de los caracteres chinos más comunes
- Adición de nuevos idiomas:
     - Zhuyin chino
     -Unicode chino
  
**Otras mejoras**
     - Mejor verificador del texto ingresado (caracteres chinos, letras latinas o Zhuyin)
     - Creación de sistema para traducciones utilizando menos espacio
     - Funciones más limpias para la traducción.
     - Mejor sistema de traducción.
     - Código más limpio y ligero.

(más características de la versión 0.1.2)

### 0.1.2

> Publicado el 12 de octubre de 2022
>

**Principales mejoras**
- Capaz de traducir 12000 de los caracteres chinos más comunes

**Otras mejoras**
     - Verificador del texto ingresado (Carácter chino o no)
     - Mejores funciones de traducción.
     - Código más limpio y ligero.
     - Adición de conceptos OOP

(más características de la versión 0.1.1)

### 0.1.1

> Publicado el 4 de octubre de 2022
>
- Primera versión inicial
- **Software del módulo Python**
- Capaz de traducir 8000 caracteres chinos más comunes
- Capaz de traducir en:
     - Chino mandarín simplificado
     - Chino mandarín tradicional
     - Pinyin chino mandarín
     - Cantonés
     - pinyin cantonés

## 🌱 Plan para el futuro

Planeo enfocarme en otros proyectos, pero todavía tengo algunas ideas para este, como:

- Traducción más precisa
- Texto a voz
- Más dialectos chinos
- Reconocimiento y entrada de voz

¡y otros!

### Contribución

Si quieres contribuir con algo, reportar problemas o agregar funciones, ¡eres totalmente bienvenido!

### Apoyo

¡Estrella ⭐ este repositorio si mi proyecto te ayudó!

## ©️ Licencia

**Licencia MIT** - Simtracan Translator - Daniela Bai - Año 2022

## 👩🏼‍💻 Autor

Daniela Bai (Daniela Barazarte)

- Twitter [@danielabai8](https://twitter.com/@danielabai8)
- Github [@danielabai](https://github.com/danielabai/)

### Gracias especiales

Gracias a mi amigo **Marco Aurelio L**. por darme retroalimentación activa sobre mi código, así como por darme recomendaciones y nuevas ideas para el proyecto. Gracias a mi socio chino de Guangdong **Avery** por (inconscientemente) darme esta idea. Gracias a mi **mamá** y a todos los que siempre me han apoyado durante este proyecto. ¡También gracias a los tutoriales que seguí para completar este proyecto!

Gracias a **FreeCodeCamp** y sus tutoriales de:

- [Curso para principiantes de Python](https://www.youtube.com/watch?v=rfscVS0vtbw)
- [Curso para principiantes de GUI de Tkinter](https://www.youtube.com/watch?v=YXPyB4XeYLA)

Gracias a **[Bro Code](https://www.youtube.com/c/BroCodez)** y sus tutoriales de:

- [Curso para principiantes de Python](https://www.youtube.com/watch?v=XKHEtdqhLK8)
- [Curso para principiantes de GUI de Tkinter](https://www.youtube.com/watch?v=TuLxsvK4svQ)


<p align="center">
<img height="auto" width="5%" alt="Daniela Bai Logo (in GIF)" src="https://github.com/danielabai/danielabai/blob/main/logo/gif/Black2White.gif?raw=true"/>
</p>
