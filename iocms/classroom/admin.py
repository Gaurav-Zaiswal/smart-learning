from django.contrib import admin

from .models import Classroom, ClassroomStudents, Rating

# Register your models here.
admin.site.register([Classroom, ClassroomStudents, Rating])