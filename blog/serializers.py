from blog.models import CompanyProfile, UserProfile
from rest_framework import serializers


class CompanyProfileSerializer(serializers.ModelSerializer): 
     class Meta:
         model = CompanyProfile
         fields = [
            'username',
            'company_id',
            'company_name'
         ]

        
 
 
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'company_name',
            'company_id',
            'username',
            'name',
            'surname',
            'email',
            'password',
            'rank'
        ]
    
    
     

    