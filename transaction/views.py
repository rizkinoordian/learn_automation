# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Transaction


# view for index
def index(request, trans_id):
    trans = get_object_or_404(Transaction, pk=trans_id)
    return render(request, 'transaction/index.html', {'transaction': trans})
