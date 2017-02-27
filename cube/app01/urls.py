#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
# Date: 2017/2/27

"""
REST framework urls
"""

from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'publishers', views.PublisherViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
