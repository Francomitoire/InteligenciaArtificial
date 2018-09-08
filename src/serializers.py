from rest_framework import serializers
from src.models import Classroom

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ('number', 'floor', 'direction', 'feature')

