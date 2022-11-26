from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


# Import the models
from .models import Student, Group
# Import the serializers
from .serializers import StudentSerializer, GroupSerializer

# Create your views here.


class StudentView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request: Request):
        """
        Get all students
        """
    

        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        """
        Create a new student
        """
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid data'})

    

