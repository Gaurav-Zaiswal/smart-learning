import os
import sys 

from django.conf import settings

# create new dir `attendance` within `MEDIA_ROOT`
# MEDIA_ROOT = os.path.join(os.path.dirname(settings.MEDIA_ROOT), 'attendance')

ATTENDANCE_MEDIA_ROOT = os.path.join(settings.MEDIA_ROOT, 'media')
# ATTENDANCE_MEDIA_ROOT = sys.path.append(os.path.join(ATTENDANCE_MEDIA, 'attendance'))

# if not os.path.exists(ATTENDANCE_MEDIA_ROOT):
#         os.makedirs('data')