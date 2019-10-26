from django.shortcuts import render
from .models import Child
from . import forms
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.models import User


class ChildList(LoginRequiredMixin, TemplateView):
    template_name = "children_app/list.html"

    def get_context_data(self, **kwargs):  # Ez a két sor itt ahhoz kell, hogy hozzáférjük a context-hez
        # amit belerakunka template-be
        context = super().get_context_data(**kwargs)
        all_child = Child.objects.filter(
            user=User.objects.get(pk=self.request.user.id)
        ).order_by('name')
        context['items'] = all_child
        return context


class AddChild(LoginRequiredMixin, TemplateView):
    template_name = 'children_app/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

