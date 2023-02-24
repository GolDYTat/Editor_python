from tkinter import *
from tkinter import scrolledtext
import sys
import controller

appName = 'Редактор'
nofileOpenedString = 'Новый файл'
currentFilePath = nofileOpenedString
fileTypes = [("Текстовый файл(*.txt)","*.txt")]

window = Tk()
txt = scrolledtext.ScrolledText(window, height=999)

window.grid_columnconfigure(0, weight=1)
window.title(currentFilePath + " - " + appName)
window.geometry('500x400')

txt = scrolledtext.ScrolledText(window, height=999)
txt.grid(row=1,sticky=N+S+E+W)
txt.bind('<KeyPress>', controller.textchange)
menu = Menu(window)
fileDropdown = Menu(menu, tearoff=False)
fileDropdown.add_command(label='Создать', command=lambda: controller.fileMenu("new"))
fileDropdown.add_command(label='Открыть...', command=lambda: controller.fileMenu("open"))
fileDropdown.add_separator()
fileDropdown.add_command(label='Сохранить', command=lambda: controller.fileMenu("save"))
fileDropdown.add_command(label='Сохранить как...', command=lambda: controller.fileMenu("saveAs"))
fileDropdown.add_separator()
fileDropdown.add_command(label='Удалить файл', command=lambda: controller.fileMenu("delete"))
menu.add_cascade(label='Файл', menu=fileDropdown)
window.config(menu=menu)

if len(sys.argv) == 2:
    currentFilePath = sys.argv[1]
    window.title(currentFilePath + " - " + appName)
    with open(currentFilePath, 'r') as f:
        txt.delete(1.0,END)
        txt.insert(INSERT,f.read())

window.mainloop()