from functools import partial
from django.http import HttpResponse, JsonResponse
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from rest_framework import parsers
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


# Create your views here.
def students_all(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    json_data = JSONRenderer().render(data=serializer.data)
    return HttpResponse(json_data, content_type='application/json')


def student_info(request, id):
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student)
    json_data = JSONRenderer().render(data=serializer.data)
    return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        parsed_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student data added!!'}
            return JsonResponse(res)
        json_data = JSONRenderer().render(data=serializer.errors)
        return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def student_update(request):
    if request.method == 'PUT':
        data = request.body
        stream = io.BytesIO(data)
        parsed_data = JSONParser().parse(stream)
        id = parsed_data.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=parsed_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student data updated !!'}
            return JsonResponse(res)
        json_data = JSONRenderer().render(data=serializer.errors)
        return HttpResponse(json_data, content_type='application/jsons')


@csrf_exempt
def student_delete(request, id):
    if request.method == 'DELETE':
        Student.objects.get(id=id).delete()
        res = {'msg': 'Student data deleted'}
        return JsonResponse(res)
