#Импорт нужных модулей для GUI
from tkinter import *
from tkinter import ttk

#Создание GUI 
root = Tk()
root.title('l33t tr4nsl4t0r')
root.geometry('250x250')

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
    entered_text = entry.get()
    label['text'] = to_leet_speak(entered_text)
    

#создание поля с переводом
label = ttk.Label()
label.pack(anchor=CENTER, padx=10, pady=30)


#кнопка для перевода 
btn = ttk.Button(text='translate', command=get_translation_of_text)
btn.pack(anchor=E, padx=5, pady=10)

#Отображение окна
root.mainloop()