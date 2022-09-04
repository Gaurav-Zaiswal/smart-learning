from django.core.exceptions import ObjectDoesNotExist
# from django.db.models.signals import post_save

from helper.jpg_to_pgm import convert_registration_faces, convert_attendance_faces
# from users.models import RegisterVideo


def train_registration_faces(sender, instance, created, **kwargs):
    convert_registration_faces(instance.user.username)


def train_attendance_faces(sender, instance, created, **kwargs):
    # import pdb; pdb.set_trace() 
    res = convert_attendance_faces(instance.user.username)

    # call Java API for attendance is `res is True`
    if res is False:
        raise ObjectDoesNotExist("The processed images of this user was not found!")
    else:
        # call JAVA API
        pass