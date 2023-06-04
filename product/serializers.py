from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from product.models import Category, Product, Review, Tag


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    product_count = ProductSerializer

    class Meta:
        model = Category
        fields = 'name product_count'.split()
        # fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text product stars'.split()
        # fields = '__all__'


class ProductsReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'title reviews rating'.split()


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField()


class ProductValidateSerializer(serializers.Serializer):
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
