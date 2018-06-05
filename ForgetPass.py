from tkinter import *
import tkinter as tk
from tempfile import NamedTemporaryFile
import shutil
import csv
from tkinter import messagebox


class Forget(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        font10 = "-family {Baskerville Old Face} -size 15 -weight bold" \
                 " -slant roman -underline 0 -overstrike 0"
        font11 = "-family {Comic Sans MS} -size 13 -weight bold -slant" \
                 " italic -underline 0 -overstrike 0"

        self.geometry("600x450+442+145")
        self.title("Forgot Password")
        self.configure(background="#cacaff")

        self.Label1 = Label(self)
        self.Label1.place(relx=0.12, rely=0.11, height=51, width=464)
        self.Label1.configure(background="#cacaff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Enter your user id and new password''')
        self.Label1.configure(width=464)

        self.Label2 = Label(self)
        self.Label2.place(relx=0.13, rely=0.31, height=31, width=84)
        self.Label2.configure(background="#cacaff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Userid''')
        self.Label2.configure(width=84)

        self.Label3 = Label(self)
        self.Label3.place(relx=0.13, rely=0.47, height=41, width=134)
        self.Label3.configure(background="#cacaff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font11)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''New Password''')
        self.Label3.configure(width=134)

        self.Entry1 = Entry(self)
        self.Entry1.place(relx=0.48, rely=0.31, height=30, relwidth=0.39)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=234)

        self.Entry2 = Entry(self)
        self.Entry2.place(relx=0.48, rely=0.47, height=30, relwidth=0.41)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=244)

        self.Button1 = Button(self,command=self.forgpass)
        self.Button1.place(relx=0.38, rely=0.64, height=34, width=177)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font11)
        self.Button1.configure(foreground="#4242ff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Change Password''')
        self.Button1.configure(width=177)

    def forgpass(self):
        u = self.Entry1.get()
        p = self.Entry2.get()

        filename = 'admininfo.csv'
        tempfile = NamedTemporaryFile(mode='w', delete=False)

        fields = ['Username', 'Userid', 'Password']

        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                if row['Userid'] == str(u):
                    row['Password'] = str(p)
                row = {'Username': row['Username'], 'Userid': row['Userid'], 'Password': row['Password']}
                writer.writerow(row)

        shutil.move(tempfile.name, filename)
        messagebox.showinfo("Done..", "Your password was changed successfully!")
        Forget.withdraw(self)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        Forget(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()