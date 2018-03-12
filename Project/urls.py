"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from CSE_Department import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login_view'),
    path('user_auth/', views.user_login, name='user_login'),
    path('profile/', views.show_profile, name='show_profile'),
    path('profile/all', views.profiles_view, name='profiles_view'),
    path('profile/other/<slug:username>', views.show_other_profile, name='show_other_profile'),
    path('profile/other/<slug:user>/papers', views.others_papers_view, name='others_papers_view'),
    path('register/', views.register_user, name='register_user'),
    path('profile/update', views.update_profile, name='update_profile'),
    path('logout/', views.logout_user, name='logout_user'),
    path('papers/', views.papers_view, name='papers_view'),
    path('seminars/', views.login_view, name='login_view'),
    path('papers/add/<slug:paper_type>', views.add_papers, name='add_papers'),
    path('papers/<slug:paper_type>/<int:pk>/edit', views.edit_papers, name='edit_papers'),
    path('papers/<slug:paper_type>/<int:pk>/delete', views.delete_papers, name='delete_papers'),
]
