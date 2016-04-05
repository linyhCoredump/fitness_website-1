# coding:utf-8
from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    projectid = models.IntegerField(default=0)  # 项目id
    projectname = models.CharField(max_length=128)  # 项目名
    imgpath = models.CharField(max_length=128)  # 图片路径

    def __unicode__(self):
        return self.projectname


class People(models.Model):
    userprofile = models.ForeignKey(User)
    # pwd = models.CharField(max_length=32)  # 密码
    # ame = models.CharField(max_length=128, unique=True)  # 名字
    age = models.IntegerField(default=12)                   # 年龄
    hight = models.IntegerField(default=0)                  # 身高
    weight = models.IntegerField(default=0)                 # 体重
    aim = models.CharField(max_length=128)              # 目标
    birth = models.DateField(null=True)                        # 出生日期
    city = models.CharField(max_length=128)             # 城市
    followed = models.IntegerField(default=0)              # 被点赞
    like = models.IntegerField(default=0)                   # 被关注
    dynamic = models.CharField(max_length=512)      # 动态
    picpath = models.CharField(max_length=128)  # 图片路径
    text = models.CharField(max_length=512)  # 分享文字
    sendtime = models.DateField(null=True)  # 时间戳

    def __unicode__(self):
        return self.age


class Subject(models.Model):
    projectid = models.ForeignKey(Project)  # 子项目id
    exername = models.CharField(max_length=64)  # 子项目名称
    exertime = models.IntegerField(default=0)  # 子项目时长
    level = models.IntegerField(default=0)  # 级别

    def __unicode__(self):
        return self.exername
