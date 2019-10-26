from django.urls import path
from statistics_app import views

app_name = 'statistics_app'

urlpatterns = [
    # HOMEPAGE
    path('child_<int:child_id>/result', views.ChildResult.as_view(), name="result"),
]