from django.contrib import admin
from django.urls import path, include
# from .views import ObtainTokenView

# urlpatterns = [
#     path('token/', ObtainTokenView.as_view(), 'token')
# ]

from django.urls import path
from .views import RegisterView, CustomUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('view/', CustomUserView.as_view(), name='view')
]