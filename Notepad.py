from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
file = None


# main window
root = Tk()
root.title("Untitled - Notepad")
root.geometry("1010x465")


def clear():
    text.delete(1.0, END)


def new():
    global file
    file = None
    root.title("Untitled - Notepad")
    text.delete(1.0, END)


def exitt():
    root.destroy()


def save_file():
    global file
    if file is None:
        file = filedialog.asksaveasfilename(title="Save As", initialfile="Untitled", defaultextension="*.txt", filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py")])
        if file == "":
            file = None
        else:
            contents = open(file, "w")
            contents.write(text.get(1.0, END))
            contents.close()
            root.title(file + " - Notepad")
    else:
        contents = open(file, "w")
        contents.write(text.get(1.0, END))
        contents.close()


def open_file():
    global file
    file = filedialog.askopenfilename(title="Open a File", filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py")])
    if file is None or file == "":
        root.title("Untitled - Notepad")
    else:
        root.title(file + " - Notepad")
        contents = open(file, "r+a")
        text.delete(1.0, END)
        text.insert(1.0, contents.read())
        contents.close()


def helpp():
    messagebox.showinfo("Notepad", "This Notepad is created by Paras")


# text area

text = Text(font="cambria 12")
text.pack(expand=1, fill=BOTH)
text.focus()

# Scrollbar Y

scrolly = Scrollbar(text)
scrolly.pack(side=RIGHT, fill=Y)
scrolly.config(command=text.yview)
text.config(yscrollcommand=scrolly.set)

# Scrollbar X

scrollx = Scrollbar(text, orient=HORIZONTAL)
scrollx.pack(side=BOTTOM, fill=X, anchor="w")
scrollx.config(command=text.xview)
text.config(xscrollcommand=scrollx.set)

# THIS IS THE AREA OF MENUS

# File Menu
file_menu = Menu(tearoff=0)
file_menu.add_command(label="New", command=new)
file_menu.add_separator()
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Clear", command=clear)
file_menu.add_command(label="Exit", command=exitt)

# Help Menu
help_menu = Menu(tearoff=0)
help_menu.add_command(label="About", command=helpp)

# Main Menu
main_menu = Menu(root)
root.configure(menu=main_menu)
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Help", menu=help_menu)

# Shortcut Keys

root.bind("<Control-s>", lambda pressed_key: save_file())
root.bind("<Control-o>", lambda pressed_key: open_file())


root.mainloop()

