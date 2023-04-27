from django.urls import path
from .views import TodoAPIView

urlpatterns = [
    path('todos/', TodoAPIView.as_view()),
    path('todos/<str:pk>/', TodoAPIView.as_view())
]