from tkinter import *
import tkinter as tk
import cv2
import webcampage
import numpy as np
from tkinter import messagebox


class Dataset(tk.Toplevel):

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font10 = "-family {Matura MT Script Capitals} -size 15 -weight" \
                 " bold -slant roman -underline 0 -overstrike 0"
        font9 = "-family {Comic Sans MS} -size 13 -weight bold -slant " \
                "roman -underline 0 -overstrike 0"
        font11 = "-family {Lucida Handwriting} -size 13 -weight bold " \
                 "-slant roman -underline 0 -overstrike 0"

        self.geometry("487x325+432+224")
        self.title("Create Dataset")
        self.configure(relief="raised")
        self.configure(background="#d0aeca")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="black")

        self.Label1 = Label(self)
        self.Label1.place(relx=0.0, rely=0.06, height=51, width=494)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#008080")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(relief=RAISED)
        self.Label1.configure(text='''..Please enter details of person to be identified..''')
        self.Label1.configure(width=494)

        self.Entry1 = Entry(self)
        self.Entry1.place(relx=0.35, rely=0.37, height=40, relwidth=0.34)
        self.Entry1.configure(background="#ffff80")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(relief=GROOVE)
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry2 = Entry(self)
        self.Entry2.place(relx=0.35, rely=0.57, height=40, relwidth=0.34)
        self.Entry2.configure(background="#ffff80")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(relief=GROOVE)
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Label2 = Label(self)
        self.Label2.place(relx=0.16, rely=0.39, height=31, width=74)
        self.Label2.configure(background="#d0aeca")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font11)
        self.Label2.configure(foreground="#a70501")
        self.Label2.configure(text='''Userid''')
        self.Label2.configure(width=74)

        self.Label3 = Label(self)
        self.Label3.place(relx=0.16, rely=0.59, height=31, width=74)
        self.Label3.configure(background="#d0aeca")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font11)
        self.Label3.configure(foreground="#a70501")
        self.Label3.configure(text='''Name''')
        self.Label3.configure(width=74)

        self.Button1 = Button(self, command=self.click)
        self.Button1.place(relx=0.41, rely=0.78, height=42, width=102)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#934900")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#dcc8b6")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Click pics''')

    def click(self):
        id = self.Entry1.get()
        name = self.Entry2.get()

        myfile = open("datasetinfo.csv", "a+")
        newdata = id + "," + name
        myfile.write("\n")
        myfile.write(str(newdata))
        myfile.close()

        faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        cam = cv2.VideoCapture(0)
        sampleNum = 0

        while (True):
            ret, img = cam.read()  # image is a color image so we need to convert to classifier
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceDetect.detectMultiScale(gray, 1.3,
                                                5)  # detects all faces in current frame and return coordinates of face
            for (x, y, w, h) in faces:
                sampleNum = sampleNum + 1
                # cv2.imwrite("dataset/User." + id + "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                cv2.imwrite("dataset/User." + str(id) + "." + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.waitKey(200)
            cv2.imshow("face", img)
            cv2.waitKey(1)
            if (sampleNum > 10):
                break
        cam.release()
        cv2.destroyAllWindows()
        Dataset.withdraw(self)
        messagebox.showinfo("Done..", "Dataset has been created!!")
        webcampage.Webcam(self)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        datacr = Dataset(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
