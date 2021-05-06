from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.StudentAPI, basename='student')

urlpatterns = [
    path('student/', include(router.urls)),
]