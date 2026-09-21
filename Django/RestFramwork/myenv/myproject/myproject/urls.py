"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from myapp.views import UserList,UserDetail


urlpatterns = [
    path('api/users',UserList.as_view()),
    path('api/users/<int:pk>',UserDetail.as_view()),
    path('admin/', admin.site.urls),
]

# check in Django REST framework or in postman 
# http://127.0.0.1:8000/api/users   get method => get all data
# http://127.0.0.1:8000/api/users/1   get method => get single data

# http://127.0.0.1:8000/api/users   post method => post data by form or json
# http://127.0.0.1:8000/api/users/1   delete method => delete data by id
# http://127.0.0.1:8000/api/users/1   put method => update all column data by id
# http://127.0.0.1:8000/api/users/1   patch method => update particular column data by id

# http://127.0.0.1:8000/users?name=raj get method => get data by name
# http://127.0.0.1:8000/users?orderby=raj  get method => get data by orderby