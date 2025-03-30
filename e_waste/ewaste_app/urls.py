from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'ewaste_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('collection-points/', views.collection_points, name='collection_points'),
    path('request-collection/', views.request_collection, name='request_collection'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='ewaste_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
