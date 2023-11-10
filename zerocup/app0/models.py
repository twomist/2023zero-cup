from django.db import models

class Message(models.Model):
    content = models.CharField(verbose_name="内容", max_length=255,default='nothing')
    type = models.CharField(verbose_name='类型', max_length=4)
