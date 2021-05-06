from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.LCStudentAPI.as_view()),
    path('student/<int:id>/', views.RUDStudentAPI.as_view()),
]