from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user),
    path('signup/', views.signup),
    path('logout/', views.logout_user),
    path('change-password/', views.change_password),
    path('profile/', views.user_profile_view),
]
