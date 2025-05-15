from django.shortcuts import render
# from django.http import JsonResponse
from student.models import student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
@api_view(['GET'])
def student_view(request):
    if request.method=='GET':
        students=student.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)





# def student_view(request):
#      students=list(student.objects.all().values()) 
#      return JsonResponse(students,safe=False)