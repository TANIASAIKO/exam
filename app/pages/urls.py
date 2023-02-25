from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='profile'),
    path('cards/<slug:suit>/', views.cards, name='cards'),
    path('cards/<slug:suit>/<slug:rank>/', views.cards, name='card'),
    path('init-cards', views.init_cards, name='init-cards'),
]
