from rest_framework import serializers
from .models import Review, Comment

class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id','review_id','user_id','content','created_at','updated_at','user_name')

class ReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(source='movie.title')
    poster_path = serializers.ReadOnlyField(source='movie.poster_path')
    user_name = serializers.ReadOnlyField(source='user.username')
    comment_set = CommentSerializer(read_only=True, many=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    like_users_count = serializers.IntegerField(source='like_users.count', read_only=True)


    class Meta:
        model = Review
        # fields="__all__"
        fields = (
            'id','title','content','user_id','movie_id', 'created_at','updated_at','movie_title',
            'poster_path','user_name','comment_set','comment_count','like_users_count'
        )
        read_only_fields = ('like_users',)


