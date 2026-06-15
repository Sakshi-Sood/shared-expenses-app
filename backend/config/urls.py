from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path("", home),

    path("admin/", admin.site.urls),

    path("api/auth/", include("accounts.urls")),

    path(
        "api/auth/login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),

    path(
        "api/auth/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    path(
        "api/imports/",
        include("imports.urls")
    ),
]