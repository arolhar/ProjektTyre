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