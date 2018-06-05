from tkinter import *
import tkinter as tk
from tkinter import messagebox
import csv


class Register(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)

        font12 = "-family {MV Boli} -size 15 -weight bold -slant " \
                 "italic -underline 0 -overstrike 0"
        font13 = "-family {Comic Sans MS} -size 15 -weight bold -slant" \
                 " italic -underline 0 -overstrike 0"
        font9 = "-family {MV Boli} -size 24 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        self.geometry("614x467+358+106")
        self.title("..Add Admin..")
        self.configure(background="#acd591")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="black")

        self.Label1 = Label(self)
        self.Label1.place(relx=0.34, rely=0.09, height=41, width=294)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#acd591")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''*Registration*''')

        self.Label2 = Label(self)
        self.Label2.place(relx=0.13, rely=0.3, height=41, width=134)
        self.Label2.configure(background="#acd591")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''User Name''')
        self.Label2.configure(width=134)

        self.Label3 = Label(self)
        self.Label3.place(relx=0.13, rely=0.47, height=31, width=114)
        self.Label3.configure(background="#acd591")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''Userid''')
        self.Label3.configure(width=114)

        self.Label4 = Label(self)
        self.Label4.place(relx=0.15, rely=0.58, height=41, width=114)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#acd591")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground="#ffffff")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Password''')

        self.Entry1 = Entry(self)
        self.Entry1.place(relx=0.42, rely=0.32, height=30, relwidth=0.38)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=234)

        self.Entry2 = Entry(self)
        self.Entry2.place(relx=0.42, rely=0.47, height=30, relwidth=0.38)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=234)

        self.Entry3 = Entry(self, show='*')
        self.Entry3.place(relx=0.42, rely=0.6, height=30, relwidth=0.38)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(width=234)

        self.Button1 = Button(self, command=self.valid)
        self.Button1.place(relx=0.42, rely=0.77, height=44, width=137)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#efa3e8")
        self.Button1.configure(disabledforeground="#c0c0c0")
        self.Button1.configure(font=font13)
        self.Button1.configure(foreground="#e90718")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Register''')
        self.Button1.configure(width=137)

    def valid(self):

        n = self.Entry1.get()
        u = self.Entry2.get()
        p = self.Entry3.get()
        myfile = open("admininfo.csv", "a+")
        newdata = n + "," + u + "," + p
        myfile.write("\n")
        myfile.write(str(newdata))
        myfile.close()
        messagebox.showinfo("Success", "Registered successfully ")
        Register.withdraw(self)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        regpage = Register(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()