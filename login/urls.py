from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.home,name = 'login'),
    path('register/',views.register,name='register'),
    path('',views.HomeView.as_view(),name = 'home'),
]