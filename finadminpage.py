from tkinter import *
import tkinter as tk
import register
import Splash
import webcampage
import remcampage
from tkinter import messagebox


class AdminPage1(tk.Toplevel):

    def __init__(self, parent):

        tk.Toplevel.__init__(self, parent)
        font10 = "-family {Monotype Corsiva} -size 16 -weight bold " \
                 "-slant italic -underline 0 -overstrike 0"
        font12 = "-family Forte -size 16 -weight bold -slant roman " \
                 "-underline 0 -overstrike 0"
        font11 = "-family {Comic Sans MS} -size 24 -weight bold -slant" \
                 " roman -underline 0 -overstrike 0"

        self.geometry("1324x660+-8+7")
        self.title("Admin Page")
        self.configure(background="#d9d9d9")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="black")

        self.Frame1 = Frame(self)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=0.14, relwidth=1.03)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#000000")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=1365)

        self.Button1 = Button(self.Frame1,command=self.add)
        self.Button1.place(relx=0.64, rely=0.21, height=54, width=127)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#c5f9bf")
        self.Button1.configure(borderwidth="5")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font10)
        self.Button1.configure(foreground="#22ab1b")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Add Admin''')

        self.Button2 = Button(self.Frame1,command=self.logout)
        self.Button2.place(relx=0.78, rely=0.21, height=44, width=107)
        self.Button2.configure(activebackground="#fcc9bc")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ffdfdd")
        self.Button2.configure(borderwidth="5")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font10)
        self.Button2.configure(foreground="#ff0000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Logout''')

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.07, rely=0.21, height=51, width=344)
        self.Label1.configure(background="#090009")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(text="Hello..")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(width=344)

        self.Frame3 = Frame(self)
        self.Frame3.place(relx=0.0, rely=0.14, relheight=0.9, relwidth=0.18)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(background="#4d3eb5")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")
        self.Frame3.configure(width=235)

        self.Button6 = Button(self.Frame3,command=self.web)
        self.Button6.place(relx=0.17, rely=0.32, height=47, width=161)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#fdf899")
        self.Button6.configure(borderwidth="5")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font=font12)
        self.Button6.configure(foreground="#809917")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Web Camera''')

        self.Button7 = Button(self.Frame3,command=self.rcam)
        self.Button7.place(relx=0.13, rely=0.52, height=47, width=183)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#fedbb8")
        self.Button7.configure(borderwidth="5")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font=font12)
        self.Button7.configure(foreground="#ff0000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''Remote Camera''')

        self.Frame2 = Frame(self)
        self.Frame2.place(relx=0.17, rely=0.14, relheight=0.9, relwidth=0.86)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#b4aee3")
        self.Frame2.configure(width=1135)

    def add(self):
        reg = register.Register(self.Frame2)

    def logout(self):
        log = Splash.Login(self.Frame2)
        AdminPage1.withdraw(self)
        messagebox.showinfo("Logged out", "You have successfully logged out..")

    def web(self):
        wc=webcampage.Webcam(self.Frame2)

    def rcam(self):
        rc = remcampage.Remcam(self.Frame2)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        adpage = AdminPage1(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
