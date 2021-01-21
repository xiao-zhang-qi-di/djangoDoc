import datetime

from django.utils import timezone
from django.db import models

# Create your models here.


class Question(models.Model):
    """问题"""
    question_text = models.CharField(max_length=200, verbose_name='问题内容')
    pub_date = models.DateTimeField(verbose_name='发布日期')
    name = models.CharField(null=True, max_length=20)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # bug: 日期在未来也会是True
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # 修复bug, 只在日期是过去式的时候才会返回True
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    # admin站点显示
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '是否最近发布'

    class Meta:
        # admin管理站点类名显示中文
        verbose_name = '问题'
        verbose_name_plural = verbose_name

class Choice(models.Model):
    """选项"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='关联的问题')
    choice_text = models.CharField(max_length=200, verbose_name='选项内容')
    votes = models.IntegerField(default=0, verbose_name='票数')

    def __str__(self):
        return self.choice_text

    class Meta:
        # admin管理站点类名显示中文
        verbose_name = '选项'
        verbose_name_plural = verbose_name


