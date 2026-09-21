from django.shortcuts import render
from django.http import HttpResponse  # response by HttpResponse


# by render get template page
def mydemo1(request):
    return render(request,"test.html")

# by HttpResponse get response
def mydemo2(request):
    return HttpResponse("Hello world!")

# Create your views here.
