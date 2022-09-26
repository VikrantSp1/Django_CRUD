from django.urls import path
from . import views
from .views import list_users
  
urlpatterns = [
  path('listusers', list_users.as_view(), name='home')   
]