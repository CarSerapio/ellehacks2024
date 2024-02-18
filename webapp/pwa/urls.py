from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('index/', views.index, name="index"),
    path('volunteer/', views.volunteer, name="volunteer"),
    path('senior/', views.senior, name="senior"),
    path('map/', views.map, name="map"),
]