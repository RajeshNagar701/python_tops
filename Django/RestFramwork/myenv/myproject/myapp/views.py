from django.shortcuts import render

from rest_framework import generics
from .models import User
from myapp.serializers import UserSerializer

# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()

        name = self.request.query_params.get('name') # http://127.0.0.1:8000/users?name=raj
        orderby = self.request.query_params.get('orderby') # http://127.0.0.1:8000/users?orderby=raj

        if name:
            queryset = queryset.filter(name__icontains=name)

        if orderby:
            queryset = queryset.order_by(orderby)

        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=User
	serializer_class=UserSerializer
 
 

