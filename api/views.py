import http

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.pagination import DefaultPageNumberPagination
from book.models import Book,Author
from api.serializers import BookSerializer,AuthorSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        query_set = Book.objects.all()
        serializer = BookSerializer(query_set, many=True)
        return Response(serializer.data, http.HTTPStatus.OK)
    elif request.method == "POST":
        book = BookSerializer(data=request.data)
        book.is_valid(raise_exception=True)
        book.save()
        return Response(book.data, http.HTTPStatus.OK)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    if request.method == 'DELETE':
        query_set = Book.objects.get(id=pk)
        query_set.delete()
        return Response("deleted successfully", http.HTTPStatus.OK)
    elif request.method == "PUT":
        query_set = Book.objects.get(id=pk)
        book = BookSerializer(query_set, data=request.data)
        book.is_valid(raise_exception=True)
        book.save()
        return Response(book.data, http.HTTPStatus.OK)


class BookListView(generics.ListAPIView):
    pagination_class = DefaultPageNumberPagination
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookSerializer


class GetBook(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"


class Update_Book(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"


class DeleteBook(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"


class All_Author(ModelViewSet):
    pagination_class = DefaultPageNumberPagination
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    lookup_field = "pk"


