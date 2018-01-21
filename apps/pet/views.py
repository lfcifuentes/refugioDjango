# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from ..pet.forms import PetForm
from ..pet.models import Pet
from django.views.generic import ListView, CreateView


def index(request):

    return render(request, 'pet/index.html')


class PetList(ListView):
    model = Pet
    ordering = ['id']
    template_name = 'pet/pet_list.html'  # si no se pasa el toma esa por defecto XD


def pet_list(request):
    pets = Pet.objects.all().order_by('id')
    context = {'Pets': pets}

    return render(request, 'pet/pet_list.html', context)


class PetCreate(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet/pet_form.html'
    success_url = reverse_lazy('pet:list')


def pet_view(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pet:index')
    else:
        form = PetForm()

    return render(request, 'pet/pet_form.html', {'form': form})


def pet_edit(request, id):
    pet = Pet.objects.get(id=id)

    if request.method == 'GET':
        form = PetForm(instance=pet)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
        return redirect('pet:list')
    return render(request, 'pet/pet_form.html', {'form': form})


def pet_delete(request, id):
    pet = Pet.objects.get(id=id)
    if request.method == 'POST':
        pet.delete()
        return redirect('pet:list')
    return render(request, 'pet/pet_delete.html', {'pet': pet})



