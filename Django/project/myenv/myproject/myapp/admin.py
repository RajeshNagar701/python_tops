from django.contrib import admin

from .models import * 

# Register your models here all table which you created so we can see all data in Admin pannel .

admin.site.register(User)     
admin.site.register(Feedback)
admin.site.register(Contact)