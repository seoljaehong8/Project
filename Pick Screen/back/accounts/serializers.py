from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.serializers import MovieSerializer, RatingSerializer
from reviews.serializers import ReviewSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    review_set = ReviewSerializer(read_only=True, many=True)
    review_count = serializers.IntegerField(source="review_set.count", read_only=True)

    like_movies = MovieSerializer(read_only=True, many=True)
    like_movies_count = serializers.IntegerField(source="like_movies.count", read_only=True)

    rating_set = RatingSerializer(read_only=True, many=True)
    rating_count = serializers.IntegerField(source='rating_set.count', read_only=True)

    class Meta:
        model = User
        fields = (
            'username', 'password','like_movies','like_movies_count',
            'review_set','review_count','rating_set','rating_count', 'is_superuser',
            )
