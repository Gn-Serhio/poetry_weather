from django.urls import path
from .models import City
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete'),
]