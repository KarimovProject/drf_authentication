from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

# Import the models
from .models import Student, Group
# Import the serializers
from .serializers import StudentSerializer, GroupSerializer

# Create your views here.

@api_view(['GET'])
def get_students(request: Request):
    """
    Get all students
    """
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)
    

