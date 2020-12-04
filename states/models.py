from django.db import models
from django.utils import timezone


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class State(models.Model):
    state = models.CharField(max_length=50)
    city = models.ManyToManyField(City, blank=True)

    def __str__(self):
        return self.state


class Customer(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    state = models.ForeignKey(
        State, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
