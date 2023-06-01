from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Category, Product, Review
from product.serializers import CategorySerializer, ProductSerializer, ReviewSerializer, ProductsReviewsSerializer


@api_view(['GET', 'POST'])
def category_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        data = request.data
        category = Category.objects.create(
            name=data.get('name')
        )
        return Response(data=CategorySerializer(category, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, **kwargs):
    try:
        category = Category.objects.get(id=kwargs['id'])
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! Такой страницы не существует")

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        data = request.data
        category.name = data.get('name')
        category.save()
        return Response(data=CategorySerializer(category).data)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def products_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        data = request.data
        product = Product.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            price=data.get('price'),
            category_id=data.get('category_id')
        )
        return Response(data=ProductSerializer(product, many=False).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, **kwargs):
    try:
        product = Product.objects.get(id=kwargs['id'])
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data="ERROR! Такой страницы не существует")

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        data = request.data
        product.title = data.get('title')
        product.description = data.get('description')
        product.price = data.get('price')
        product.category_id = data.get('category_id')
        product.save()
        return Response(data=ProductSerializer(product).data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reviews_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        data = request.data
        review = Review.objects.create(
            text=data.get('text'),
            product_id=data.get('product_id'),
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
        data = request.data
        review.text = data.get('text')
        review.product_id = data.get('product_id')
        review.stars = data.get('stars')
        review.save()
        return Response(data=ReviewSerializer(review).data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def products_reviews_api_view(request):
    products = Product.objects.all()
    serializer = ProductsReviewsSerializer(products, many=True)
    return Response(data=serializer.data)