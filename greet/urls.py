from django.urls import path
from . import views


app_name = 'greet'



urlpatterns = [
    # path('', views.greet_user, name='get_user'),
    path('greet/<str:name>/', views.greet_user, name='greet_user'),
]
