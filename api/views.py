from django.shortcuts import render
# from django.http import JsonResponse
from student.models import student
from .serializer import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView


@api_view(['GET','POST'])
def student_view(request):
    if request.method=='GET':
        students=student.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method =='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def student_detail_view(request,pk):
    try:
        students=student.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer=StudentSerializer(students)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method== "PUT":
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=="DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )


class Employee(APIView):
    def get(self,request):
        students=Employee.objects.all()
        serializer=EmployeeSerializer(students, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


