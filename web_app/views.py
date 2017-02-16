from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from web_app.models import Category, Item, Comment
from web_app.serializers import CategoryListSerializer, CategorySerializer, ItemListSerializer, ItemSerializer, CommentSerializer
import time


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


@api_view(['GET','POST'])
def comment_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(item.comments.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data.update({
            'item': item.id,
            'addition_date': int(time.time())
        })
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)