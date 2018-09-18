# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

from ..adoption.models import Request, Person
from ..adoption.form import RequestForm, PersonForm


def index_adoption(request):
    return HttpResponse("app")


class RequestList(ListView):
    model = Request
    template_name = 'adoption/request_list.html'


class RequestCreate(CreateView):
    model = Request
    template_name = 'adoption/request_form.html'
    form_class = RequestForm
    second_form_class = PersonForm

    success_url = reverse_lazy('adoption:request_list')

    def get_context_data(self, **kwargs):
        context = super(RequestCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            requestO = form.save(commit=False)
            requestO.person = form2.save()
            requestO.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class RequestUpdate(UpdateView):
        model = Request
        second_model = Person
        template_name = 'adoption/request_form.html'
        form_class = RequestForm
        second_form_class = PersonForm

        success_url = reverse_lazy('adoption:request_list')

        def get_context_data(self, **kwargs):
            context = super(RequestUpdate, self).get_context_data(**kwargs)
            pk = self.kwargs.get('pk', 0)
            request_v = self.model.objects.get(id=pk)
            person_v = self.second_model.objects.get(id=request_v.person_id)

            if 'form' not in context:
                context['form'] = self.form_class()
            if 'form2' not in context:
                context['form2'] = self.second_form_class(instance=person_v)
            context['id'] = pk
            return context

class RequestDelete(DeleteView):
    model = Request
    template_name = 'adoption/request_delete.html'
    success_url = reverse_lazy('adoption:request_list')
