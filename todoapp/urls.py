"""todoapp URL Configuration

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
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # auth
    path(route='signup/', view=views.signupuser, name='signupuser'),
    path(route='login/', view=views.loginuser, name='loginuser'),
    path(route='logout/', view=views.logoutuser, name='logoutuser'),

    # todos
    path(route='', view=views.home, name='home'),
    path(route='create/', view=views.createtodo, name='createtodo'),
    path(route='current/', view=views.currenttodos, name='currenttodos'),
    path(route='completed/', view=views.completedtodos, name='completedtodos'),
    path(route='todo/<int:todo_pk>', view=views.viewtodo, name='viewtodo'),
    path(route='todo/<int:todo_pk>/complete', view=views.completetodo, name='completetodo'),
    path(route='todo/<int:todo_pk>/delete', view=views.deletetodo, name='deletetodo'),
]
