from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    data = CategorySerializer(categories, many=True)
    return Response(data.data)


@api_view(['GET'])
def category_detail(request, **kwargs):
    category = Category.objects.get(id=kwargs['id'])
    data = CategorySerializer(category, many=False).data
    return Response(data=data)


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True)
    return Response(data.data)


@api_view(['GET'])
def product_detail(request, **kwargs):
    product = Product.objects.get(id=kwargs['id'])
    data = ProductSerializer(product, many=False).data
    return Response(data=data)


@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True)
    return Response(data.data)


@api_view(['GET'])
def review_detail(request, **kwargs):
    review = Review.objects.get(id=kwargs['id'])
    data = ReviewSerializer(review, many=False).data
    return Response(data=data)
