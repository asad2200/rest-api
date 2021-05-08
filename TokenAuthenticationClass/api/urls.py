from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('', views.StudentAPI, basename='student')

urlpatterns = [
    path('student/', include(router.urls)),
    path('auth-token/', obtain_auth_token),
]