from django.contrib import admin
from blog import models

admin.site.register(models.Register)
admin.site.register(models.Company)
admin.site.register(models.Membership)
