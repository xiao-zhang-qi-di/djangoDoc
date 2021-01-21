from django.urls import path

from . import views

urlpatterns = [
    path('tes/', views.tes, name='tes'),
]