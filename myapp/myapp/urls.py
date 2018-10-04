"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from riddles import views
from django.urls import path
from riddles.views import SignUp, RiddleFormView, RiddlesListView, MyUserUpdate2, LevelsListView, ChallistView, \
    CuriosityView, Ranking, HomePageView

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls'), name='login'),


    #lista z zagadkami
    url(r'^$', RiddlesListView.as_view(), name="index"),

    #podląg zagadki
    # url(r'^riddle/(?P<pk>[0-9]+)/$', RiddleView, name='riddle'),

    #tworzenie zagadki, raczej do wywalenia
    url(r'^riddles_form/(?P<pk>[0-9]+)/$', RiddleFormView.as_view(), name="riddle-form"),

    #rejestracja
    url(r'^signup/$', SignUp, name='signup'),

    #profil użytkownika
    path('profile/', views.userDetails, name="user-profile"),

    url(r'^profile/(?P<id>[0-9]+)/$', views.userDetails2, name="user-profile2"),

    #update użytkownika
    url(r'profile/edit', MyUserUpdate2.as_view(), name='profile-update'),

    url(r'^list/$', LevelsListView.as_view(), name='levellist'),

    url(r'^chall/$', ChallistView.as_view(), name='challist'),

    url(r'^costam/$', CuriosityView.as_view(), name='costam'),

    url(r'^rank/$', Ranking.as_view(), name='rank'),

    url(r'^homepage/$', HomePageView.as_view(), name='homepage')

    ]
