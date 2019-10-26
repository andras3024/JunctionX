from django.shortcuts import render
from .models import Result
from children_app.models import Child
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class ChildResult(LoginRequiredMixin, TemplateView):
    template_name = "statistics_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_result = Result.objects.filter(
            child=Child.objects.get(pk=kwargs['child_id'])
        ).order_by('time')
        context['items'] = all_result
        return context
