import tkinter
from tkinter import *

"""master = Tk()

def main():
    listbox = Listbox(master)
    listbox.pack()

    listbox.insert(END, "a list entry")

    for item in ["one", "two", "three", "four"]:
        listbox.insert(END, item)

    mainloop()"""

"""def main():
    master = Tk()

    e = Entry(master)
    e.pack()

    e.focus_set()

    def callback():
        print(e.get())

    b = Button(master, text="get", width=10, command=callback)
    b.pack()

    mainloop()
    e = Entry(master, width=50)
    e.pack()

    text = e.get()
    def makeentry(parent, caption, width=None, **options):
        Label(parent, text=caption).pack(side=LEFT)
        entry = Entry(parent, **options)
        if width:
            entry.config(width=width)
        entry.pack(side=LEFT)
        return entry

    user = makeentry(parent, "User name:", 10)
    password = makeentry(parent, "Password:", 10, show="*")
    content = StringVar()
    entry = Entry(parent, text=caption, textvariable=content)

    text = content.get()
    content.set(text)"""

def main():
    master = Tk()

    e = Entry(master)
    e.pack()

    e.focus_set()
    """    
    def callback():
        print(e.get())
    
    b = Button(master, text="get", width=10, command=callback)
    b.pack()
    
    e = Entry(master, width=50)
    e.pack()
    """

    text = e.get()
    print(text)

    mainloop()

if __name__ == "__main__":
    main()