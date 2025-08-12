import os
'''
1. make the array list of people
2. traverse the araay people
3. and extract the name of each person and append in the last path
4. once folder is confirmed traverse the folder and take each image
5. convert to grayscale
6. use Haars cascader to get the face and append in feature and label array
'''
import cv2 as cv
import numpy as np
people=['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']
DIR=r'C:\Users\Hp\Desktop\Folders\Python\Faces\train'
features=[]
labels=[]
haar_cascade=cv.CascadeClassifier('haar_face.xml')

def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)
        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)
            for(x,y,w,h) in faces_rect:
                face_roi=gray[y:y+h,x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()
# print(len(features))
# print(len(labels))
print('Traning Done---------------->')
features=np.array(features,dtype='object')
labels=np.array(labels)
face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)
