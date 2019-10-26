from django.urls import path
from tale_app import views

app_name = 'tale_app'

urlpatterns = [
    path('tales', views.TalesList.as_view(), name="TalesListTest"),
    path('tales_<int:tale_id>/start', views.TaleStart.as_view(), name="TaleStartTest"),
    path('tales_<int:tale_id>/content_<int:content_id>', views.TaleContent.as_view(),name="TaleContentTest"),

    path('child_<int:child_id>/tales', views.TalesList.as_view(), name="TalesList"),
    path('child_<int:child_id>/tales_<int:tale_id>/start', views.TaleStart.as_view(), name="TaleStart"),
    path('child_<int:child_id>/tales_<int:tale_id>/content_<int:content_id>', views.TaleContent.as_view(), name="TaleContent"),
]