from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    exclude = ()


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
    exclude = ()


@admin.register(models.MC)
class MCAdmin(admin.ModelAdmin):
    exclude = ()
