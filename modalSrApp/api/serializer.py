from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Student


# validators
def capital(value):
    if value[0].upper() != value[0]:
        raise serializers.ValidationError(
            'Name Should be start with capital letter')


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[capital])

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['id']

    # field level validation
    def validate_roll_no(self, value):
        if value >= 50:
            raise serializers.ValidationError("Seats are full !!")
        return value

    # object level validation
    def validate(self, data):
        ct = data.get("city")
        if ct.lower() != 'basu':
            raise serializers.ValidationError(
                'student must be belongs to basu')
        return data