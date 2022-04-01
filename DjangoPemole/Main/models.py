from django.db import models
from django.utils import timezone


class Photo(models.Model):
    title = models.CharField(max_length=100, verbose_name='標題')
    path = models.CharField(max_length=300, verbose_name='圖片路徑')
    story = models.TextField(verbose_name='圖片敘述')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='上傳時間')


    def __str__(self):
        return self.title