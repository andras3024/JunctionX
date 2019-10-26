from django.shortcuts import render
from . import forms
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView


class ChildList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    template_name = "tale_app/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
