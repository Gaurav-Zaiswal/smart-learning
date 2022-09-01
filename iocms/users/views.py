from django.http import Http404

from rest_framework import permissions
from rest_framework import mixins, viewsets
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin

from .permissions import IsStudentUser

from .models import AttendenceImage, Student, Teacher, User
from .serializers import AttendencePicturesSerializer, PicturesSerializer, ProfileSerializer, StudentRegistrationSerializer, TeacherRegistrationSerializer, UserSerializer, VideoSerializer



class CreateStudentView(generics.CreateAPIView,
                        viewsets.GenericViewSet):

    model = Student
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentRegistrationSerializer


class CreateTeacherView(generics.CreateAPIView,
                        viewsets.GenericViewSet):

    model = Teacher
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TeacherRegistrationSerializer


class UserView(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated, 
    ]
    model = User 

    serializer_class = UserSerializer 

    def get_object(self):
        return self.request.user



class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=204)


class UploadImage(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        # request.data['student'] = request.user.id 
        # assignment_file = request.FILES['file']
        # print("_______________________________________________________________") 
        # print(request.FILES)
        try:
            request.data['image'] = request.FILES['image'] 
            serializer = ProfileSerializer(data = request.data)
        except: 
            serializer = ProfileSerializer(data = request.data)
 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class UploadImages(APIView):
    permission_classes = [IsStudentUser]

    def post(self, request):
        request.data['image'] = request.FILES['image']
        # request.data['user'] = User.objects.get(pk=request.user.id)
        serializer = PicturesSerializer(data = request.data)
        request.data['user'] = request.user.id       
        # import pdb; pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class UploadAttendanceImageViewset(APIView):
    permission_classes = [IsStudentUser]

    def post(self, request):
        request.data['image'] = request.FILES['image']
        # request.data['user'] = User.objects.get(pk=request.user.id)
        serializer = AttendencePicturesSerializer(data = request.data)
        request.data['user'] = request.user.id       
        # import pdb; pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# class UploadAttendanceImageViewset(ModelViewSet):
#     queryset = AttendenceImage.objects.all()
#     serializer_class = AttendencePicturesSerializer
#     permission_classes = [IsStudentUser]
#     # filter_fields = ("user", "image")

    # update_data_pk_field = 'id'

    # def create(self, request, *args, **kwargs):
    #     import pdb; pdb.set_trace()
    #     kwarg_field: str = self.lookup_url_kwarg or self.lookup_field
    #     # self.kwargs[kwarg_field] = request.data['self.update_data_pk_field']
    #     self.kwargs[kwarg_field] = request.data['id']

    #     try:
    #         return self.update(request, *args, **kwargs)
    #     except Http404:
    #         return super().create(request, *args, **kwargs)



class RegisterVideoView(APIView):
    # authentication_classes = [IsAuthenticated]
    permission_classes = [IsStudentUser]
    def post(self, request):
        # import pdb; pdb.set_trace()

        request.data['video'] = request.FILES['video']
        # request.data['user'] = User.objects.get(pk=request.user.id)
        serializer = VideoSerializer(data = request.data)
        request.data['user'] = request.user.id       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)