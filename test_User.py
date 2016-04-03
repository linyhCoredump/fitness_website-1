# coding=utf-8
import os
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_website.settings')
import django
django.setup()

from fitness_app.models import People, Source, Project, Subject
from test_Project import add_project, add_subject


def testscript():
    project_t = add_project(1, '活力燃脂')
    people_t = add_People(13, project_t, 'Tom', 20, 175, 60, '50',
                          '1995-03-03', 'NewYork', 84, 3, 'alkdaoiureqxadsfhjlsa')
    add_Source(people_t, 'wtf', 'asdklfj;qwpoieramsdnf', '2010-01-09')

    project_t = add_project(2, '腹肌雕刻')
    people_t = add_People(101, project_t, 'Jack', 30, 174, 70,
                          '40', '1992-08-12', 'San Antonio', 72, 5, 'zxcvzxcvxzcvzxcv')
    add_Source(people_t, 'hello', 'cheasdp', '2012-04-04')

    project_t = add_project(3, '动作入门')
    people_t = add_People(102, project_t, 'Kobe', 23, 180, 100,
                          '47', '2000-05-04', 'Los Angelas', 78, 7, 'qwerqwerqwerqwer')
    add_Source(people_t, 'shit', 'acoaocao', '2015-07-05')


def add_People(myuid, myprojectid, myname, myage, myhight, myweight, myaim, mybirth, mycity, myfollowed, mylike, mydynamic):
    c = People.objects.get_or_create(uid=myuid, projectid=myprojectid, name=myname, age=myage, hight=myhight, weight=myweight, aim=myaim,
                                     birth=mybirth, city=mycity, followed=myfollowed, like=mylike, dynamic=mydynamic)[0]
    return c


def add_Source(myuid, mypicpath, mytext, mysendtime):
    p = Source.objects.get_or_create(
        uid=myuid, picpath=mypicpath, text=mytext, sendtime=mysendtime)[0]
    return p

if __name__ == '__main__':
    print "testing..."
    testscript()
