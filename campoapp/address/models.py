from django.db import models
from person.models import Client


class State(models.Model):
    name = models.CharField(max_length=140)
    short_name = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class Municipality(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class Location(models.Model):
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name + " / " + self.municipality.name + " / " + self.municipality.state.short_name


class Address(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    street = models.CharField(max_length=140)
    zip_code = models.CharField(max_length=20,null=True, blank=True)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True, blank=True)
    lat = models.DecimalField(max_digits = 15, decimal_places=8, null=True, blank=True)
    lon = models.DecimalField(max_digits = 15, decimal_places=8, null=True, blank=True)

    def __str__(self):
        return self.name
