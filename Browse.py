from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import cv2
import tkinter as tk
import csv


def storage(nme, a):
    myfile = open(str(a)+".csv", 'w')
    newdata = nme + ","
    myfile.write("\n")
    myfile.write(str(newdata))
    myfile.close()



class Brow(tk.Toplevel):

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        font10 = "-family {Viner Hand ITC} -size 15 -weight bold " \
                 "-slant italic -underline 0 -overstrike 0"
        font12 = "-family Terminal -size 12 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"
        font13 = "-family {Lucida Handwriting} -size 14 -weight normal" \
                 " -slant roman -underline 0 -overstrike 0"

        self.geometry("600x450+439+128")
        self.title("Browse file")
        self.configure(background="#fed2b1")

        self.Label1 = Label(self)
        self.Label1.place(relx=0.13, rely=0.09, height=51, width=444)
        self.Label1.configure(background="#fed2b1")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#6c0000")
        self.Label1.configure(text='''Choose the video file for  monitoring..''')
        self.Label1.configure(width=444)

        self.Button2 = Button(self,command=self.track)
        self.Button2.place(relx=0.18, rely=0.47, height=44, width=357)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#620702")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font13)
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(relief=GROOVE)
        self.Button2.configure(text='''**Browse and  track**''')
        self.Button2.configure(width=357)

    global a


    def browse(self):
        root = Tk()
        root.withdraw()
        currdir = os.getcwd()
        a = askopenfilename(parent=root, initialdir=currdir, filetypes=(("Video File", "*.mp4,*.avi"), ("All Files", "*.*")),
                            title='Please select a directory')
        return a

    def track(self):
        a = self.browse()
        faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        cam = cv2.VideoCapture(a)
        rec = cv2.face.LBPHFaceRecognizer_create()
        rec.read("recognizer/trainingData.yaml")
        id1 = 0
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        while (True):
            (grabbed, img) = cam.read()
            if grabbed:# image is a color image so we need to convert to classifier
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
                                nme = line['name']
                                storage(nme,a)
                                cv2.putText(img, nme, (x, y + h), font, 2, (0, 0, 255), 2)

            cv2.imshow("face", img)
            if (cv2.waitKey(50) == ord('q')):
                break

        cam.release()
        cv2.destroyAllWindows()


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        Brow(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
