from django.urls import path
from . import views
from .views import list_users,newUser,address,RegisterUser
from rest_framework.authtoken import views
  
urlpatterns = [
  path('listusers', list_users.as_view(), name='home'),
  path('newusers', newUser.as_view(), name='home'),
  path('address', address.as_view(), name='address'),
  path('register', RegisterUser.as_view(), name='register'),
  path('api-token-auth/', views.obtain_auth_token),     

]