from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('cabinet/', include('Cabinet.urls')),
    path('', include('Home.urls')),
]
