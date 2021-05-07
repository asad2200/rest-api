from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def student(request, id=None):
    if id is not None:
        try:
            stud = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'msg': 'Student not found'})

    if request.method == 'GET':
        if id is not None:
            serializer = StudentSerializer(stud)
            return Response(serializer.data)
        studs = Student.objects.all()
        serializer = StudentSerializer(studs, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Added!!'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        serializer = StudentSerializer(stud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data is updated !!'})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        serializer = StudentSerializer(stud, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial data is updated !!'})
        return Response(serializer.errors)

    if request.method == 'DELETE':

        stud.delete()
        return Response({'msg': 'Data Deleted !!'})