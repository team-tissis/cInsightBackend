from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.TextField() 
    mail = models.TextField() 
    eoa = models.CharField(max_length=42) # user の wallet account address．
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"
