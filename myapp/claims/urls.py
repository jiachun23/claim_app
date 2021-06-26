from django.urls import path
from . import views


app_name = 'claims'

urlpatterns = [
    path('login/', views.login, name="login"),
    path('login/index/', views.index, name="index"),
 
]

