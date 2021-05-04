from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    roll_no = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)