#Импорт нужных модулей для GUI
from tkinter import *
from tkinter import ttk

#Создание GUI 
root = Tk()
root.title('l33t tr4nsl4t0r')
root.geometry('250x250')

#Добавление названия
label_of_entry = ttk.Label()
label_of_entry['text'] = 'Enter text that you need to translate to l33t'
label_of_entry.pack(anchor=CENTER, padx = 10, pady = 20)


#Добавление поля ввода
entry = ttk.Entry()
entry.pack(anchor=CENTER, padx = 10, pady = 10)

#функция для перевода
def to_leet_speak(str):
    leet = {
  'A' : '@',
  'B' : '8',
  'C' : '(',
  'D' : 'D',
  'E' : '3',
  'F' : 'F',
  'G' : '6',
  'H': '#',
  'I' : '!',
  'J' : 'J',
  'K' : 'K',
  'L' : '1',
  'M' : 'M',
  'N' : 'N',
  'O' : '0',
  'P' : 'P',
  'Q' : 'Q',
  'R' : 'R',
  'S' : '$',
  'T' : '7',
  'U' : 'U',
  'V' : 'V',
  'W' : 'W',
  'X' : 'X',
  'Y' : 'Y',
  'Z' : '2'
}
    for key in leet:
        str = str.replace(key, leet[key])
    return str

#функция для получения текта
def get_translation_of_text():
    global entered_text
    entered_text = entry.get().upper()
    label['text'] = to_leet_speak(entered_text)
    

#создание поля с переводом
label = ttk.Label()
label.pack(anchor=CENTER, padx=10, pady=30)


#кнопка для перевода 
btn = ttk.Button(text='translate', command=get_translation_of_text)
btn.pack(anchor=E, padx=5, pady=10)

#Добавление альтернативного перевода
label_of_alt_translate = Label()
label_of_alt_translate['text'] = 'Enter text you need to translate from l33t'
label_of_alt_translate.pack(anchor=S, pady = 40)

alt_entry = ttk.Entry()
alt_entry.pack(anchor=S, pady = 60)

#Функция для альт перевода

def from_leet_speak(alt_str):
    alt_leet = {
  '@' : 'A',
  '8' : 'B',
  '(' : 'C',
  'D' : 'D',
  '3' : 'E',
  'F' : 'F',
  '6' : 'G',
  '#': 'H',
  '!' : 'I',
  'J' : 'J',
  'K' : 'K',
  '1' : 'L',
  'M' : 'M',
  'N' : 'N',
  '0' : 'O',
  'P' : 'P',
  'Q' : 'Q',
  'R' : 'R',
  '$' : 'S',
  '7' : 'T',
  'U' : 'U',
  'V' : 'V',
  'W' : 'W',
  'X' : 'X',
  'Y' : 'Y',
  '2' : 'Z'
}
    for key in alt_leet:
        alt_str = alt_str.replace(key, alt_leet[key])
    return alt_str

#Функция для отображения альт перевода
def get_alt_translation_of_text():
    global entered_alt_text
    entered_alt_text = alt_entry.get()
    alt_trans_lbl['text'] = from_leet_speak(entered_alt_text)


#Кнопка для альт перевода
alt_btn = ttk.Button(text='translate', command=get_alt_translation_of_text)
alt_btn.pack(anchor=E, pady=70)

#Вывод альтернативного перевода

alt_trans_lbl = Label()
alt_trans_lbl.pack(anchor=CENTER, pady=80)

#Отображение окна
root.mainloop()