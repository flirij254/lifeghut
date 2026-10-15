from django.db import models

class Employees(models.Model):
    name = models.CharField(max_lenght=100, null=False)
    surname = models.CharField(max_lenght=100, null=False)
    patronymic = models.CharField(max_lenght=120, null=True)
    age = models.IntegerField()
    date_of_birth = models.DateField(null=False)
    salary = models.FloatField(null=False)
