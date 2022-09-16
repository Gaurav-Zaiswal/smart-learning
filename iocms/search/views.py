from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from msrest import Serializer
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework import status

from classroom.serializers import  RecommendationListSerializer, ClassroomListSerializer
from classroom.models import Classroom
# from classroom.documents import ClassroomDocument

from .recommed import ComputeRecommendation


class RecomendationView(APIView):
    def get(self, request):
        class_ids = []
        recommended_classes = ComputeRecommendation.generateRecommendation(request) # list of dits
        # print(recommended_classes)
        for classroom in recommended_classes:
            class_ids.append(classroom['classroom_id'])
        # import pdb; pdb.set_trace()
        # filtered_classes = Classroom.objects.filter(id__in=class_ids)
        # user = request.user
        filtered_classes = Classroom.objects.filter(id__in=class_ids)
        # f = filtered_classes.exclude(user__in=Classroom.classoom_relation.enrolled_student_id)
        # filtered_classes = Classroom.objects.filter(id__in=class_ids).exclude(user__in=classoom_relation__enrolled_students_id)
        
        # serializer = RecommendationListSerializer(filtered_classes, many=True)
        serializer = ClassroomListSerializer(filtered_classes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
 