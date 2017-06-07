# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from models import Chore

# Create your views here.

class HomeView(ListView):
    model = Chore
