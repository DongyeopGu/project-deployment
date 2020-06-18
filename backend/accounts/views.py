from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import CreateUserSerializer, UserSerializer, LoginUserSerializer
from community.serializers import ArticleSerializer
from movies.serializers import ReviewSerializer, MovieSerializer
from movies.models import Movie
from rest_framework import viewsets, permissions, generics, status
from knox.models import AuthToken
from datetime import datetime
# Create your views here.

@api_view(['GET'])
def profile(request, user_name):
    User = get_user_model()
    user = get_object_or_404(User, username=user_name)
    serializer = UserSerializer(user)
    data = serializer.data
    movies_serializer = MovieSerializer(user.like_movies.all(),many=True)
    article_serializer = ArticleSerializer(user.article_set.all(), many=True)
    review_serializer = ReviewSerializer(user.review_set.all(), many=True)
    data['articles'] = article_serializer.data
    data['reviews'] = review_serializer.data
    data['movies'] = movies_serializer.data
    data['n_article'] = user.article_set.count()
    data['n_review'] = user.review_set.count()
    data['n_movies'] = user.like_movies.count()
    return Response(data)

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        body = {}
        try:    
            User.objects.get(username=request.data["username"])
        except: # ID 없음
            body["error"] = {
                "username": "아이디 정보가 없습니다."
                }
            return Response(body)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            update_last_login(None, user)       #최근 로그인 시간 저장    
            u_last_login = user.last_login
            up_last_login = u_last_login.strftime('%Y-%m-%d %H:%M:%S')
            user.last_login = up_last_login
            return Response(
                {
                    "user": UserSerializer(
                        user, context=self.get_serializer_context()
                    ).data,
                    "token": AuthToken.objects.create(user)[1],
                }
            )
        else:
            body["error"] = { "password" : "비밀번호가 일치하지 않습니다." }
            return Response(body)


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        body = {}
        try:    # 이미 가입된 ID인지 확인
            User.objects.get(username=request.data["username"])
            body["error"] = {
                        "username": "해당 아이디는 이미 존재합니다."
                    }
            return Response(body)
        except: # 아이디 & 비밀번호 제한조건 확인
            if len(request.data["username"]) < 6:
                body["error"] = {
                        "username": "아이디는 6자리 이상이어야 합니다."
                    }
                return Response(body)
            if len(request.data["password"]) < 8:
                body["error"] = { "password" : "비밀번호는 8자리 이상이어야 합니다." }
                return Response(body)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        update_last_login(None, user)       #최근 로그인 시간 저장    
        u_last_login = user.last_login
        up_last_login = u_last_login.strftime('%Y-%m-%d %H:%M:%S')
        user.last_login = up_last_login
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

class UserList(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        serializer = self.get_serializer(user, many=True)
        return Response(serializer.data)
    
    def put(self, request, user_name, **kwargs):
        user = User.objects.get(username=user_name)
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data)

    def delete(self, request, user_name, **kwargs):
        user = User.objects.get(username=user_name)
        user.delete()
        return Response('성공적으로 삭제 되었습니다.')




# @api_view(['POST'])
# def user_perm_change(request):
