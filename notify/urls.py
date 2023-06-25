from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('djoser.urls')),  # third party
    path('api/auth/', include('djoser.urls.jwt')),  # third party
    path('api/auth/', include('djoser.social.urls')),  # third party

    path('api/users/', include('base.urls.user_urls')),
]
