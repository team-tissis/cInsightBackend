from django.db import models
from django.utils import timezone

class Comment(models.Model):
    code = models.CharField(max_length=64)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comment"

    def __str__(self):
        return self.code
