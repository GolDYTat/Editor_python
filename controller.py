from tkinter import *
from tkinter import filedialog
import view
import os

def fileMenu(action):
    global currentFilePath
    if action == "open":
        file = filedialog.askopenfilename(filetypes = view.fileTypes)
        view.window.title(file + " - " + view.appName)
        currentFilePath = file
        with open(file, 'r') as f:
            view.txt.delete(1.0,END)
            view.txt.insert(INSERT,f.read())
    elif action == "new":
        currentFilePath = view.nofileOpenedString
        view.txt.delete(1.0,END)
        view.window.title(view.appName + " - " + currentFilePath)
    elif action == "delete":
        os.remove(currentFilePath)
    elif action == "save" or action == "saveAs":
        if currentFilePath == view.nofileOpenedString or action== 'saveAs':
            currentFilePath = filedialog.asksaveasfilename(filetypes = view.fileTypes)
        with open(currentFilePath, 'w') as f:
            f.write(view.txt.get('1.0','end'))
        view.window.title(currentFilePath + " - " + view.appName)

def textchange(event):
    view.window.title(currentFilePath + " - *" + view.appName)