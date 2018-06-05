from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import time
import Browse
import Dwnload


class Remcam(tk.Toplevel):

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        font9 = "-family {Comic Sans MS} -size 15 -weight bold -slant " \
                "roman -underline 0 -overstrike 0"

        self.geometry("600x450+394+128")
        self.title("Rem Camera")
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

        self.Button1 = Button(self.Frame1, command=self.syn)
        self.Button1.place(relx=0.14, rely=0.27, height=44, width=137)
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
        self.Button1.configure(text='''Synchronize''')
        self.Button1.configure(width=127)

        self.Button2 = Button(self.Frame1, command=self.browse)
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
        self.Button2.configure(text='''Monitoring''')
        self.Button2.configure(width=117)

        self.Frame2 = Frame(self)
        self.Frame2.place(relx=0.0, rely=0.13, relheight=0.84, relwidth=1.0)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="5")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#b6bde0")
        self.Frame2.configure(width=725)

    def syn(self):
        Download(self.Frame2)
        Dwnload.main()

    def browse(self):
        Browse.Brow(self)


class Download(tk.Toplevel):

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        '''This class configures and populates the toplevel window.
                    top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        self.geometry("600x81+368+257")
        self.title("Downloading...!")
        self.configure(background="#d9d9d9")

        self.TProgressbar1 = ttk.Progressbar(self)
        self.TProgressbar1.place(relx=0.03, rely=0.25, relwidth=0.95
                                     , relheight=0.0, height=22)
        self.TProgressbar1.configure(length="570")
        self.TProgressbar1["maximum"] = 100
        for i in range(101):
            time.sleep(0.05)
            self.TProgressbar1["value"] = i
            self.TProgressbar1.update()
        self.TProgressbar1["value"] = 0
        Download.withdraw(self)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        rcpage = Remcam(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
