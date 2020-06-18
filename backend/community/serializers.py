from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import *



class ArticleSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    user = UserSerializer(required=False)
    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user']

