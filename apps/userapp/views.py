# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from ..userapp.forms import registrationForm
# Create your views here.
class CreatedUser(CreateView):
    model = User
    template_name = 'user/create.html'
    form_class = registrationForm
    success_url = reverse_lazy('pet:list')