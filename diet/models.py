from django.db import models

class Diet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    openid = models.CharField(max_length=32)
    food = models.CharField(max_length=64)
