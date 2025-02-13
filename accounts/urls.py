from django.urls import path
from . import views
urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path('orders/', views.orders, name='accounts.orders'),
    path("password-reset/", views.password_reset, name="accounts.password_reset"),
    path('verify/<str:username>/', views.verify_security_question, name='verify_security_question'),
    path('reset-password/<str:username>/', views.reset_password, name='reset_password'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('verify/<str:username>/', views.verify_security_question, name='verify_security_question'),
    path('reset-password/<str:username>/', views.reset_password, name='reset_password'),
    path('password-reset-success/', views.password_reset_success, name='password_reset_success'),
]