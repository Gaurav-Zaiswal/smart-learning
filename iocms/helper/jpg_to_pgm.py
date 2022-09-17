# from curses import def_shell_mode
from re import I
import shutil
import cv2
import sys
import os

def detect_save(sourcePath, destinationPath):
    # cascPath = "C:\\Users\gaurav\\OneDrive - Nepal College of Information Technology\aithon-be-BACKUP\\Aithon be\\iw-acad-iocms-be\\iocms\\helper\\front.xml"
    # print("within detect_save function")
    cascPath = "F:\\front.xml"
    # os.chmod(cascPath, 0o444)
    faceCascade = cv2.CascadeClassifier(cascPath)
    full_image = cv2.imread(sourcePath)

    # image = cv2.resize(full_image, (1000, 1000), interpolation = cv2.INTER_AREA)

    image0 = cv2.resize(full_image, (400, 400), interpolation = cv2.INTER_AREA)
    image = cv2.rotate(image0, cv2.ROTATE_180)

    # image0 = cv2.rotate(full_image, cv2.ROTATE_180)
    # image = cv2.resize(image0, (500, 500), interpolation = cv2.INTER_AREA)
 

    faces = faceCascade.detectMultiScale(
        cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # if(len(faces) != 1):
    #     print("fail")
    #     return -1
    print(faces)
    for (x, y, w, h) in faces:
        try:
            x1 = int(x-h/1.5)
            y1 = int(y)
            x2 = int(x+h)
            y2 = int(y+w)
            img = image[y1:y2, x1:x2]
            detected = cv2.resize(img, (92, 112), interpolation = cv2.INTER_AREA)
            bw = cv2.cvtColor(detected, cv2.COLOR_BGR2GRAY)
            print(destinationPath)
            cv2.imwrite(destinationPath, bw)
            print("within detect save")
            return 1
        except:
            pass

def process(sourceDirectory, destinationDirectory):
    properCount = 1
    root = "F:\\NCIT_P3\\aithon-be-BACKUP\\Aithon_be\\iw-acad-iocms-be\\media\\"
    source = root + "jpg_registration\\"
    destination = root + "pgm_processed\\"
    print("within process function")
    for filename in os.listdir(sourceDirectory):
        f = os.path.join(sourceDirectory, filename)
        # import pdb; pdb.set_trace()
        if os.path.isfile(f):
            print("is a file")
            if (detect_save(f, destinationDirectory + "\\" + str(properCount) + ".pgm") == 1):
                properCount = properCount + 1
            # if (properCount == 21):
            #     return 1
    # if properCount == 1: 
    #     return 0
    # return -1

def convert_registration_faces(username):
    root = "F:\\NCIT_P3\\aithon-be-BACKUP\\Aithon_be\\iw-acad-iocms-be\\media\\"
    source = root + "jpg_registration\\" + username
    destination = root + "pgm_processed_registration\\" + username
    if not os.path.exists(destination):
        os.mkdir(destination)
    # i= process(source, destination)
    # if i != 1:
    #     shutil.rmtree(destination)
    print("within convert_regitration_face")
    process(source, destination)
    
        


def convert_attendance_faces(username):
    root = "F:\\NCIT_P3\\aithon-be-BACKUP\\Aithon_be\\iw-acad-iocms-be\\media\\"
    source = root + "jpg_attendance\\" + username
    destination = root + "pgm_processed_attendance\\" + username
    if not os.path.exists(destination):
        # return None
        os.mkdir(destination)
    # i= process(source, destination)
    # if i != 1:
    #     shutil.rmtree(destination)
    #     return False 
    # return True
    print("within convert_attendence_face")
    process(source, destination)


if __name__ == "__main__":
    source = "F:\\NCIT_P3\\aithon-be-BACKUP\\Aithon_be\\iw-acad-iocms-be\\media\\jpg_registration\\sameer"
    dest = "F:\\NCIT_P3\\aithon-be-BACKUP\\Aithon_be\\iw-acad-iocms-be\\iocms\\data_pgm"
    # process(source, dest)

    convert_registration_faces("sameer")
    convert_attendance_faces("gauravjs")