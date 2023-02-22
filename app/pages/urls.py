from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tags/<slug:tag_name>', views.index, name='tag'),
    path('description', views.description, name='description'),
]
