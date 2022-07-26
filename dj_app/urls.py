from django.urls import path
from dj_app import views

urlpatterns = [
    path('', views.index_page, name='homepage'),
    
]