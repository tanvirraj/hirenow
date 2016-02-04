from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=200, null=True, blank=True)
    updated_by = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        abstract = True
