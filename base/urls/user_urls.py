from django.urls import path
from base.views import user_views as views

urlpatterns = [
    path('', views.getUsers, name='users'),
    path('login/', views.custom_login_view, name='login'),
    path('activate/', views.custom_activation_view, name='activate'),
    path('reset-password/', views.custom_request_password_reset,
         name='password-reset'),
    path('update-profile/', views.updateUserProfile, name='user-update-profile'),
    path('google/', views.GoogleCodeVerificationView.as_view(),
         name='google-callback'),
    path('<str:pk>/', views.getUserById, name='user'),
    path('<str:pk>/update/', views.updateUser, name='user-update'),
    path('<str:pk>/delete/', views.deleteUser, name='user-delete'),
]
