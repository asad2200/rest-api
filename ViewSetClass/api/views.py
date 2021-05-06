from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import serializers, viewsets

# Create your views here.


class StudentAPI(viewsets.ViewSet):
    def list(self, request):
        studs = Student.objects.all()
        serializer = StudentSerializer(studs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Added!!'})
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        stud = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stud)
        return Response(serializer.data)

    def update(self, request, pk):
        stud = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated!!'})
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        stud = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated!!'})
        return Response(serializer.errors)

    def destroy(self, request, pk):
        stud = Student.objects.get(pk=pk)
        stud.delete()
        return Response({'msg': 'Data Deleted!!'})
