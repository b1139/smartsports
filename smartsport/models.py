"""
    Author      : Sathish Kumar(sathishkumarb1139@gmail.com)
    Version     : 1.0
    Description : File contains the Data Base Access Object and Methods
"""

from django.db import models


class Series(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        db_table = 'series'


class Tournament(models.Model):

    id = models.AutoField(primary_key=True)
    series = models.ManyToManyField(Series)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        db_table = 'tournament'
