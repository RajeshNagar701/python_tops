
from django.urls import path
from .import views  # import for view page function call

urlpatterns = [

    # create route & call function from views.py
    path('mydemo1/', views.mydemo1, name='mydemo1'),
    path('mydemo2/', views.mydemo2, name='mydemo2'),

    #theme intgration
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('signup/', views.signup, name='signup'),
    path('deleteuser/<int:id>', views.deleteuser, name='deleteuser'),
    path('edituser/<int:id>', views.edituser, name='edituser'),
    path('statususer/<int:id>', views.statususer, name='statususer'),
    
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
