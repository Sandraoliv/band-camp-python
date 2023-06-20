from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists."
            )
        ]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="This field must be unique."
            )
        ]
    )

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data) 
    
    def update(self, instance, validated_data):
       
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'full_name', 'artistic_name']
        extra_kwargs = {
            'password': {'write_only': True},
        }

