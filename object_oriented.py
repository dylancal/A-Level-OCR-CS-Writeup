import cv2
from PIL import image
from flask import Flask
import numpy as np
import mysql.connector
obj_faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

class camera():
    def __init__(self, width, height):
        self.obj_camera = cv2.videoCapture(0)
        self.obj_camera.set(3, self.height)
        
        self.obj_camera.set(4, self.width)
    def outputVideo(self):
        self.bool_working, self.cameraOutput = self.obj_camera.read()
        return self.cameraOutput
        
    def release(self):
        self.obj_camera.release()
        cv2.destroyAllWindows()

def cascadeDetction(obj_frame, obj_faceCascade):
    matrix_faces = obj_faceCascade.detectMultiscale(
        cv2.cvtColor(obj_frame, cv2.COLOR_BGR2GRAY), 
        scaleFactor = 1.2, 
        minNeighbors = 5,
        minSize = (30, 30)
    )
    for (originX, originY, displacedX, displacedY) in matrix_faces:
        cv2.rectangle(
            obj_frame,
            (originX, originY),
            (originX + displacedX, originY + displacedY),
            (255, 255, 255),
            4
        )
    return self.obj_frame


class usersDatabase():
    def __init__(self, username, password):
        
    def linkDatabase(self):
        self.mydb = msql.connector.connect(
            host = "localhost",
            user = "raspiDatabase",
            password = "raspiPassword"
        )
    
    def createDatabase(self, name)
        self.dbCursor = self.mydb.cursor()
        self.dbCursor.execute("CREATE DATABASE usersDatabase")
    
    def openDatabase(self, username, password, database):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user=str(username),
            password=str(password),
            database=str(database)
        )
    
    def appendRecord(self):
        print("hello")
    
    
def faceDetection(obj_frame, obj_faceCascade, obj_recogniser)