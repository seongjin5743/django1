from django.contrib import admin
from django.urls import path

from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('hello/', views.hello),
    path('lunch/', views.lunch),
    path('lotto/', views.lotto),
    path('profile/<username>/', views.profile),
    path('cube/<int:number>', views.cube),
    path('articles/', views.articles),
]
