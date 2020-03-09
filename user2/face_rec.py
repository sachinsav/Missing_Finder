import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep

class Face():
    def run(self):
        print(self.classify_face("test.jpg"))
    def get_encoded_faces(self):
        """
        looks through the faces folder and encodes all
        the faces
        """
        encoded = {}

        for dirpath, dnames, fnames in os.walk("../media/faces"):
            for f in fnames:
                if f.endswith(".jpg") or f.endswith(".png"):
                    face = fr.load_image_file("../media/faces/" + f)
                    encoding = fr.face_encodings(face)[0]
                    encoded[f.split(".")[0]] = encoding

        return encoded


    def unknown_image_encoded(self,img):
        """
        encode a face given the file name
        """
        face = fr.load_image_file("../media/faces/" + img)
        encoding = fr.face_encodings(face)[0]

        return encoding


    def classify_face(self,im):
    
        self.faces = self.get_encoded_faces()
        self.faces_encoded = list(self.faces.values())
        self.known_face_names = list(self.faces.keys())

        self.img = cv2.imread(im, 1)
        #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        #img = img[:,:,::-1]
    
        self.face_locations = face_recognition.face_locations(self.img)
        self.unknown_face_encodings = face_recognition.face_encodings(self.img, self.face_locations)

        self.face_names = []
        for face_encoding in self.unknown_face_encodings:
            # See if the face is a match for the known face(s)
            self.matches = face_recognition.compare_faces(self.faces_encoded, face_encoding)
            self.name = "Unknown"

            # use the known face with the smallest distance to the new face
            self.face_distances = face_recognition.face_distance(self.faces_encoded, face_encoding)
            self.best_match_index = np.argmin(self.face_distances)
            if self.matches[self.best_match_index]:
                self.name = self.known_face_names[self.best_match_index]

            self.face_names.append(self.name)

            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                # Draw a box around the face
                cv2.rectangle(self.img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

                # Draw a label with a name below the face
                cv2.rectangle(self.img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
                self.font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(self.img, name, (left -20, bottom + 15), self.font, 1.0, (255, 255, 255), 2)


        # Display the resulting image
        while True:

            cv2.imshow('Video',self.img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return self.face_names 


 

Face().run()
