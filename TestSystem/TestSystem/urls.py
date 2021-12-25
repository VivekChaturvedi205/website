"""TestSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home1),
    path('index/', views.home),
    path('Sign-up/', views.sign_up),
    path('client_list/', views.show_list),
    path('process_reg/', views.Process),
    path('login/', views.login),
    path('login-process/', views.login_process),
    path('result/', views.result),
    path('logout/', views.logout),
    path('quiz/', views.Quiz1),
    path('saveclient/', views.saveclient),
    path('quizresult/', views.quizresult),
    
]
