from rest_framework import serializers
from .models import Album
from users.serializers import UserSerializer


class AlbumSerializer(serializers.ModelSerializer):
 
    user = UserSerializer(required=False)
   
    class Meta:
        model = Album
        fields = ['id', 'name', 'year', 'user']
         

      