from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.views import APIView 
from classroom.serializers import ClassroomDetailSerializer, ClassroomSearchSerializer 
from users.models import Teacher, Student
from users.serializers import TeacherSerializer, StudentSerializer
from feed.models import ClassroomFeed
from .models import Assignment, AssignmentByStudent



class AssignmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        # fields = ['id', "title", "description","class_name", "points", "deadline","teacher", "paper"]
        fields = ['id', "title", "description","class_name", "teacher"]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["teacher"] = TeacherSerializer(instance.teacher).data
        # response['class_name'] = ClassroomDetailSerializer(instance.class_name).data
        response['class_name'] = ClassroomSearchSerializer(instance.class_name).data
        return response
        

class AssignmentListSerializer(serializers.ModelSerializer):
    # details = HyperlinkedIdentityField(lookup_field =  'pk', view_name='assignment:details')
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'creation_date']


class AssignmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
    def to_representation(self, instance):
            response = super().to_representation(instance)
            # response['class_name'] = ClassroomDetailSerializer(instance.class_name).data
            response['class_name'] = ClassroomSearchSerializer(instance.class_name).data
            response["teacher"] = TeacherSerializer(instance.teacher).data
            return response
    

# class AssignmentSubmitSerializer(serializers.ModelSerializer): 
#     # assignment_link = serializers.URLField()

#     class Meta:
#         model = AssignmentByStudent
#         fields = ['student', 'assignment_answer']
        
#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         # response['assignment_details'] = AssignmentDetailSerializer(instance.assignment_details).data
#         response['student'] = StudentSerializer(instance.student).data
#         return response
