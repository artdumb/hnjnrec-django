from django.db import models

# Create your models here.


class Placedata(models.Model):
    place_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default=None, null=True)


class Picdata(models.Model):
    title = models.CharField(max_length=50)
    cam = models.CharField(max_length=50)
    film = models.CharField(max_length=50, default=None, null=True)
    lens = models.CharField(max_length=50, default=None, null=True)
    descrip = models.CharField(max_length=200, default=None, null=True)
    place_name = models.CharField(max_length=50, default='임시', null=True)
    place_id = models.ForeignKey(Placedata, on_delete=models.CASCADE)
    password = models.CharField(max_length=50, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True)


class Reviewdata(models.Model):
    comment = models.CharField(max_length=50, default=None, null=True)
    pic = models.ForeignKey(Picdata, on_delete=models.CASCADE)
    password = models.CharField(max_length=50, default=None, null=True)


class Password(models.Model):
    password = models.CharField(max_length=50, default=None, null=True)


class record(models.Model):
    views_count = models.IntegerField()
