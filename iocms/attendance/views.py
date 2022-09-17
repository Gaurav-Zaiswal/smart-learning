from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from users.permissions import IsStudentUser
from .serializers import AttendanceVideoSerializer, DummySerializer


class UploadAttendanceVideo(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        # try:
        # print("_________________________________________________________________")
        # print(request.user.id)
        # print(request.FILES['video'])
        request.data['video'] = request.FILES['video'] 
        serializer = AttendanceVideoSerializer(data = request.data)
        request.data['user'] = request.user.pk   
        # except: 
        #     serializer = AttendanceVideoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class DummyAPI(APIView):
    """
    dummy api to test the uploading of 'library docuemnt with form data'
    """
    def post(self, request):
        request.data['document'] = request.FILES['document']
        serializer = DummySerializer(data=request.data)
        if serializer.is_valid():
            print("____________________ inside dummy view")
            print(serializer.validated_data['document'])
            print(serializer.data)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        