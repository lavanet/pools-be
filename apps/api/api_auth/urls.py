from django.urls import path, include

from . import views

urlpatterns = [
    path('me/', views.me),
    path('token/', views.login_token, name='login_token'),
    path('session/', views.login_session, name='login_session'),
]
