from django.urls import path
from . import views

urlpatterns = [
    # Vue publique
    path('', views.home, name='home'),
    
    # Vues privées (requièrent authentification)
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.user_profile, name='profile'),
    path('api/user-info/', views.user_info_api, name='user_info_api'),
]
