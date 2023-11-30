# employees/serializers.py

from rest_framework import serializers
from .models import Employee
from django.core.exceptions import ValidationError
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    
 
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
