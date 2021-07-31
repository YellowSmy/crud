from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main),
    path('', phraselist, name='list'),
    path('create/', phraseCreate, name='create'),
    path('update/<str:pk>/', phraseUpdate, name='update'),
    path('delete/<str:pk>/', phraseDelete, name='delete'),
]