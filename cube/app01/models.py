from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="书名")
    author = models.ManyToManyField("Author")
    publisher = models.ForeignKey("Publisher")

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="名字")
    company = models.ForeignKey("MC", related_name="authors")

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=32, verbose_name="出版社名")

    def __str__(self):
        return self.name


class MC(models.Model):
    name = models.CharField(max_length=32, verbose_name="经纪公司")
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = "经纪公司"
        verbose_name_plural = verbose_name

