from django.db import models
import datetime


class InstitutionCategory(models.Model):
    name = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = "Categries"

    def __str__(self):
        return self.name


class Field(models.Model):
    name =  models.CharField(max_length = 100)

    def __str__(self):
        return self.name



