from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from datetime import datetime

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_superuser', 'is_staff', 'last_login']

    
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")

class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "password", "last_login")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user