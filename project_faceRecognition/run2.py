import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
print(cv2.__version__)
# Get the training data we previously made
data_path = "C:\\Users\\admin\\Desktop\\NCU\\Projects sem 1-2-3-4-5\\Full Python Proj\\project_faceRecognition\\project_pics\\"
# a=listdir('d:/faces')
# print(a)
# """
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

# Create arrays for training data and labels
Training_Data, Labels = [], []

# Open training images in our datapath
# Create a numpy array for training data
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)
# 
# Create a numpy array for both training data and labels
Labels = np.asarray(Labels, dtype=np.int32)
model=cv2.face_LBPHFaceRecognizer.create()
# Initialize facial recognizer
# model = cv2.face_LBPHFaceRecognizer.create()
# model=cv2.f


# Let's train our model 
model.train(np.asarray(Training_Data), np.asarray(Labels))
print("Model trained sucessefully")














face_classifier = cv2.CascadeClassifier("C:\\Users\\admin\\Desktop\\NCU\\Projects sem 1-2-3-4-5\\Full Python Proj\\project_faceRecognition\\haarcascade_frontalface_default.xml")

def face_detector(img,size=0.5):
    
	# Convert image to grayscale
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = face_classifier.detectMultiScale(gray,scaleFactor = 1.3,minNeighbors=5)
	if faces is ():
		return img,[]
    
	for x,y,w,h in faces:
		resized=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
		resized1 = img[y:y+h,x:x+w]
		resized1 = cv2.resize(resized1,(200,200))
	return img,resized1


# Open Webcam
video = cv2.VideoCapture(0)

while True:

	check,frame = video.read()
    
	image,face = face_detector(frame)
    
	try:
		face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

        # Pass face to prediction model
        # "results" comprises of a tuple containing the label and the confidence value
		results = model.predict(face)
		
		if results[1] < 500:
			confidence = int( 100 * (1 - (results[1])/400) )
			display_string = str(confidence)+'% Confident it is User'
        
		cv2.putText(image,display_string,(100, 50),cv2.FONT_HERSHEY_COMPLEX,1,(120,225,120),2)
        
		if confidence > 20:
			cv2.putText(image,"Aayush Agarwal",(250, 120),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
			cv2.putText(image,"18csu004",(250, 450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
			cv2.imshow('Face Recognition',image)

		
		else:
			cv2.putText(image,"Locked",(250, 450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
			
			cv2.imshow('Face Recognition', image )

	except:
		cv2.putText(image,"No Face Found",(220, 120),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
		cv2.putText(image,"Locked",(250, 450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
		cv2.imshow('Face Recognition',image)
		pass
        
	if cv2.waitKey(1) == ord('q'):
		break
video.release()
cv2.destroyAllWindows()   


