from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.LCStudentAPI.as_view()),
    path('student/<int:pk>/', views.RUDStudentAPI.as_view()),
]