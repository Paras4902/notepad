from tkinter import Menu, END, Label, LabelFrame, Button, RIDGE
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import messagebox, font
from tkinter import ttk
from datetime import datetime
import webbrowser


def new():
    text.delete('1.0', 'end')


def new_window():
    root = tk.Tk()
    root.geometry('500x500')
    menu_bar = Menu(root)
    filed = Menu(menu_bar, tearoff=0)
    filed.add_command(label="New", command=new)
    filed.add_command(label="New window", command=new_window)
    filed.add_command(label="Open", command=openn)
    filed.add_command(label="Save as", command=save_as)
    filed.add_separator()
    filed.add_command(label="Exit", command=exitt)
    menu_bar.add_cascade(label="File", menu=file, font=('verdana', 10, 'bold'))
    editt = Menu(menu_bar, tearoff=0)
    editt.add_separator()
    editt.add_command(label="Cut", command=cut)
    editt.add_command(label="Copy", command=copy)
    editt.add_command(label="Paste", command=paste)
    editt.add_command(label="Delete", command=delete)
    editt.add_command(label="Select All", accelerator="Ctrl+A", command=select_all)
    editt.add_command(label="Time/Date", accelerator="F5", command=time)
    menu_bar.add_cascade(label="Edit", menu=edit)
    formatt = Menu(menu_bar, tearoff=0)
    formatt.add_command(label="Word Wrap")
    formatt.add_command(label="Font...", command=fonts)
    menu_bar.add_cascade(label="Format", menu=formatt)
    helpp = Menu(menu_bar, tearoff=0)
    helpp.add_command(label="View Help", command=view_help)
    helpp.add_command(label="Send FeedBack", command=send_feedback)
    helpp.add_command(label="About Notepad")
    menu_bar.add_cascade(label="Help", menu=helpp)
    root.config(menu=menu_bar)
    textt = ScrolledText(root, width=1000, height=1000)
    textt.place(x=0, y=0)
    root.mainloop()


def openn():
    window.filename = filedialog.askopenfilename(
        initialdir='/',
        title="Select file",
        filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    filee = open(window.filename)
    text.insert('end', filee.read())


def save_as():
    window.filename = filedialog.asksaveasfile(mode="w", defaultextension='.txt')
    if window.filename is None:
        return
    file_save = str(text.get(1.0, END))
    window.filename.write(file_save)
    window.filename.close()


def exitt():
    message = messagebox.askquestion('Notepad', "Do you want to save changes")
    if message == "yes":
        save_as()
    else:
        window.destroy()


def cut():
    text.event_generate("<<Cut>>")


def copy():
    text.event_generate("<<Copy>>")


def paste():
    text.event_generate("<<Paste>>")


def delete():
    message = messagebox.askquestion('Notepad', "Do you want to Delete all")
    if message == "yes":
        text.delete('1.0', 'end')
    else:
        return "break"


def select_all():
    text.tag_add('sel', '1.0', 'end')
    return 'break'


def time():
    d = datetime.now()
    text.insert('end', d)


def fonts():
    root = tk.Tk()
    root.geometry('400x400')
    root.title('Font')
    l1 = Label(root, text="Font:")
    l1.place(x=10, y=10)
    f = tk.StringVar()
    fontss = ttk.Combobox(root, width=15, textvariable=f, state='readonly', font=('verdana', 10, 'bold'), )
    fontss['values'] = font.families()
    fontss.place(x=10, y=30)
    fontss.current(0)
    l2 = Label(root, text="Font Style:")
    l2.place(x=180, y=10)
    st = tk.StringVar()
    style = ttk.Combobox(root, width=15, textvariable=st, state='readonly', font=('verdana', 10, 'bold'), )
    style['values'] = ('bold', 'bold italic', 'italic')
    style.place(x=180, y=30)
    style.current(0)
    l3 = Label(root, text="Size:")
    l3.place(x=350, y=10)
    sz = tk.StringVar()
    size = ttk.Combobox(root, width=2, textvariable=sz, state='readonly', font=('verdana', 10, 'bold'), )
    size['values'] = (8, 9, 10, 12, 15, 20, 23, 25, 27, 30, 35, 40, 43, 47, 50, 55, 65, 76, 80, 90, 100, 150, 200, 255, 300)
    size.place(x=350, y=30)
    size.current(0)
    sample = LabelFrame(root, text="Sample", height=100, width=200)
    sample['font'] = (fontss.get(), size.get(), style.get())
    sample.place(x=180, y=220)
    l4 = Label(sample, text="This is sample")
    l4.place(x=20, y=30)

    def okk():
        text['font'] = (fontss.get(), size.get(), style.get())
        root.destroy()

    ok = Button(root, text="OK", relief=RIDGE, borderwidth=2, padx=20, highlightcolor="blue", command=okk)
    ok.place(x=137, y=350)

    def apl():
        l4['font'] = (fontss.get(), size.get(), style.get())

    apply = Button(root, text="Apply", relief=RIDGE, borderwidth=2, padx=20, highlightcolor="blue", command=apl)
    apply.place(x=210, y=350)

    def cnl():
        root.destroy()

    cancel = Button(root, text="Cancel", relief=RIDGE, borderwidth=2, padx=20, command=cnl)
    cancel.place(x=295, y=350)
    root.mainloop()


def about():
    messagebox.showinfo("About", "This Notepad is created by Paras Udapurkar")


def view_help():
    webbrowser.open('#')


def send_feedback():
    webbrowser.open('#')


window = tk.Tk()
window.geometry('1000x500')
window.title('notepad')
# window.iconbitmap('notepad.ico')
menubar = Menu(window)
file = Menu(menubar, tearoff=0)
file.add_command(label="New", command=new)
file.add_command(label="New window", command=new_window)
file.add_command(label="Open", command=openn)
file.add_command(label="Save as", command=save_as)
file.add_separator()
file.add_command(label="Exit", command=exitt)
menubar.add_cascade(label="File", menu=file, font=('verdana', 10, 'bold'))
edit = Menu(menubar, tearoff=0)
edit.add_separator()
edit.add_command(label="Cut", accelerator="Ctrl+X", command=cut)
edit.add_command(label="Copy", accelerator="Ctrl+C", command=copy)
edit.add_command(label="Paste", accelerator="Ctrl+V", command=paste)
edit.add_command(label="Delete", accelerator="Del", command=delete)
edit.add_command(label="Select All", accelerator="Ctrl+A", command=select_all)
edit.add_command(label="Time/Date", accelerator="F5", command=time)
menubar.add_cascade(label="Edit", menu=edit)
Format = Menu(menubar, tearoff=0)
Format.add_command(label="Word Wrap")
Format.add_command(label="Font...", command=fonts)
menubar.add_cascade(label="Format", menu=Format)
Help = Menu(menubar, tearoff=0)
Help.add_command(label="View Help", command=view_help)
Help.add_command(label="Send FeedBack", command=send_feedback)
Help.add_command(label="About Notepad", command=about)
menubar.add_cascade(label="Help", menu=Help)
window.config(menu=menubar)
text = ScrolledText(window, width=1000, height=1000)
text.place(x=0, y=0)
window.mainloop()

