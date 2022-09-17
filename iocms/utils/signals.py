import json
import requests

from django.core.exceptions import ObjectDoesNotExist
# from django.db.models.signals import post_save

from helper.jpg_to_pgm import convert_registration_faces, convert_attendance_faces
# from users.models import RegisterVideo

DOMAIN = "http://192.168.1.129:8081"


def callJavaAPIForTraining(username):
    """
    
    """
    url = f"{DOMAIN}/uploading/{username}"

    file_root = "F:\\NCIT_P3\\aithon-be-BACKUP\\Aithon_be\\iw-acad-iocms-be\\media\\pgm_processed_registration\\"+username
    for i in range(1, 16):
        try:
            file = f"{file_root}\\{i}.pgm"
            data = {'dir':'/uploads/', 'submit':'Submit'}
            files = {'file':(file, open(file, 'rb'))}
            # files = {'file':('1.jpg', open('1.jpg', 'rb'))}
            r = requests.post(url, data=data, files=files)
            # print(type(r))
            print(r._content)
            print(url)
            # r_json = r.decode('utf-8')
            # print(json.dumps(r))
        except:
            pass


def callJavaAPIForVerification(username, email):
    """
    
    """
    url = f"{DOMAIN}/up/verify"
    file_root = "F:\\NCIT_P3\\aithon-be-BACKUP\\Aithon_be\\iw-acad-iocms-be\\media\\pgm_processed_attendance\\"+username
    for i in range(1, 14):
        try:
            file = f"{file_root}\\{i}.pgm"
            data = {'dir':'/uploads/', 'submit':'Submit', 'email':email, 'userID':username}
            files = {'file':(file, open(file, 'rb'))}
            # files = {'file':('1.jpg', open('1.jpg', 'rb'))}
            r = requests.post(url, data=data, files=files)
            print(r._content)
        except:
            pass

def train_registration_faces(sender, instance, created, **kwargs):
    """
    conver JPG images to PGM and then call the JAVA API for tarining the PGM images
    """
    # convert JPG to PGM
    res = convert_registration_faces(instance.user.username)
    print("registration image to pgm done!")
    # traing PGM images
    callJavaAPIForTraining(instance.user.username)

    print("called java api for registration")



def train_attendance_faces(sender, instance, created, **kwargs):
    """
    Convert JPG images to PGM and finally call the JAVA api for verification of user
    """
    # import pdb; pdb.set_trace() 
    res = convert_attendance_faces(instance.user.username)

    # call Java API for attendance is `res is True`
    # if res is False:
    #     raise ObjectDoesNotExist("The processed images of this user was not found!")
    # else:
        # call JAVA API
    callJavaAPIForVerification(instance.user.username, instance.user.email)
    print("called java api for verification")


# print("called")
# send("__init__.py")
if __name__ == "__main__":
    print("called")
    send("F:\\NCIT_P3\\aithon-be-BACKUP\\Aithon_be\\iw-acad-iocms-be\\media\\jpg_registration\\gaurav\\frame_4.jpg")
    send("F:\\NCIT_P3\\aithon-be-BACKUP\\Aithon_be\\iw-acad-iocms-be\\media\\jpg_registration\\gaurav\\frame_2.jpg")
    send("F:\\NCIT_P3\\aithon-be-BACKUP\\Aithon_be\\iw-acad-iocms-be\\media\\jpg_registration\\gaurav\\frame_3.jpg")
