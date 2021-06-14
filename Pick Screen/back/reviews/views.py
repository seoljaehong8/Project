
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Review, Comment
from movies.models import Movies
from .serializers import CommentSerializer, ReviewSerializer

# Create your views here.
@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list_create(request):

    if request.method == 'GET':
        try:
            reviews = get_list_or_404(Review)
        except:
            reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        movie_pk = request.data['movie']
        movie = get_object_or_404(Movies, pk=movie_pk)

        serializer = ReviewSerializer(data=request.data)
        # serializer.is_valid()
        # print(serializer.errors)
        

        if serializer.is_valid():
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET','DELETE','PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_detail_delete_update(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'{review_pk}번 글이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
  

@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list_create(request,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    if request.method == 'GET':
        comments = review.comment_set.all()
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save(user=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete_update(request,review_pk,comment_pk):
    if request.method == 'DELETE':
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
        data = {
            'delete' : f'{comment_pk}번 댓글이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def likes(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if review.like_users.filter(pk=request.user.pk).exists():
        #좋아요 취소
        review.like_users.remove(request.user)
        liked = False
    else:
        #좋아요 누름
        review.like_users.add(request.user)
        liked = True
    
    context = {
        'liked' : liked,
        'count' : review.like_users.count(),
    }

    return JsonResponse(context)