from django.contrib import admin
from django.urls import path

from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('hello/', views.hello),
    path('lunch/', views.lunch),
    path('lotto/', views.lotto),
    path('profile/<username>/', views.profile), # username을 인자로 받음
    path('cube/<int:number>', views.cube), # number를 int로 변환하여 인자로 받음
    path('articles/', views.articles),
]
