import cv2
from PIL import image
from flask import Flask
import numpy as np

obj_faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
class camera():
    def __init__(self, self.width, self.height):
        self.obj_camera = cv2.videoCapture(0)
        self.obj_camera.set(3, self.height)
        self.obj_camera.set(4, self.width)
    def outputVideo(self):
        self.bool_working, self.cameraOutput = self.obj_camera.read()
    
   