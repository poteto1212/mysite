from django.db import models
from django.untils import timezone
# Create your models here.

class post(models.Model):
    author=models.ForeignKey(setting.AUTH_USER_MODEL,on_delete=models.CASCADE)
    