import uuid
# import Pillow

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save

# from helper.extract_frames import frame_extractor
from helper.extract_frames import frame_extractor_registration
from utils.signals import train_attendance_faces, train_registration_faces
# from utils.signals import train_faces

#
# User = get_user_model()


def profile_pic_path(instance, filename):
    # checks jpg exttension
    extension = filename.split('.')[1]
    if len(filename.split('.')) != 2:
        raise ValidationError("image seems currupted...")
    if extension not in ['jpg', 'jpeg']:
        raise ValidationError("we currently accept jpg/jpeg formats only.")
    unique_name = uuid.uuid4().hex[:4]
    username = str(instance).split("-")[0].strip()
    # return 'author_pictures/' + unique_name + '.' + extension
    return 'user_pictures/' + username +"_" + unique_name + '.' + extension


def attendence_pic_path(instance, filename):
    username = str(instance).split("-")[0].strip()

    # checks jpg exttension
    extension = filename.split('.')[1]
    if len(filename.split('.')) != 2:
        raise ValidationError("image seems currupted...")
    if extension not in ['jpg', 'jpeg']:
        raise ValidationError("we currently accept jpg/jpeg formats only.")
    unique_name = uuid.uuid4().hex[:12]
    # calling frame extractor
    return 'for-attendence/' + unique_name + '.' + extension


def register_video_path(instance, filename):
    username = str(instance).split("-")[0].strip()
    # import pdb; pdb.set_trace()
    # checks jpg exttension
    extension = filename.split('.')[1]
    if len(filename.split('.')) != 2:
        raise ValidationError("video seems currupted...")
    if extension not in ['mp4', 'mkv', 'webm', 'MP4', 'MKV', 'WEBM']:
        raise ValidationError("video format cannot be accepted!")
    unique_name = uuid.uuid4().hex[:6]
    frame_extractor_registration(instance=instance, dir_name=username)
    return 'register_video' + unique_name + '.' + extension



class User(AbstractUser):
    # adding custom field
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # now user can log in using email
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  # here, email is already a required field

    def __str__(self):
        return self.username


class Student(models.Model):
    # adding custom field
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    # adding custom field
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    image = models.ImageField(upload_to=profile_pic_path)


class Images(models.Model):
    """
    students should be able to upload multiple images of themselves
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=profile_pic_path)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.image}"


class AttendenceImage(models.Model):
    """
    upload image that will be matched with images of `Images` model for attendence
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='image_for_attendance')
    image1 = models.ImageField(upload_to=attendence_pic_path)
    # image2 = models.ImageField(upload_to=attendence_pic_path)
    # image3 = models.ImageField(upload_to=attendence_pic_path)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.image}"


class RegisterVideo(models.Model):
    """
    upload video 
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='register_registration')
    video = models.FileField(upload_to=register_video_path)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.video}"

post_save.connect(train_registration_faces, sender=RegisterVideo)