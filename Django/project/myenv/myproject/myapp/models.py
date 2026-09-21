from django.db import models

# Create your models here.

class User(models.Model):
    
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=254,unique=True)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    hobby=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    status = models.CharField(
        max_length=10,
        choices=[
            ('Block', 'Block'),
            ('Unblock', 'Unblock'),
        ],
        default='Unblock'
    )
    created_at=models.DateTimeField(auto_now=True)

class Feedback(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    
class Contact(models.Model):
    
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=254)
    phone=models.BigIntegerField()
    message=models.CharField(max_length=255)
    
    
    def __str__(self):
        return f"{self.id} : {self.name}"