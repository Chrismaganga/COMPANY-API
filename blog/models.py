from django.conf import settings    
import uuid
from django.db import models
from django.contrib.auth.models import User

class CompanyProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    company_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    company_name = models.CharField(max_length=200)

class UserProfile(models.Model):

    ranks = (
        ('casual', 'Casual'),
        ('security', 'Security'),
        ('analyst', 'Analyst'),
        ('seniorAnalyst', 'Senior Analyst'),
        ('manager', 'Manager'),
        ('seniorManager', 'Senior Manager'),
        ('director', 'Director'),
        ('regionalDirector', 'Regional Director'),
        ('chiefFinancialDirector', 'Chief Financial Director'),
    )

    companies = (
        ('codelovers', 'CodeLovers'),
        ('codecom', 'Codecom'),
    )
    company_name = models.CharField(max_length=200, choices=companies, default="Choose")
    user_id = models.UUIDField(default=uuid.uuid4(), editable=False, unique=True)
    username = models.CharField(max_length=500)
    name = models.CharField(max_length=200, default=None)
    surname = models.CharField(max_length=200, default=None)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    rank = models.CharField(max_length=200, choices=ranks)
