from django.contrib import admin

# Register your models here.

from .models import *

# 以行展示
# class ChoiceInline(admin.StackedInline):
# 以列展示
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3   # 提供3个足够的选项字段

class QuestionAdmin(admin.ModelAdmin):

    # 新增搜索框
    search_fields = ['question_text']

    # 展示所有记录
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 新增过滤器
    list_filter = ['pub_date']  # “任意时间”，“今天”，“过去7天”，“这个月”和“今年”

    # 更改admin站点的字段顺序
    # fields = ['pub_date', 'question_text']

    # 新增操作
    # 将表单分为几个字段集, fieldsets 元组中的第一个元素是字段集的标题
    fieldsets = [
        (None, {'fields': ['question_text']}),
        # 'classes':['collapse']可选择隐藏
        # ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # 添加外键的内容
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

