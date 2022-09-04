from django.shortcuts import render
from django.http import HttpResponse
from msrest import Serializer
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework import status

from classroom.serializers import  RecommendationListSerializer
# from classroom.documents import ClassroomDocument

from .recommed import ComputeRecommendation


class RecomendationView(APIView):
    def get(self, request):
        recommended_classes_dict = ComputeRecommendation.generateRecommendation(request)
        import pdb; pdb.set_trace()
        serializer = RecommendationListSerializer(recommended_classes_dict, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
 