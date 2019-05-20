"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from todo import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.TodoListView.as_view(),name='home'),
    url(r'^(?P<pk>\d+)/$',views.TodoDetailView.as_view(),name='detail'),
    url(r'^create/',views.TodoCreateView.as_view()),
    url(r'^update/(?P<pk>\d+)/$',views.TodoUpdateView.as_view()),
    url(r'^delete/(?P<pk>\d+)/$',views.TodoDeleteView.as_view()),
    url(r'^api/',include('todo.api.urls'))
    ]
