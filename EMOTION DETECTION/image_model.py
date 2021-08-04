import keras
from keras.optimizers import Adam
import cv2
import numpy as np


class Image_Model:


    def camera_input(self):
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        face = cv2.resize(frame, (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(face, 1.3, 5)

        for (x,y,w,h) in faces:
            img = cv2.rectangle(face,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imshow('img',img)
            file_name_path = r'C:\Users\Piyush\Desktop\Bharat\EMOTION DETECTION\image_output'+'.jpg'
            cv2.imwrite(file_name_path, img)
            cv2.waitKey(1) 
            
        cap.release()
        cv2.destroyAllWindows()      
        print("Collecting Samples Complete")
    
    def predict_image(self):
        EMOTIONS = ['ANGRY','DISGUST','FEAR','HAPPY', 'NEUTRAL','SAD','SURPRISE']
        model = keras.models.load_model(r"C:\Users\Piyush\Desktop\Bharat\EMOTION DETECTION\camera_model")
        model.load_weights(r"C:\Users\Piyush\Desktop\Bharat\EMOTION DETECTION\camera_model_weights.h5")
        opt = Adam(lr=0.0005)
        model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
        image = cv2.imread(r'C:\Users\Piyush\Desktop\Bharat\EMOTION DETECTION\image_output.jpg')
        image=cv2.resize(image  , (48 , 48))
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        image = image[np.newaxis, :, :, np.newaxis]
        res=model.predict(image)
        print(EMOTIONS[res.argmax()])
        return EMOTIONS[res.argmax()]

