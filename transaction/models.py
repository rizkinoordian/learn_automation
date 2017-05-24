# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Transaction(models.Model):
    """docstring for transaction."""
    trx_id = models.CharField(max_length=9)
    address_ship = models.CharField(max_length=255)
    date_order = models.DateField()
    seller_name = models.CharField(max_length=255)
    delivery_service = models.CharField(max_length=10)

    def __str__(self):
        return self.trx_id
