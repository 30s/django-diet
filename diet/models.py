from django.db import models

class Diet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted = models.BooleanField(default=False)
    openid = models.CharField(max_length=32)
    food = models.CharField(max_length=64)    
