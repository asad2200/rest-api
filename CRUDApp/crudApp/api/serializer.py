from rest_framework import serializers
from .models import Student


# validators
def capital(value):
    if value[0].upper() != value[0]:
        raise serializers.ValidationError(
            'Name Should be start with capital letter')


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, validators=[capital])
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # field level validation
    def validate_roll_no(self, value):
        if value >= 50:
            raise serializers.ValidationError("Seats are full !!")
        return value

    # object level validation
    def validate(self, data):
        ct = data.get("city")
        if ct.lower() != 'basu':
            raise serializers.ValidationError('student must be belongs to basu')
        return data