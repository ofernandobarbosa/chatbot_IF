from rest_framework import viewsets
from app.models import Calendario
from api.serializer import CalendarioSerializer

class CalendariosViewSet(viewsets.ModelViewSet):
    """Todos Eventos"""
    queryset = Calendario.objects.all()
    serializer_class = CalendarioSerializer