import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from user1.models import Reports
from user2.models import Checking




#from time import sleep

   
def run():
    
    for i in Checking.objects.raw('SELECT * FROM user2_checking'):
        
        #print(i.u2_image)
        x=i.u2_image
        
        y=str(x)[9:]
        #print(y)
        
    return classify_face("media/test_img/"+y)
    
    
    
def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("media/images"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face=[]
                face = fr.load_image_file("media/images/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded


def unknown_image_encoded(img):
    """
    encode a face given the file name
    """
    face = fr.load_image_file("media/images/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding


def classify_face(im):
    
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im, 1)
    #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    #img = img[:,:,::-1]
    
    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img,face_locations)

    face_names = ""
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            face_names=name
            print(face_names)
        #x="images/"+face_names+".jpg"
        x="images/"+face_names+".jpg"
        print("msg"+x)
        '''for j in Reports.objects.raw('SELECT * FROM user1_reports WHERE u_image= %s',[x]):
            print(j)
            print(j.title)
            print('hii')'''
        if face_names!="":
            j=Reports.objects.select_related().get(u_image=x)
            return j.title
        else:
            return "1"
        

if __name__=='__main__':
    run()



