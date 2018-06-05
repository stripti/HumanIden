from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import time
import os
import cv2
import numpy as np
from PIL import Image
import webcampage


class Train(tk.Toplevel):

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
        self.title("Please wait till training is done!")
        self.configure(background="#d9d9d9")

        self.TProgressbar1 = ttk.Progressbar(self)
        self.TProgressbar1.place(relx=0.03, rely=0.25, relwidth=0.95
                                 , relheight=0.0, height=22)
        self.TProgressbar1.configure(length="570")

        recogniser = cv2.face.LBPHFaceRecognizer_create()
        path = 'dataset'

        def getImagesWihID(path):
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            faces = []
            Ids = []
            for imagePath in imagePaths:
                faceImg = Image.open(imagePath).convert('L')
                faceNp = np.array(faceImg, 'uint8')
                ID = int(os.path.split(imagePath)[-1].split('.')[1])
                faces.append(faceNp)
                Ids.append(ID)
                cv2.waitKey(10)
            return np.array(Ids), faces

        Ids, faces = getImagesWihID(path)
        recogniser.train(faces, Ids)
        recogniser.save('recognizer/trainingData.yaml')
        cv2.destroyAllWindows()

        self.TProgressbar1["maximum"]=100
        for i in range(101):
            time.sleep(0.05)
            self.TProgressbar1["value"]=i
            self.TProgressbar1.update()
        self.TProgressbar1["value"]=0
        Train.withdraw(self)
        #webcampage.Webcam(self)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        tr = Train(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()