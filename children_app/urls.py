from django.urls import path

from children_app import views

app_name = 'children_app'

urlpatterns = [
    # HOMEPAGE
    path('', views.ChildList.as_view(), name="child"),
    path('child/add', views.AddChild.as_view(), name="add_child"),
]