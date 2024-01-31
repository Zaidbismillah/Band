from . import views
from django.urls import path
app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
    name='authenticate_user')
]