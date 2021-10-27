"""medsoverflow URL Configuration

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
from os import name
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

app_name = 'mainframe'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('profile/<int:pk>', views.Profile.as_view(), name='profile'),
    path('question/<int:pk>', views.Post.as_view(), name='question'),
    path('askq', login_required(login_url='/login')(views.AskQuestion.as_view()), name='ask'),
    path('register', views.Register.as_view(), name='register'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('tag/<int:pk>', views.TagFilter.as_view(), name='tagFilter'),
    path('alltags', views.Tags.as_view(), name='alltags'),
    path('allusers', views.AllUsers.as_view(), name='allusers'),

    path('upvote/<int:qpk>', login_required(login_url='/login')(views.UpvoteQClass.as_view()), name='upvoteQ'),
    path('downvote/<int:qpk>', login_required(login_url='/login')(views.DownvoteQClass.as_view()), name='downvoteQ'),

    path('bookmark/<int:qpk>', login_required(login_url='/login')(views.BookmarkClass.as_view()), name='bookmark'),

    path('upvoteA/<int:qpk>/<int:apk>', login_required(login_url='/login')(views.UpvoteAClass.as_view()), name='upvoteA'),
]
