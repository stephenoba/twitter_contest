from django.urls import path
from play_ground import views

app_name = 'play_ground'

urlpatterns = [
    path('', views.home, name='home'),
]


