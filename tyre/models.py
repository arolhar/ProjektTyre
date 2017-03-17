from django.db import models
from django.utils import timezone


class Symbol(models.Model):
    symbol = models.CharField(max_length=50, verbose_name="Symbol")
    description = models.TextField(verbose_name="Opis")
    created_date = models.DateTimeField(
            default=timezone.now, verbose_name="Data dodania")

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.symbol
    
    class Meta:
        verbose_name = 'Dodatkowe oznaczenie'
        verbose_name_plural = 'Dodatkowe oznaczenia'
    
class Capacity(models.Model):
    symbol = models.CharField(max_length=10, verbose_name="Symbol")
    capacity = models.CharField(max_length=10, verbose_name="Maksymalna nośność [kg]")
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.symbol
    
    class Meta:
        verbose_name = 'Indeks nośności'
        verbose_name_plural = 'Indeksy nośności'
    
class Speed(models.Model):
    symbol = models.CharField(max_length=10, verbose_name="Symbol")
    speed = models.CharField(max_length=10, verbose_name="Maksymalna prędkość [km/h]")
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.symbol
    
    class Meta:
        verbose_name = 'Indeks prędkości'
        verbose_name_plural = 'Indeksy prędkości'
    
class Label(models.Model):
    symbol = models.CharField(max_length=5, verbose_name="Symbol")
    rollingResistance = models.CharField(max_length=100, verbose_name="Opory toczenia [kg/t]")
    wetGrip = models.CharField(max_length=100, verbose_name="Przyczepność na mokrej nawierzchni [%]")
    externalNoise = models.TextField(verbose_name="Hałas zewnętrzny")

    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.symbol
    
    class Meta:
        verbose_name = 'Etykieta opony'
        verbose_name_plural = 'Etykiety opon'
    
class Companies(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nazwa")
    headquarters = models.CharField(max_length=200, verbose_name="Siedziba")
    brands = models.TextField(verbose_name="Produkowane marki")
    factory = models.TextField(verbose_name="Fabryki")

    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Koncern'
        verbose_name_plural = 'Koncerny'