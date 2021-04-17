from rest_framework import serializers
from .models import Student

# def start_with_r(value):
#     if value[0].lower() !='r':
#         raise serializers.ValidationError('name should start with R')
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

    # field level validation
    def validate_roll(self, value):
        if value >=200:
            raise serializers.ValidationError('Seat Full')
        return value

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'veeru' and ct.lower() != 'noida':
            raise serializers.ValidationError('city must be noida')
        return data