from tkinter import *
import tkinter as tk
import datasetcreate
import training
import detector


class Webcam(tk.Toplevel):

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        font9 = "-family {Comic Sans MS} -size 15 -weight bold -slant " \
                "roman -underline 0 -overstrike 0"

        self.geometry("600x450+394+128")
        self.title("Web Camera")
        self.configure(background="#d9d9d9")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="black")

        self.Frame1 = Frame(self)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=0.14, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#070707")
        self.Frame1.configure(width=725)

        self.Button1 = Button(self.Frame1, command=self.iden)
        self.Button1.place(relx=0.14, rely=0.27, height=44, width=127)
        self.Button1.configure(activebackground="#a9abb4")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d2d2d2")
        self.Button1.configure(borderwidth="5")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#730e8c")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Identify''')
        self.Button1.configure(width=127)

        self.Button2 = Button(self.Frame1, command=self.train)
        self.Button2.place(relx=0.41, rely=0.27, height=44, width=117)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#e7cbe6")
        self.Button2.configure(borderwidth="5")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font9)
        self.Button2.configure(foreground="#a3369f")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Training''')
        self.Button2.configure(width=117)

        self.Button3 = Button(self.Frame1, command=self.track)
        self.Button3.place(relx=0.72, rely=0.27, height=44, width=107)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#e7b8df")
        self.Button3.configure(borderwidth="5")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font9)
        self.Button3.configure(foreground="#804040")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Tracking''')
        self.Button3.configure(width=107)

        self.Frame2 = Frame(self)
        self.Frame2.place(relx=0.0, rely=0.13, relheight=0.84, relwidth=1.0)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="5")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#b6bde0")
        self.Frame2.configure(width=725)

    def iden(self):
        Webcam.withdraw(self)
        dc = datasetcreate.Dataset(self)

    def train(self):
        # Webcam.withdraw(self)
        training.Train(self)

    def track(self):
        Webcam.withdraw(self)
        detector.Detect()
        Webcam(self)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        wcpage = Webcam(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
