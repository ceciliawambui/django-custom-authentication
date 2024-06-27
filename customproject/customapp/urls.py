# from django.contrib import admin
# from django.urls import path
from . import views

# from django.urls import path
# from .views import SignupView, LoginView, LogoutView

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('signup/', SignupView.as_view(), name='signup'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
# ]
from django.urls import path
from .views import signup_view, login_view, logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]


