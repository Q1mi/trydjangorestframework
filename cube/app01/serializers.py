#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2017/2/27

"""
序列化
"""

from rest_framework import serializers
from . import models


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    company = serializers.StringRelatedField()

    class Meta:
        model = models.Author
        fields = "__all__"


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(many=True)
    publisher = serializers.StringRelatedField()

    class Meta:
        model = models.Book
        fields = "__all__"


class PublisherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Publisher
        fields = "__all__"
