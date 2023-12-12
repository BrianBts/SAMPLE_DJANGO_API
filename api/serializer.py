#CONVERTIR MODELO PROGRAMMER A JSON

from rest_framework import serializers
from .models import Programmer

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Programmer
        #fields=('fullname', 'nickName') #Si quiero unos campos en particular
        fields= '__all__' #Indico que quiero todos los campos del modelo, incluso su ID predeterminado
