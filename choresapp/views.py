# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from choresapp.forms import ChoresForm

from models import Chore, Clean

# Create your views here.

class HomeView(FormView):
    template_name = 'chores_form.html'
    model = Chore
    form_class = ChoresForm

    # def get_context_data(self, **kwargs):
    #
    #     all_cleans= {}
    #     for x in Chore.objects.order_by('chore_name').all():
    #         most_recent_object = Clean.objects.filter(chore_completed__id=x.id).last()
    #         print(x, most_recent_object.id)
    #         marshall_id = most_recent_object.id
    #         all_cleans[most_recent_object.id] = most_recent_object.time
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     context['alldata'] = all_cleans
    #     print('looking at: ', context['alldata'])
    #
    #     return context
