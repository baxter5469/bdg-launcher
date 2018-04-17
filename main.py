'''BDG Launcher v1.0 By Andrew Ault
4/16/18
'''
import tkinter as tk
from tkinter import filedialog
import os
self = ""
top = tk.Tk()
def runFormat(self):
    file = filedialog.askopenfile(initialfile = "bdgformat.exe", title = "Select File", filetypes = (("exe files","format*.exe"),)) #Opens File Explorer and allows user to select file.
    os.startfile(file.name) 
def runDiscord(self):
    file = filedialog.askopenfile(initialfile = "bdgdiscord.exe", title = "Select File", filetypes = (("exe files","bdgdiscord*.exe"),)) #Opens File Explorer and allows user to select file.
    os.startfile(file.name) 
def runFriend(self):
    file = filedialog.askopenfile(initialfile = "bdgfriend.exe", title = "Select File", filetypes = (("exe files","bdgfriend*.exe"),)) #Opens File Explorer and allows user to select file.
    os.startfile(file.name) 
def runKey(self):
    file = filedialog.askopenfile(initialfile = "bdgkey.exe", title = "Select File", filetypes = (("exe files","bdgkey*.exe"),)) #Opens File Explorer and allows user to select file.
    os.startfile(file.name)     
b = tk.Button(top, text = "BDG Format Tool", command=lambda: runFormat(self))
b.grid(row=0, column=0)
b2 = tk.Button(top,text = "BDG Friend Manager", command=lambda: runDiscord(self) )
b2.grid(row=0, column=1)
b3 = tk.Button(top, text = "BDG Key Safe", command=lambda: runFriend(self))
b3.grid(row=1, column=0)
b4 = tk.Button(top,text = "BDG Discord Manager", command=lambda: runKey(self) )
b4.grid(row=1, column=1)
top.title("BDG Launcher")
top.mainloop()