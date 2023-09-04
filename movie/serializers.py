from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from movie.models import Director, Review, Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    movie_count = MovieSerializer(read_only=True, many=1)

    class Meta:
        model = Director
        fields = 'name movie_count'.split()
        # fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movie stars'.split()
        # fields = '__all__'


class MovieReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'title reviews rating'.split()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField()


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    category_id = serializers.ListField(child=serializers.IntegerField())
    tag = serializers.ListField(child=serializers.IntegerField(min_value=1))

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category not found!')
        return category_id

    def validate_tag(self, tag):
        tags_db = Tag.objects.filter(id__in=tag)
        if len(tags_db) != len(tag):
            raise ValidationError('Tag not found')
        return tag


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    product_id = serializers.IntegerField()
    stars = serializers.IntegerField()

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError(f'Product with id ({product_id}) not found')
        return product_id
