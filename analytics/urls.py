from django.urls import path

from analytics import views

urlpatterns = [
    path('', views.index, name="index"),
]
