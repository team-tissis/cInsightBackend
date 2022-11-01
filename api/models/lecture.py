from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone

class Lecture(models.Model):
    name = models.TextField() 
    from_date = models.DateTimeField() 
    to_date = models.DateTimeField() 
    tag = models.CharField(max_length=30)
    description = models.TextField()
    material_url = models.URLField() # 資料 url
    record_url = models.URLField() # 動画 url

    attendee_max_num = models.IntegerField() # 参加上限数
    attendee_num = models.IntegerField() # 現在の参加者数
    attendee_eoas = JSONField() # userのwallet account addressのjson．"{"eoa":["0xhoge", "0xfuga"]}"

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "lecture"
