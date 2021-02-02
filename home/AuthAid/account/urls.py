from django.urls import path
from .views import registration_view, logout_view

app_name = 'account'

urlpatterns = [
    path('register/',registration_view, name='register'),
    path('logout/',logout_view,name='logout')
]