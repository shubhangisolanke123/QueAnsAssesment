from django.urls import path
from . import views

urlpatterns=[
   path('rv/',views.signupView,name='signup_url'),
   path('lv/',views.loginView,name='login_url'),
   path('lot/',views.logoutView,name='logout_url'),
]