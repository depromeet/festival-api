from django.urls import path

from .views import LoginAPIView

app_name = 'users'
urlpatterns = [
    path('login', LoginAPIView.as_view(), name='login'),
]
