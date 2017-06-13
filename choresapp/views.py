# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from choresapp.forms import ChoresForm

from models import Chore, Clean, Boyfriend

# Create your views here.

class HomeView(FormView):
    template_name = 'chores_form.html'
    model = Chore
    form_class = ChoresForm
    success_url = '/clean_submission/'

    def form_valid(self, form):
        if form.is_valid():
            chore_submitted = Chore.objects.get(id=form.cleaned_data['chores'])
            boyfriend_submitting = Boyfriend.objects.get(id=1)
            c = Clean.objects.create(chore_completed=chore_submitted, cleaner=boyfriend_submitting)
            c.save()
            return super(HomeView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        list_all_chores = Chore.objects.values('id').all()
        most_recent_chores = {}
        for z in list_all_chores:
            retrieved_chore = Clean.objects.filter(chore_completed=z['id']).latest('time')
            print('z: ', z['id'], retrieved_chore.chore_completed.chore_name)
            most_recent_chores[z['id']] = retrieved_chore
        context['pagetitle'] = 'My special Title'
        context['most_recent_chores'] = most_recent_chores
        return context
