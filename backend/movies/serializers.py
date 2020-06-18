from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        queryset=True,
        slug_field= 'name',
     )
    like_users = serializers.SlugRelatedField(
        many=True,
        queryset=True,
        slug_field='username'
    )
    class Meta:
        model = Movie
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%Sd")
    updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    user = UserSerializer(required=False)
    class Meta:
        model = Review
        fields = ['id', 'title', 'content', 'rank', 'user', 'created_at', 'updated_at', 'movie_id']
