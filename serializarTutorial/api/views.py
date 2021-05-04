import json
from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
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
        json_data = request.body
        stream = io.BytesIO(json_data)
        pdata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pdata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student information added !!'}
            return JsonResponse(res, safe=False)
        return JsonResponse(serializer.errors, safe=False)