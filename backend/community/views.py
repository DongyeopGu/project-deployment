from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer

@api_view(['GET'])
def index(request):
    articles = Article.objects.order_by('-pk')
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def page_index(request):
    paginator = LimitOffsetPagination()
    paginator.default_limit = 10
    articles = paginator.paginate_queryset(Article.objects.order_by('-pk'), request)
    serializer = ArticleSerializer(articles, many=True)
    return paginator.get_paginated_response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['GET'])
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    data =serializer.data
    if request.user == article.user:
        data['check_user'] = True
    else:
        data['check_user'] = False
    return Response(data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article, data=request.data)
    if request.user.is_staff:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('성공적으로 수정 되었습니다.')
    else:
        if request.user == article.user:
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=article.user)
                return Response('게시글이 수정되었습니다.')
        else:
            return Response('작성자와 다릅니다.')

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user.is_staff:
        article.delete()
        return Response('게시글이 삭제되었습니다.')
    else:
        if request.user == article.user:
            article.delete()
            return Response('게시글이 삭제되었습니다.')
        else:
            return Response('작성자와 다릅니다.')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
        return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def comment_update(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response('댓글이 수정되었습니다.')

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        return Response('댓글이 삭제되었습니다.')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.order_by('-pk')
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

    
