from pyexpat import model
from blog.models import Register, Membership, Company
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer): 
     class Meta:
         model = Register
         fields = '__all__'

        
 
 
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'
    
    
     
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
    