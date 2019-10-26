from django.urls import path
from tale_app import views

app_name = 'tale_app'

urlpatterns = [
    path('child_<int:child_id>/tales', views.tales, name="tales"),
]