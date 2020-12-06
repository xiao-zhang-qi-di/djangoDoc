from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'
    verbose_name = 'polls（投票）'  # admin管理站点中子应用的别名
