# from dataclasses import field
# from msilib.schema import Class
# from pyexpat import model
from .models import AttendenceImage, Images, Profile, User, RegisterVideo

from rest_framework import serializers
from rest_framework.validators import UniqueValidator  # makes sure email, username are unique

from .models import Student, Teacher


class StudentRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    email = serializers.EmailField(
        max_length=150
    )
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(
        min_length=8,
        style={'input_type': 'password'},
        write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            is_student = True
        )
        password = self.validated_data['password']
        user.set_password(password)
        #
        user.save()
        #
        student = Student(user=user)
        student.save()

        return user


class TeacherRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    email = serializers.EmailField(
        max_length=150
    )
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(
        min_length=8,
        style={'input_type': 'password'},
        write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            is_teacher=True
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        teacher = Teacher(user=user)
        teacher.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'is_teacher', 'is_student']


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher 
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["user"] = UserSerializer(instance.user).data
        return response 

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student 
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["user"] = UserSerializer(instance.user).data
        return response 


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image']


class PicturesSerializer(serializers.ModelSerializer):
    """
    foreign key does not require any special treatment. however its represnetation does.
    for example, if to_representation is not used,
    response will be:
    {
    "id": 10,
    "image": "https://aithonimages.blob.core.windows.net/media/author_pictures/7c3c.jpg",
    "user": 1
    }

    but if you want to include all the details of user as will, then use to_representation as well.
    {
        "id": 10,
        "image": "https://aithonimages.blob.core.windows.net/media/author_pictures/7c3c.jpg",
        "user": {
            "first name":
            ...
        }
    }

    here, we are fetching `user` details from `images`, but if you want to fetch `images' from 'user'
    then `RelatedField` is used.

    learn about `depth` artibute inside `Meta`
    """
    class Meta:
        model = Images
        fields = '__all__'
        # depth = 1 


class AttendencePicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendenceImage
        fields = '__all__'
        # depth = 1 
    
    def create(self, validated_data):
        image, created = AttendenceImage.objects.update_or_create(
            user=validated_data.get('user', None),
            defaults={'image': validated_data.get('image', None)})
        return image


class VideoSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = RegisterVideo
        fields = ['user', 'video']
