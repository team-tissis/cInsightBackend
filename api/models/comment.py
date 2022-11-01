from django.db import models
from django.utils import timezone
from api.models.lecture import Lecture

class Comment(models.Model):
    lecture_id = models.ForeignKey(Lecture, on_delete=models.CASCADE) # lecture id 
    commenter_eoa = models.CharField(max_length=42) # 作成者 の wallet account address．
    code = models.CharField(max_length=64)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comment"

    def __str__(self):
        return self.code
