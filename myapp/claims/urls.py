from django.urls import path
from . import views


app_name = 'claims'

urlpatterns = [
    # path('/', views.login, name="login")
    path('view/', views.viewlist , name="viewlist"),
    path('index/', views.index, name="index"),
 
]

