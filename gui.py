from tkinter import *
from tts import speak
from tkinter import filedialog

def convertFile():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text Files","*.txt"),("all files","*.*")))
    with open(filename, 'rt') as f:
        text = f.read()
        speak(text,"en")
    status_label.configure(text ="successfully completed")

def addF():
    if (txtbx.get() != ""):
        try:
            txt = txtbx.get()
            speak(txt,"en")
            status_label.configure(text ="successfully completed")
        except:
            status_label.configure(text ="The text is not in proper format.")
    else:
        status_label.configure(text ="fill in the text, please.")

root = Tk()
root.geometry("410x350")
root.title("Text To Speech")

title = Label(root, text="Text-To-Speech\nConvertor", height =2, width =15, bg ="blue", fg="white")
title.grid(row=0,column=1)

blank_label = Label(root, text="")
blank_label.grid(row =1, column=0)

label1 =Label(root, text ="Text")
label1.grid(row =2, column =0,)

txtbx =Entry(root)
txtbx.grid(row =2, column =1, )
txtbx.focus_set()

btn = Button(root, text="speak", command = addF)
btn.grid(row=2,column=2)

blank_label = Label(root, text="")
blank_label.grid(row =3, column=0)

label1 =Label(root, text ="OR")
label1.grid(row =4, column =1)

blank_label = Label(root, text="")
blank_label.grid(row =5, column=0)

btn = Button(root, text="Convert Text File", command = convertFile)
btn.grid(row=6,column=1)

blank_label = Label(root, text="")
blank_label.grid(row =7, column=0)



status_label =Label(root, height =5, width =25, bg ="black", fg ="#00FF00", text ="---", wraplength =150)
status_label.grid(row =9, column =1)

root.mainloop()