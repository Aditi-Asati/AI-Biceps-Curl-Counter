from array import array
from itertools import count
from tkinter import Image
import PIL
import numpy as np
import cv2
from sklearn.svm import LinearSVC

class Model:

    def __init__(self):
        self.model = LinearSVC()
    
    def train_model(self, counters):
        img_list = np.array([])
        class_list = np.array([])

        for i in range(1, counters[0]):
            img = cv2.imread(f"1/frame{i}.jpg")[:,:,0]
            img = img.reshape(16950)
            img_list = np.append(img_list, [img])
            class_list = np.append(class_list, 1)


        for i in range(1, counters[1]):
            img = cv2.imread(f"2/frame{i}.jpg")[:,:,0]
            img = img.reshape(16950)
            img_list = np.append(img_list, [img])
            class_list = np.append(class_list, 2)
        
        img_list = img_list.reshape(counters[0] + counters[1] - 2, 16950)
        self.model.fit(img_list, class_list)
        print("Model successfully trained!")

    def predict(self, frame):
        frame = frame[1]
        cv2.imwrite("frame.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))
        img = PIL.Image.open("frame.jpg")
        img.thumbnail((150,150), PIL.Image.ANTIALIAS)
        img.save("frame.jpg")

        img = cv2.imread("frame.jpg")[:,:,0]
        img = img.reshape(16950)
        prediction = self.model.predict([img])
        return prediction[0]