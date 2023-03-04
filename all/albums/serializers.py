from rest_framework import serializers
from rest_framework.validators import ValidationError,UniqueValidator
from .models import *



class AlbumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Album
        fields = '__all__'
