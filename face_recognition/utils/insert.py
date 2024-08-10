import face_recognition
import mysql.connector
import pickle as pkl
import numpy as np
import cv2

insert_query = "INSERT INTO face_encodings(name, encoding) values(%s, %s)"
load_query = "SELECT * FROM face_encodings"

def insert(file_path, name):
    print("insert.....")

    config = {
        "host": "localhost",
        "port": 3306,
        "database": "face_attendance_system",
        "user": "root",
        "password": "",
        "charset": "utf8",
        "use_unicode": True,
        "get_warnings": True,
    }
    
    cnx = mysql.connector.connect(**config)
    cur = cnx.cursor()

    frame = cv2.imread(file_path)

    face_locations = face_recognition.face_locations(frame)
    print("faces detected : ", len(face_locations))
    if len(face_locations) <= 0:
        return False
    
    image = face_recognition.load_image_file(file_path)
    face_encoding = face_recognition.face_encodings(image)[0]
    print(face_encoding)
    
    cur.execute(insert_query, (name, pkl.dumps(face_encoding), ))
    cnx.commit()

    cur.close()
    cnx.close()

    return True



if __name__ == "__main__":
    pass

   
        
   