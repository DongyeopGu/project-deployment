from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
import random
from django.http import JsonResponse
from accounts.models import User
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user
    serializer = MovieSerializer(movie)
    if movie.like_users.filter(pk=user.pk).exists():
        liked = True
    else:
        liked = False
    data = {
        'liked': liked,
        'data': serializer.data
    }
    return JsonResponse(data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = ReviewSerializer(movie.review_set.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def review_detail(request, movie_id, review_id):
    movie = get_object_or_404(Movie, id=movie_id)
    review = get_object_or_404(Review, id=review_id)
    serializer = ReviewSerializer(review)
    data = serializer.data
    if request.user == review.user:
        data['check_user'] = True
    else:
        data['check_user'] = False
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def review_update(request, movie_id, review_id):
    movie = get_object_or_404(Movie, id=movie_id)
    review = get_object_or_404(Review, id=review_id)
    serializer = ReviewSerializer(review, data=request.data)
    if request.user.is_staff:
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=review.user)
            return Response('성공적으로 수정 되었습니다.')
    else:
        if request.user == review.user:
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=review.user)
                return Response('성공적으로 수정 되었습니다.')
        else:
            return Response('작성자와 다릅니다.')

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def review_delete(request, movie_id, review_id):
    movie = get_object_or_404(Movie, id=movie_id)
    review = get_object_or_404(Review, id=review_id)
    if request.user.is_staff:
        review.delete()
        return Response('성공적으로 삭제 되었습니다.')
    else: 
        if request.user == review.user:
            review.delete()
            return Response('성공적으로 삭제 되었습니다.')
        else:
            return Response('작성자와 다릅니다.')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like(request, movie_id):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer =MovieSerializer(movie)
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        liked = False
    else:
        movie.like_users.add(user)
        liked = True
    data = {
        'liked': liked,
        'count': movie.like_users.count(),
        'movie': serializer.data
    }
    return JsonResponse(data)

@api_view(['GET'])
def random_list(request):
    movies = Movie.objects.order_by('?')[:20]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def voted_list(request):
    movies = Movie.objects.order_by('-vote_count')[:20]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

from .pagination import genre_movie_list
@api_view(['GET'])
def genre_list(request, genre_name):
    paginator = LimitOffsetPagination()
    paginator.default_limit = 20
    genre_id = genre_movie_list(genre_name)
    movies = paginator.paginate_queryset(Movie.objects.filter(genres__in=[genre_id]).order_by('?'),request)
    serializer = MovieSerializer(movies, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def genre_list_all(request, genre_name):
    genre_id = genre_movie_list(genre_name)
    movies = Movie.objects.filter(genres__in=[genre_id])
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_movie(request, search_title):
    if len(search_title) <= 1:
        return Response(False)
    searched = Movie.objects.filter(title__contains=search_title)
    count = len(searched)
    serializer = MovieSerializer(searched, many=True)
    data = { 
        'movies': serializer.data,
        'count': count
    }
    return Response(data)

from .makingjson import tmdb_search, tmdb_toprated
@api_view(['GET'])
def search_movies(request):
    search = request.GET.get('search')
    word = request.GET.get('query')
    page = request.GET.get('page')
    data = tmdb_search(search, word, page)
    print(search)
    return JsonResponse(data)

from datetime import datetime
@api_view(['GET'])
def top_rated_movies(request):
    data = tmdb_toprated()
    for i in range(len(data["results"])):
        try:
            Movie.objects.get(id=data["results"][i].get('id'))
            continue
        except:
            genres_list = data["results"][i].get('genre_ids')
            movie = Movie.objects.create(
                pk = data["results"][i].get('id'),
                # adult = data.get('adult'),
                backdrop_path = data["results"][i].get('backdrop_path'),
                original_title = data["results"][i].get('original_title'),
                original_language = data["results"][i].get('original_language'),
                overview = data["results"][i].get('overview'),
                release_date = data["results"][i].get('release_date'),
                poster_path = data["results"][i].get('poster_path'),
                # popularity = data.get('popularity'),
                title = data["results"][i].get('title'),
                vote_count = data["results"][i].get('vote_count'),
                vote_average = data["results"][i].get('vote_average')
            )
            for i in genres_list:
                movie.genres.add(i)
    return JsonResponse(data)


@api_view(['POST'])
def save_db(request):
    data = request.data
    try:
        Movie.objects.get(id=data.get('id'))
        return Response(False)
    except:
        genres_list = data.get('genre_ids')
        movie = Movie.objects.create(
            pk = data.get('id'),
            # adult = data.get('adult'),
            backdrop_path = data.get('backdrop_path'),
            original_title = data.get('original_title'),
            original_language = data.get('original_language'),
            overview = data.get('overview'),
            release_date = data.get('release_date'),
            poster_path = data.get('poster_path'),
            # popularity = data.get('popularity'),
            title = data.get('title'),
            vote_count = data.get('vote_count'),
            vote_average = data.get('vote_average')
        )
        for i in genres_list:
            movie.genres.add(i)
        return Response(request.data)

@api_view(['GET'])
def recommend_genre(request):
    like_movies = request.user.like_movies.all()
    like_genres = {}
    if like_movies.count() == 0:
        movies = Movie.objects.order_by('?')[0:10]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    for movie in like_movies:
        for genres in movie.genres.all():
            if genres.name in like_genres.keys():
                like_genres[genres.name] += 1
            else:
                like_genres[genres.name] = 1
    most_liked_genres = sorted(like_genres.items(), key=lambda x: x[1], reverse=True)[0]
    most_liked_genre = most_liked_genres[0]
    most_liked_genre_id = Genre.objects.get(name=most_liked_genre)
    genre_matched_movies = Movie.objects.filter(genres=most_liked_genre_id)
    recommend_movies = genre_matched_movies.order_by('-popularity')[0:10]
    serializer = MovieSerializer(recommend_movies, many=True)
    data = {
        'most_liked_genre': most_liked_genres,
        'data': serializer.data
    }
    return Response(data)