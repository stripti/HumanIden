from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time
import finadminpage
import ForgetPass
import cv2
import csv


class Splash(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Human Identification in Real Time System")
        # root = tk.Tk()
        # root.overrideredirect(True)
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("{0}x{1}+0+0".format(width, height))
        image_file = "images/img.gif"
        image = tk.PhotoImage(file=image_file)
        canvas = tk.Canvas(self, height=height, width=width, bg="brown")
        canvas.create_image(width / 2, height / 2, image=image)
        canvas.pack()
        ## required to make window show before the program gets to the mainloop
        # self.after(5000, self.destroy)
        # self.mainloop()
        self.update()


def detect(n):
    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read("recognizer/trainingData.yaml")
    id1 = 0
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    while (True):
        ret, img = cam.read()  # image is a color image so we need to convert to classifier
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3,
                                            5)  # detects all faces in current frame and return coordinates of face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id1, conf = rec.predict(gray[y:y + h, x:x + w])
            fields = ['id', 'name']
            with open('datasetinfo.csv', 'r') as f:
                d_reader = csv.DictReader(f, fieldnames=fields)

                for line in d_reader:
                    if line['id'] == str(id1):
                        nme = " "
                        nme = line['name']

        cv2.imshow("face", img)
        if (cv2.waitKey(1) == ord('q') or nme != ""):
            break

    cam.release()
    # cv2.destroyAllWindows()
    if n == nme:
        return 1
    else:
        return 0


class Login(tk.Toplevel):
    uname = ""

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)

        font12 = "-family {MV Boli} -size 15 -weight bold -slant " \
                 "italic -underline 0 -overstrike 0"
        font11 = "-family Terminal -size 9 -weight normal -slant roman" \
                 " -underline 1 -overstrike 0"
        font13 = "-family {Comic Sans MS} -size 15 -weight bold -slant" \
                 " italic -underline 0 -overstrike 0"
        font9 = "-family {MV Boli} -size 24 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        self.geometry("614x467+358+106")
        self.title("Login page")
        self.configure(background="#000088")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="black")

        self.Label1 = Label(self)
        self.Label1.place(relx=0.37, rely=0.09, height=41, width=174)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#000088")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''!!!Login!!!''')

        self.Label2 = Label(self)
        self.Label2.place(relx=0.13, rely=0.3, height=41, width=134)
        self.Label2.configure(background="#000088")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''User Name''')
        self.Label2.configure(width=134)

        self.Label3 = Label(self)
        self.Label3.place(relx=0.13, rely=0.47, height=31, width=114)
        self.Label3.configure(background="#000088")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''Userid''')
        self.Label3.configure(width=114)

        self.Label4 = Label(self)
        self.Label4.place(relx=0.15, rely=0.58, height=41, width=114)
        self.Label4.configure(background="#000088")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font12)
        self.Label4.configure(foreground="#ffffff")
        self.Label4.configure(text='''Password''')
        self.Label4.configure(width=114)

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
        self.Button1.place(relx=0.42, rely=0.79, height=44, width=137)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#efa3e8")
        self.Button1.configure(disabledforeground="#c0c0c0")
        self.Button1.configure(font=font13)
        self.Button1.configure(foreground="#e90718")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Log-in''')
        self.Button1.configure(width=137)

        self.Button2 = Button(self, command=self.forget)
        self.Button2.place(relx=0.18, rely=0.71, height=24, width=277)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#000088")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font11)
        self.Button2.configure(foreground="#c0c0c0")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Forgot Password? Click here!''')
        self.Button2.configure(width=257)

    def valid(self):
        n = self.Entry1.get()
        u = self.Entry2.get()
        p = self.Entry3.get()

        stri = n + "," + u + "," + p
        flag1 = 0

        with open("admininfo.csv") as fh:
            for row in fh:
                if stri in row:
                    flag1 += 1

        flag2 = detect(n)
        if flag1 != 0 and flag2 != 0:
            Login.uname = n
            finadminpage.AdminPage1(self)
            Login.withdraw(self)
            messagebox.showinfo("Say Hello", "Hello " + str(Login.uname))

        elif flag1 == 0:
            messagebox.showwarning("Alert", "Invalid user id or password!! ")
        elif flag2 == 0:
            messagebox.showwarning("Alert", "Invalid user in front of screen!! ")

    def forget(self):
        ForgetPass.Forget(self)

        self.mainloop()


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        splash = Splash(self)
        ## setup stuff goes here
        login = Login(self)

        ## simulate a delay while loading
        time.sleep(3)

        ## finished loading so destroy splash
        splash.destroy()
        ## show window again
        # self.deiconify()
        # login.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
