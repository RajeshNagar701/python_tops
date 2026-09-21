from django.shortcuts import render,redirect
from django.http import HttpResponse  # response by HttpResponse

from .models import *  # all model load for crud

#django.contrib import messages is used in Django to display temporary messages to the user, such as success, error, warning, or information messages.
from django.contrib import messages # flash session for message
 
#Import make_password & check_password for encript
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

# by render get template page
def mydemo1(request):
    user1 = User.objects.all()
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            msg="Email already exits"
            return render(request,"test.html",{'msg':msg})
        except:
            User.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                password=make_password(request.POST['password']),
                mobile=request.POST['mobile'],
                gender=request.POST['gender'],
                hobby=",".join(request.POST.getlist('hobby'))
            )
            msg="Signup Success"
            return render(request,"test.html",{'msg':msg})
    else:
        print("**********else executed!!")
        return render(request,"test.html",{'user1':user1})

# by HttpResponse get response
def mydemo2(request):
    return HttpResponse("Hello world!")


# theme integration

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def menu(request):
    return render(request,"menu.html")

def book(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message=request.POST['message'],
        )
        msg="Booking Inquiry Success"
        return render(request,"book.html",{'msg':msg})
    else:
        return render(request,"book.html")

def signup(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            msg="Email already exits"
            return render(request,"signup.html",{'msg':msg})
        except:
            User.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                password=request.POST['password'],
                mobile=request.POST['mobile'],
                gender=request.POST['gender'],
                hobby=",".join(request.POST.getlist('hobby'))
            )
            msg="Signup Success"
            return render(request,"signup.html",{'msg':msg})
    else:
        return render(request,"signup.html")
    
    
def deleteuser(request,id):
    user = User.objects.get(id=id)
    user.delete()
    messages.success(request, "User deleted successfully!")
    return redirect('mydemo1')

def edituser(request,id):
    
    single_user = User.objects.get(id=id)
    
    if request.method == "POST":

        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        # Multiple checkbox values
        hobby = ",".join(request.POST.getlist('hobby'))  # Convert list to comma-separated string

       
        # Update database
        single_user.name = name
        single_user.email = email
        single_user.password = password
        single_user.mobile = mobile
        single_user.gender = gender
        single_user.hobby = hobby
        single_user.save()

        messages.success(request, "User Updated successfully!")
        # Redirect after update
        return redirect('mydemo1')

    hobby = single_user.hobby.split(",") # string to arr
    return render(request,"edit_user.html",{'single_user':single_user,'hobby': hobby})


def statususer(request,id):
    user = User.objects.get(id=id)
    if user.status == 'Block':
        user.status="Unblock"
        user.save()
        messages.success(request, "User Unblock successfully!")
        # Redirect after update
        return redirect('mydemo1')
    else:
        user.status="Block"
        user.save()
        messages.success(request, "User Block successfully!")
        # Redirect after update
        return redirect('mydemo1')
    
def login(request):
    try:
     user = User.objects.get(email=request.POST['email'])
     
     if check_password(request.POST['password'], user.password):
         request.session['email']=user.email
         request.session['name']=user.name
         request.session['id']=user.id
         
         return redirect('index')   
     else:
         msg="Password does not match!!"
         return render(request,"login.html",{'msg':msg})
    except:
        msg = "Email does not exist!!"
        return render(request,"login.html",{'msg':msg})
    

def logout(request):
    del request.session['email']
    del request.session['name']
    del request.session['id']
    return redirect('login')

"""

Other common Django ORM queries in DRF

# Exact
User.objects.filter(name='Rajesh')

# LIKE %raj%
User.objects.filter(name__contains='raj')

# LIKE %raj%, case-insensitive
User.objects.filter(name__icontains='raj')

# Starts with
User.objects.filter(name__startswith='Raj')

# Ends with
User.objects.filter(name__endswith='esh')

# Greater than
User.objects.filter(id__gt=5)

# Greater than or equal
User.objects.filter(id__gte=5)

# Less than
User.objects.filter(id__lt=10)

# Between
User.objects.filter(id__range=[5, 10])

# NULL
User.objects.filter(mobile__isnull=True)

# NOT equal
User.objects.exclude(gender='Male')

# Order
User.objects.all().order_by('name')

# Descending
User.objects.all().order_by('-name')




Quick ORM Cheat Sheet
Requirement	        Django ORM
All	                User.objects.all()
One	                User.objects.get(id=1)
Filter	            filter(name="Rajesh")
LIKE	            name__contains="raj"
LIKE ignore case	name__icontains="raj"
Starts	            name__startswith="Raj"
Ends	            name__endswith="esh"
Greater	            age__gt=18
Greater/equal	    age__gte=18
Less	            age__lt=50
Less/equal	        age__lte=50
Between	            age__range=(18,50)
IN	                id__in=[1,2,3]
NOT	                exclude() / ~Q()
OR	                Q() | Q()
AND	                Q() & Q()
Sort ASC	        order_by("name")
Sort DESC	        order_by("-name")
Count	            .count()
Exists	            .exists()
First	            .first()
Last	            .last()
Fields	            .values()
Tuples	            .values_list()
Unique	            .distinct()
NULL	            field__isnull=True
Group By	        .values().annotate()
Count group	        Count()
Average	            Avg()
Maximum	            Max()
Minimum	            Min()
Sum	                Sum()
Update	            .update()
Delete	            .delete()
Create	            .create()


"""
