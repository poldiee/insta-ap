from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('', views.index, name='index')
]