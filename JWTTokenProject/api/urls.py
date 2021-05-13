from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('', views.StudentAPI, basename='student')

urlpatterns = [
    path('student/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name="obtain_token"),
    path('api/token/refresh/',
         TokenRefreshView.as_view(),
         name="refresh_token"),
    path('api/token/verify/', TokenVerifyView.as_view(), name="verify_token"),
]