import cv2
import numpy as np
import csv


def Detect():
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
            with open('datasetinfo.csv', 'r') as f:
                d_reader = csv.DictReader(f)

                # get fieldnames from DictReader object and store in list
                headers = d_reader.fieldnames
                for line in headers:
                    if line[0] == str(id1):
                        nme = line[1]
                        cv2.putText(img, nme, (x, y + h), font, 2, (0, 0, 255), 2)
                        print(str(id1))

                        ''' with open('datasetinfo.csv', 'r') as f:
 d_reader = csv.DictReader(f)

 # get fieldnames from DictReader object and store in list
 headers = d_reader.fieldnames

 for line in d_reader:
     # print value in MyCol1 for each row
     print(line['name'])'''
        cv2.imshow("face", img)
        if (cv2.waitKey(1) == ord('q')):
            break
    cam.release()
    cv2.destroyAllWindows()
