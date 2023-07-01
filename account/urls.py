from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

from .views import MyTokenObtainPairView, ChangePasswordView, RegisterView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='jwt_login'),
    path('logout/', TokenBlacklistView.as_view(), name='jwt_logout'),
    path('change-password/', ChangePasswordView.as_view(), name='reset-password' ),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterView.as_view(), name="register_user"),
]
