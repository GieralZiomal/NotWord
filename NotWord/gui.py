from cgitb import text
from email.policy import default
from fileinput import filename
from tkinter import *
from tkinter import filedialog
import ctypes
from tkinter.messagebox import RETRY
import pyperclip as pc
from tkinter import font

root = Tk()
root.title("NotWord")
root.geometry("1920x1080")
#root.iconbitmap("NotWord\justicon.ico")

textediting_frame = Frame(root, bg="white", width=1920, height=200, pady=3).grid(column=0, row=0, columnspan=3)
textwrite_frame = Frame(root, bg="#bdd4ff", width=1920, height=1080, pady=3).grid(column=0, row=1, columnspan=3)


def newfile():
    inputtxt.delete("1.0", END)

def openfile():
    #inputtxt.delete("1.0", END)
	text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
	text_file = open(text_file, 'r')
	stuff = text_file.read()
	inputtxt.insert(END, stuff)
	text_file.close()

def saveasfile():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    text_file = open(text_file, 'w')
    text_file.write(inputtxt.get(1.0, END))
    text_file.close()

def savefile():
	global open_status_name
	if open_status_name:
		text_file = open(open_status_name, 'w')
		text_file.write(inputtxt.get(1.0, END))
		text_file.close()
	else:
		saveasfile()

  
def textformatu():
    inp = str(inputtxt.get(1.0, "end-1c"))
    inputtxt.delete('1.0', END)
    inputtxt.insert(END, inp.upper())

def textformatl():
    inp = str(inputtxt.get(1.0, "end-1c"))
    inputtxt.delete('1.0', END)
    inputtxt.insert(END, inp.lower())

def textformatt():
    inp = str(inputtxt.get(1.0, "end-1c"))
    inputtxt.delete('1.0', END)
    inputtxt.insert(END, inp.title())

def textformatc():
    inp = str(inputtxt.get(1.0, "end-1c"))
    inputtxt.delete('1.0', END)
    inputtxt.insert(END, inp.capitalize())

def textformats():
    inp = str(inputtxt.get(1.0, "end-1c"))
    inputtxt.delete('1.0', END)
    inputtxt.insert(END, inp.swapcase())

def cuttext():
    inp = str(inputtxt.get(1.0, "end-1c"))
    inputtxt.delete('1.0', END)
    pc.copy(inp)

def copytext():
    inp = str(inputtxt.get(1.0, "end-1c"))
    pc.copy(inp)

def pastetext():
    inp = str(inputtxt.get(1.0, "end-1c"))
    inputtxt.delete('1.0', END)
    inputtxt.insert(END, pc.paste())

def deletetext():
    inputtxt.delete('1.0', END)

def selectatext():
    inputtxt.tag_add('sel', '1.0', 'end')

def reversetext():
    inp = str(inputtxt.get(1.0, "end-1c"))
    inputtxt.delete('1.0', END)
    inputtxt.insert(END, inp[::-1])

our_font = font.Font(family="Helvetica", size="10")

def font_size_chooser(e):
    our_font.config(
		size = font_size_listbox.get(font_size_listbox.curselection()))

def font_family_chooser(e):
    our_font.config(
		family = font_family_listbox.get(font_family_listbox.curselection()))

inputtxt = Text(textediting_frame, width=150, height=67, font=our_font)
inputtxt.grid(column=1, row=1)

font_size_listbox = Listbox(textediting_frame, selectmode=SINGLE, width=20 )
font_size_listbox.grid(row=0, column=0)

font_family_listbox = Listbox(textediting_frame, selectmode=SINGLE, width=20 )
font_family_listbox.grid(row=0, column=1)

font_label = Label(textediting_frame, text="Choose Font Size", font=("Helvetica", 10))
font_label.grid(row=0, column=0, padx=10, sticky=W)
font_label = Label(textediting_frame, text="Choose Font", font=("Helvetica", 10))
font_label.grid(row=0, column=1, padx=10, sticky=W)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_command(label="Save as...", command=saveasfile)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=inputtxt.edit_undo, accelerator="(Ctrl+z)")
editmenu.add_command(label="Redo", command=inputtxt.edit_redo, accelerator="(Ctrl+y)")

editmenu.add_separator()

editmenu.add_command(label="Cut", command=cuttext, accelerator="(Ctrl+x)")
editmenu.add_command(label="Copy", command=copytext, accelerator="(Ctrl+c)")
editmenu.add_command(label="Paste", command=pastetext, accelerator="(Ctrl+v)")
editmenu.add_command(label="Delete", command=deletetext)
editmenu.add_command(label="Select All", command=selectatext, accelerator="(Ctrl+a)")

menubar.add_cascade(label="Edit", menu=editmenu)
formatmenu = Menu(menubar, tearoff=0)
formatmenu.add_command(label="Uppercase", command=textformatu)
formatmenu.add_command(label="Lowercase", command=textformatl)
formatmenu.add_command(label="Title", command=textformatt)
formatmenu.add_command(label="Capitalize", command=textformatc)
formatmenu.add_command(label="Swapcase", command=textformats)
formatmenu.add_command(label="Reverse", command=reversetext)
menubar.add_cascade(label="Formating", menu=formatmenu)


root.config(menu=menubar)

font_sizes = [8, 10, 12, 14, 16, 18, 20, 36, 48]
for size in font_sizes:
	font_size_listbox.insert('end', size)

font_families = ["Arial", "Comic Sans MS"]
for family in font_families:
	font_family_listbox.insert('end', family)

font_family_listbox.bind('<ButtonRelease-1>', font_family_chooser)

font_size_listbox.bind('<ButtonRelease-1>', font_size_chooser)

root.mainloop()