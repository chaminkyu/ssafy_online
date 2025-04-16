from django.urls import path

# . : 현재 디렉토리
from . import views

# {% url namespace:name %}
# app_name = 'namespace'
app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
]
