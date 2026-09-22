from rest_framework import serializers
from .models import User


#translators :  These act as the translators. 
#They serialize complex data (like Django QuerySets and model instances) 
#into native Python datatypes that can easily be rendered into JSON, XML, or YAML. 

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('id','name','email','mobile','gender')
		# fields = '__all__'
        
        