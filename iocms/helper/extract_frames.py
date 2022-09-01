import os
import cv2
import sys

# from django.conf import settings

from .constants import ATTENDANCE_MEDIA_ROOT


def frame_extractor(instance, dir_name) -> bool:
    """

    :param file_path:
    :param dir_name:
    :return:
    """
    video_path = instance.video._file.file.name
    video = cv2.VideoCapture(video_path)
    current_frame = 0
    media_dir = os.path.dirname(ATTENDANCE_MEDIA_ROOT)
    # a = os.path.join(media_dir, )
    # print(os.path.dirname(ATTENDANCE_MEDIA_ROOT))

    import pdb; pdb.set_trace()
    # directory = os.path.join(media_dir, dir_name) 
    directory = os.path.join(media_dir, dir_name) # C:\Users\gaurav\OneDrive - Nepal College of Information Technology\aithon-be-BACKUP\Aithon be\iw-acad-iocms-be\media\gauravjs\

    if not os.path.exists(directory):
        # sys.path.append(directory)
        os.makedirs(directory)
    dir_location = '{directory}\\frame_'.format(directory=directory)
    
    # frame_location = '{folder}/frame_'.format(folder=dir_location)

    # user_dir = 
    # if not os.path.exists('data'):
    #     os.makedirs('data')
    # success =True
    while current_frame<30:
        success, frame = video.read()

        # cv2.imshow("output video", frame)
        print(dir_location + str(current_frame) + '.jpg')
        cv2.imwrite(dir_location + str(current_frame) + '.jpg', frame)
        current_frame += 1

    video.release()
    cv2.destroyAllWindows()
    return True

