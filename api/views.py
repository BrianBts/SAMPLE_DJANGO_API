from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import Programmer
# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet): #CON ESTO YA TENEMOS LAS VISTAS NECESITARIAS PARA REALIZAR LAS ACCIONES DE ESTA ENTIDAD
    queryset=Programmer.objects.all()
    serializer_class=ProgrammerSerializer

