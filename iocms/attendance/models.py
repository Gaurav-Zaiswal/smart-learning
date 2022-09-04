import uuid

from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from helper.extract_frames import frame_extractor_attendence
from utils.signals import train_attendance_faces
from users.models import User

from users.models import Student


def video_renaming(instance, filename):
    extension = filename.split('.')[1]
    if len(filename.split('.')) != 2:
        raise ValidationError("Video seems corrupted...")
    if extension not in ['mp4', 'MP4', 'WEBM', 'MKV']:
        raise ValidationError("we currently accept mp4, webm, and mkv formats only.")
    unique_name = uuid.uuid4().hex[:8]
    # print('author_pictures/' + unique_name + '.' + extension)
    return 'attendance_video/' + unique_name + '.' + extension


def attendance_video_path(instance, filename):
    username = str(instance).split("-")[0].strip()
    # import pdb; pdb.set_trace()
    # checks jpg exttension
    extension = filename.split('.')[1]
    if len(filename.split('.')) != 2:
        raise ValidationError("video seems currupted...")
    if extension not in ['mp4', 'mkv', 'webm', 'MP4', 'MKV', 'WEBM']:
        raise ValidationError("video format cannot be accepted!")
    unique_name = uuid.uuid4().hex[:6]
    frame_extractor_attendence(instance=instance, dir_name=username)
    return 'register_video' + unique_name + '.' + extension


# Create your models here.
class AttendanceVideoModel(models.Model):
    user = models.ForeignKey(User, related_name="user_id", on_delete=models.CASCADE)
    video = models.FileField(upload_to=attendance_video_path)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.video}"


post_save.connect(train_attendance_faces, sender=AttendanceVideoModel)
