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
            # This method is called when valid form data has been POSTed.
            # It should return an HttpResponse.
            # form.send_email()
            if form.is_valid():
                print("Yes, the form was valid!")
                print(repr(form.cleaned_data['chores']))
                chore_submitted = Chore.objects.get(id=form.cleaned_data['chores'])
                boyfriend_submitting = Boyfriend.objects.get(id=1)
                c = Clean.objects.create(chore_completed=chore_submitted, cleaner=boyfriend_submitting)
                c.save()
            # chore_completed = Chore.objects.filter(id=form.cleaned_data['chores'])
            # print('chore is: ', chore_completed )
            # print(" ^^^^A FORM HAS BEEN SUBMITTED SUCCESSFULLY")
                # submitted_clean = Clean(chore_completed = 3)
                # submitted_clean.save()
                return super(HomeView, self).form_valid(form)



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
