from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from . import models
from . import serializers


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
