from django.db import models
from django.utils import timezone


class Symbol(models.Model):
    symbol = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.symbol
    
class Capacity(models.Model):
    symbol = models.CharField(max_length=10)
    capacity = models.CharField(max_length=10)
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.symbol
    
class Speed(models.Model):
    symbol = models.CharField(max_length=10)
    speed = models.CharField(max_length=10)
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.symbol
    
class Label(models.Model):
    symbol = models.CharField(max_length=5)
    rollingResistance = models.CharField(max_length=100)
    wetGrip = models.CharField(max_length=100)
    externalNoise = models.TextField()

    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.symbol
    
class Companies(models.Model):
    name = models.CharField(max_length=200)
    headquarters = models.CharField(max_length=200)
    brands = models.TextField()
    factory = models.TextField()

    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name