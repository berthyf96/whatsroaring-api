from django.db import models


class Organization(models.Model):
    org_name = models.CharField(max_length=100)


class Category(models.Model):
    category = models.CharField(max_length=100)


class Event(models.Model):
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    location = models.CharField(max_length=100)  # Better field type?
    is_free = models.BooleanField()
