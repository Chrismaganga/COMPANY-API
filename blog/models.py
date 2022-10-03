from django.db import models
from datetime import datetime

class Register(models.Model):
    first_name                   = models.CharField(max_length=200)
    last_name                    = models.CharField(max_length=200)
    age                          = models.IntegerField()
    # registered                   = models.ForeignKey(Registered, null=True, blank=True)                 
    city                         = models.CharField(max_length=200)
    country                      = models.CharField(max_length=200)
    email                        = models.EmailField()
    qualification                = models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
  
    
class Company(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    
        
    class Meta:
        verbose_name = ("company")
        verbose_name_plural = ("companies")

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Register, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    
 