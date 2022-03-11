from django.urls import path

from listings.views import listing

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]
