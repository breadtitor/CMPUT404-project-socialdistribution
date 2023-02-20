from django.urls import path
from . import views

urlpatterns = [
  path('authors/<slug:uid>', views.AuthorView, name='AuthorView'),
]