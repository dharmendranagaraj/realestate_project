from django.urls.resolvers import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    # n number of realestate listing
    path('', views.index, name='realtors'),

]
