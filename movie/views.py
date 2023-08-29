from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie.models import Movie, Director, Review
from movie.serializers import (DirectorSerializer, MovieSerializer, ReviewSerializer, ReviewValidateSerializer,
                               DirectorValidateSerializer, MovieValidateSerializer, MovieReviewsSerializer)


@api_view(['GET', 'POST'])
def director_api_view(request):
    if request.method == 'GET':
        categories = Director.objects.all()
        serializer = DirectorSerializer(categories, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        data = serializer.validated_data
        director = Director.objects.create(
            name=data.get('name')
        )
        return Response(data=DirectorSerializer(director, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, **kwargs):
    try:
        director = Director.objects.get(id=kwargs['id'])
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! Такой страницы не существует")

    if request.method == 'GET':
        serializer = DirectorSerializer(director)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        data = serializer.validated_data
        director.name = data.get('name')
        director.save()
        return Response(data=DirectorSerializer(director).data)

    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movies_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        data = serializer.validated_data
        movie = Movie.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            price=data.get('price'),
            director_id=data.get('director_id'),
            tag=data.get('tag')
        )
        return Response(data=MovieSerializer(movie, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, **kwargs):
    try:
        movie = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! Такой страницы не существует")

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        data = serializer.validated_data
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.price = data.get('price')
        movie.director_id = data.get('director_id')
        movie.tag = data.get('tag')
        movie.save()
        return Response(data=MovieSerializer(movie).data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reviews_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        data = serializer.validated_data
        review = Review.objects.create(
            text=data.get('text'),
            movie_id=data.get('movie_id'),
            stars=data.get('stars')
        )
        return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, **kwargs):
    try:
        review = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! Такой страницы не существует")

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        data = serializer.validated_data
        review.text = data.get('text')
        review.movie_id = data.get('movie_id')
        review.stars = data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movies_reviews_api_view(request):
    movies = Movie.objects.all()
    serializer = MovieReviewsSerializer(movies, many=True)
    return Response(data=serializer.data)
