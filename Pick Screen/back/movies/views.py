from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http.response import JsonResponse

import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from . models import Movies, Rating
from .serializers import MovieSerializer, RatingSerializer

# Create your views here.
# 데이터베이스에 영화 정보 저장하기
def make_movieData(request):

    page = 0

    genre_dict = {28: '액션', 12: '어드벤처', 16: '애니메이션', 35: '코디미', 80: '범죄', 99: '다큐멘터리', 18: '드라마', 
        10751: '가족', 14: '판타지', 36: '역사', 27: '공포', 10402: '음악', 9648: '미스테리', 10749: '로맨스', 
        878: 'SF', 10770: 'TV 영화', 53: '스릴러', 10752: '전쟁', 37: '서부'
    }

    # while page <= 499:
    while page <= 50:
        print(page)
        page += 1
        url = f'https://api.themoviedb.org/3/movie/popular?api_key=6b3db2093be8e14d01eccd56d390ec42&language=ko&page={page}'
        response = requests.get(url)
        datas = response.json()
        datas = datas['results']
        
        for data in datas:
            overview = data['overview']
            
            if overview == '':
                continue
            title = data['title']
            number = data['id']
            genre = data['genre_ids']

            genre_list = ''
            for idx in range(len(genre)):
                genre_list += genre_dict[genre[idx]]
                if idx != len(genre)-1:
                    genre_list += ','

            poster_path = data['poster_path']
            release_date = data['release_date']
            vote_average = data['vote_average']
            vote_count = data['vote_count']
            popularity = data['popularity']
            vote_score = int(vote_average * vote_count)
    
            movie = Movies(title=title,genre=genre_list,overview=overview,
                poster_path=poster_path,release_date=release_date,vote_average=vote_average,
                vote_count=vote_count,popularity=popularity,vote_score=vote_score)
            movie.save()  

            # overview = data['overview']

            # if overview[0] == '':
            #     continue
            # title = data['title']
            # number = data['id']
            # genre = data['genre_ids']

            # genre_list = []
            # for g in genre[0]:
            #     genre_list.append(genre_dict[g])

            # poster_path = data['poster_path']
            # release_date = data['release_date']
            # vote_average = data['vote_average']
            # vote_count = data['vote_count']
            # popularity = data['popularity']
    
            # movie = Movies(number=number[0],title=title[0],genre=genre_list,overview=overview[0],
            #     poster_path=poster_path[0],release_date=release_date[0],vote_average=vote_average[0],
            #     vote_count=vote_count[0],popularity=popularity[0])
            # movie.save()   



    return render(request,'list.html')


@api_view(['GET'])
def make_dumpData(request, movie_pk):

    movies = get_list_or_404(Movies)
    serializer = MovieSerializer(movies,many=True)


    with open('movies.json','w',encoding='utf-8') as make_file:
        json.dump(serializer.data ,make_file, ensure_ascii=False, indent='\t')

    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movies)
        serializer = MovieSerializer(movies,many=True)

        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_detail(request,movie_pk):
    movie = get_object_or_404(Movies, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_rating(request,movie_rating_pk):
    if request.method == 'POST':       
        movie = get_object_or_404(Movies,pk=movie_rating_pk)
        serializer = RatingSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            print(serializer)
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        rating = get_object_or_404(Rating,pk=movie_rating_pk)
        rating.delete()
        data = {
            'delete': f'{movie_rating_pk}번 평이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def likes(request, movie_pk):
    movie = get_object_or_404(Movies, pk=movie_pk)

    if movie.like_users.filter(pk=request.user.pk).exists():
        #좋아요 취소
        movie.like_users.remove(request.user)
        liked = False
    else:
        #좋아요 누름
        movie.like_users.add(request.user)
        liked = True
    
    context = {
        'liked' : liked,
        'count' : movie.like_users.count(),
    }

    return JsonResponse(context)

