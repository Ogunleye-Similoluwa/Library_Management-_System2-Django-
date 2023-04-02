from rest_framework import serializers
from book.models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(queryset=Author.objects.all(), view_name="All_Author", lookup_field="pk")

    class Meta:
        model = Book
        fields = ['title', 'description', 'genre', 'language', 'price', 'author', 'date_added']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
