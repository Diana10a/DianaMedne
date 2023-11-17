#mērķis ir uzstaisīt programmu, kurā zemūdene spridzina burbuļus
#tiek skaitīti punkti
from tkinter import *
from random import *
from math import *
logs = Tk()
garums = 700
platums = 700
logs.title("Burbuļu spridzinātājs")
a = Canvas(logs, width=platums, height=garums, bg='lightblue')
a.pack()
kuga_id2 = a.create_oval(5,5,80,80,outline='black', width=4)









mainloop()
