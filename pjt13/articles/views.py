from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from django.shortcuts import get_list_or_404, get_object_or_404

# 홈페이지에서 게시글 조회, 게시글 생성
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # DB에 Article 모델에 데이터가 없을 경우 404에러 발생
        articles = get_list_or_404(Article)
        # 직렬화(django data를 json으로)
        # many=True : 객체가 여러 개일 때
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        # 유효성 검사
        # 데이터 제출(생성) 성공 HTTP_201
        # 데이터 제출(생성) 실패 HTTP_400
        # raise_exception=True : 유효성 검사에서 실패했을 때 예외 발생(HTTP_400)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 유효성 검사 실패 했을 때
        # return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

# 단일 게시글 조회, 삭제, 수정
# Restfull API : GET, POST, PUT, DELETE
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    # 삭제
    if request.method == 'DELETE':
        article.delete()
        return Response(status=status. HTTP_204_NO_CONTENT)
    
    # 수정
    if request.method == 'PUT':
        # partial=True : 부분 업데이트 허용(일부 필드만 수정 가능)
        serializer = ArticleSerializer(
            article, data=request.data, partial=True
        )
        # raise_exception=True : 유효성 검사에서 실패했을 때 예외 발생(HTTP_400)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # 유효성 검사 실패 했을 때
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 전체 댓글 조회
@api_view(['GET'])
def comment_list(request):
    # 댓글이 하나도 없으면 404에러
    comments = get_list_or_404(Comment)
    # 직렬화(-> json)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# 단일 댓글 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    # 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    # 삭제
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # 수정
    if request.method == 'PUT':
        # 어차피 수정할 것이 content 밖에 없다.
        serializer = CommentSerializer(comment, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    # 유효성 검사 성공 HTTP_201 / 실패하면 HTTP_400
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    