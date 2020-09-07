from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('personal/', views.personal_info),
    path('current_orders/', views.current_orders),
    path('all_orders/', views.all_orders),
    path('new_orders/', views.new_orders),
    path('new_orders/<int:pk>/', views.get_new_orders),
    path('my_req/', views.curr_req),
    path('made_req/', views.made_req),
    path('msg/', views.message_page),
    path('', views.dashboard, name='dashboard'),
]