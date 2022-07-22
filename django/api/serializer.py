from dataclasses import fields
from rest_framework import serializers
from app.models import Calendario

class CalendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendario
        fields = '__all__'