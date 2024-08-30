from django.urls import path, include
from . import views
from django.contrib.auth import views as authviews

app_name = 'accounts'
urlpatterns = [
    path('', authviews.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.signin, name='signin'),
]
