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
from children_app.models import Child
from statistics_app.models import Session
from django.utils import timezone


class TalesList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        tales = Tale.objects.all()
        context = {'items': tales}
        return render(request, 'tale_app/list.html', context)


class TaleStart(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, **kwargs):
        try:
            old_session = Session.objects.get(tale=kwargs['tale_id'], child=kwargs['child_id'])
            first_content_id = old_session.content_id
        except Session.DoesNotExist:
            first_content_id = Content.objects.filter().order_by('order')[0].id
            new_session = Session(tale=Tale.objects.get(
                id=kwargs['tale_id']),
                child=Child.objects.get(id=kwargs['child_id']),
                completed=False,
                date=str(timezone.now()),
                content_id=first_content_id)
            new_session.save()

        kwargs.update({'content_id': first_content_id})
        return HttpResponseRedirect(reverse('tale_app:TaleContent', kwargs=kwargs))


class TaleEnd(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, **kwargs):
        tale = Tale.objects.get(id=kwargs['tale_id'])
        context = {'item': tale}
        return render(request, 'tale_app/tale.html', context)


class TaleContent(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        content = Content.objects.get(id=kwargs['content_id'])
        context = {'item': content}
        return render(request, 'tale_app/tale.html', context)
