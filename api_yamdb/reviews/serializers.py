from rest_framework import serializers
from django.db.models import Avg

from .models import *
from authentication.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitlesSerializerForCreate(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Genre.objects.all(),
        many=True,
        required=False
    )
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all(),
    )

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')


class TitlesSerializerForRead(serializers.ModelSerializer):
    genre = GenresSerializer(many=True)
    rating = serializers.SerializerMethodField()
    category = CategorySerializer()

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating', 'description',
                  'genre', 'category')
        read_only_fields = ('id', 'rating')

    def get_rating(self, obj):
        title = Title.objects.get(id=obj.id)
        # обратимся через related_name модели Title
        # к связонной с ней моделью Review и вызвоем агрегирующую функцию
        # c параметром вычесления среднего арефметического
        awg_score_on_title = title.reviews.aggregate(Avg('score'))
        return awg_score_on_title.get('score__avg')


class ReviewsSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(max_value=10, min_value=1)
    title = serializers.HiddenField(default=None)
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    
    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date', 'title')
        read_only_fields = ('id', 'author', 'pub_date', 'title')


class CommentsSerializer(serializers.ModelSerializer):
    review = serializers.HiddenField(default=None)
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comments
        fields = '__all__'
        read_only_fields = ('id', 'author', 'created', 'review')
