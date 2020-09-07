from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('about/', views.about_view, name='about'),
    path('categories/', views.Category_view.as_view(), name='categories'),
    path('categories/<slug:slug>/', views.Fuel_view.as_view()),
    path('categories/<slug:slug>/<int:pk>/', views.buyform)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)