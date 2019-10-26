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
from next_prev import next_in_order, prev_in_order
from .forms import ReportPicture
from statistics_app.models import Result
from azure_app.functions import emotion_detction
from statistics_app.views import create_radar


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
            old_session = Session.objects.get(tale=kwargs['tale_id'], child=kwargs['child_id'], completed=False)
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

        try:
            Content.objects.get(id=first_content_id)
        except Content.DoesNotExist:
            first_content_id = Content.objects.filter().order_by('order')[0].id

        kwargs.update({'content_id': first_content_id})
        return HttpResponseRedirect(reverse('tale_app:TaleContent', kwargs=kwargs))


class TaleEnd(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, **kwargs):
        try:
            session = Session.objects.get(tale=kwargs['tale_id'], child=kwargs['child_id'], completed=False)
            session.completed = True
            session.save()
            create_radar(session.id)
        except Session.DoesNotExist:
            pass

        tale = Tale.objects.get(id=kwargs['tale_id'])
        next_content_url = reverse('tale_app:TalesList', kwargs={
            'child_id':kwargs['child_id'],
        })
        context = {'item': tale, 'next_content_url': next_content_url}
        return render(request, 'tale_app/taleend.html', context)


class TaleContent(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        session = Session.objects.get(tale=kwargs['tale_id'], child=kwargs['child_id'], completed=False)
        session.content_id = kwargs['content_id']
        contents = Content.objects.filter(taleid=kwargs['tale_id']).order_by('order')
        curr_content = Content.objects.get(id=kwargs['content_id'])
        next_content = next_in_order(curr_content, qs=contents)
        if next_content is None:
            next_content_url = reverse('tale_app:TaleEnd', kwargs={
                'child_id': kwargs['child_id'],
                'tale_id': kwargs['tale_id'],
            })
        else:
            next_content_url = reverse('tale_app:TaleContent', kwargs={
                'child_id': kwargs['child_id'],
                'tale_id': kwargs['tale_id'],
                'content_id': next_content.id
            })
        content = Content.objects.get(id=kwargs['content_id'])

        if content.type == 0:
            renderhtml = 'tale_app/tale.html'
        else:
            renderhtml = "tale_app/" + str(content.type) + ".html"

        context = {'item': content, 'next_content_url': next_content_url}
        return render(request, renderhtml, context)

    def post(self, request, *args, **kwargs):
        print("POST IN.")
        session = Session.objects.get(tale=kwargs['tale_id'], child=kwargs['child_id'], completed=False)
        content = Content.objects.get(id=kwargs['content_id'])
        try:
            result = Result.objects.get(session=session, content=content)
            result.time = str(timezone.now())
        except Result.DoesNotExist:
            result = Result(
                session=session,
                content=content,
                time=str(timezone.now()),
            )
            result.save()
        endresult = Result.objects.get(session=session,content=content)
        emotion_detction(endresult.id)
        # Redirect response
        session = Session.objects.get(tale=kwargs['tale_id'], child=kwargs['child_id'], completed=False)
        session.content_id = kwargs['content_id']
        contents = Content.objects.filter(taleid=kwargs['tale_id']).order_by('order')
        curr_content = Content.objects.get(id=kwargs['content_id'])
        next_content = next_in_order(curr_content, qs=contents)
        if next_content is None:
            next_content_url = reverse('tale_app:TaleEnd', kwargs={
                'child_id': kwargs['child_id'],
                'tale_id': kwargs['tale_id'],
            })
            return HttpResponseRedirect(next_content_url)
        else:
            kwargs['content_id'] = next_content.id
            return HttpResponseRedirect(reverse('tale_app:TaleContent', kwargs=kwargs))



class TaleUpload(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, **kwargs):
        context ={'form': ReportPicture()}
        return render(request, 'tale_app/upload.html',context)

    def post(self, request, *args, **kwargs):
        form = ReportPicture(request.POST, request.FILES)
        if form.is_valid():
            print("VALID FORM IN.")
            session = Session.objects.get(tale=kwargs['tale_id'], child=kwargs['child_id'], completed=False)
            content = Content.objects.get(id=kwargs['content_id'])
            try:
                result = Result.objects.get(session=session, content=content)
                result.image = form.cleaned_data['image']
                result.time = str(timezone.now())
                result.save()
            except Result.DoesNotExist:
                result = Result(
                    session=session,
                    content=content,
                    time=str(timezone.now()),
                    image=form.cleaned_data['image'],
                )
                result.save()
            endresult = Result.objects.get(session=session,content=content)
            emotion_detction(endresult.id)
            # Redirect response
            session = Session.objects.get(tale=kwargs['tale_id'], child=kwargs['child_id'], completed=False)
            session.content_id = kwargs['content_id']
            contents = Content.objects.filter(taleid=kwargs['tale_id']).order_by('order')
            curr_content = Content.objects.get(id=kwargs['content_id'])
            next_content = next_in_order(curr_content, qs=contents)
            if next_content is None:
                next_content_url = reverse('tale_app:TaleEnd', kwargs={
                    'child_id': kwargs['child_id'],
                    'tale_id': kwargs['tale_id'],
                })
                return HttpResponseRedirect(next_content_url)
            else:
                kwargs['content_id'] = next_content.id
                return HttpResponseRedirect(reverse('tale_app:TaleContent', kwargs=kwargs))

        else:
            print("Problem with FORM IN.")
            return HttpResponseRedirect(reverse('tale_app:TaleUpload', kwargs=kwargs))