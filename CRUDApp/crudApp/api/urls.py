from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.students_all),
    path("student/<int:id>/", views.student_info),
    path("student/new/", views.student_create),
    path("student/update/", views.student_update),
    path("student/delete/<int:id>/", views.student_delete),
]