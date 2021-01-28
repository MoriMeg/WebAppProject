from django.db import models


class MaintenanceModel(models.Model):
    date = models.DateField()                               # 日付
    category = models.CharField(max_length=100)             # カテゴリ
    content = models.CharField(max_length=100)              # 内容
    comment = models.TextField()                            # 備考
    author = models.CharField(max_length=100)               # 記録者
    images = models.ImageField(upload_to='', blank=True)    # 写真


class ConsumableModel(models.Model):
    datetime = models.DateTimeField()
    elapsed_time = models.IntegerField()
    elapsed_days = models.IntegerField()
