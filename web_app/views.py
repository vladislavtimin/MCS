from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from web_app.models import Category, Item
from web_app.serializers import CategoryListSerializer, CategorySerializer, ItemListSerializer, ItemSerializer


@api_view(['GET'])
def categories_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        print(serializer.data['items'])
        return Response(serializer.data['items'])


@api_view(['GET'])
def items_list(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemListSerializer(items, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def item_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)
