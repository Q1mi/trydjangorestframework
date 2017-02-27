from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name=u"书名")
    author = models.ManyToManyField("Author")
    publisher = models.ForeignKey("Publisher")

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name=u"名字")

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=32, verbose_name=u"出版社名")

    def __str__(self):
        return self.name



