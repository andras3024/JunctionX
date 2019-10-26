from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Tale
from .models import Content


class TalesList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        tales = Tale.objects.all()
        context = {'items': tales}
        return render(request, 'tale_app/list.html', context)


class TaleStart(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, **kwargs):
        first_content_id = Content.objects.filter().order_by('order')[0].id
        kwargs.update({'content_id': first_content_id})
        return HttpResponseRedirect(reverse('tale_app:TaleContent', kwargs=kwargs))


class TaleContent(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        content = Content.objects.get(id=kwargs['content_id'])
        context = {'item': content}
        return render(request, 'tale_app/tale.html', context)
