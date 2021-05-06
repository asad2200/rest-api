from django.db import models
from .models import Student
from rest_framework import fields, serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'