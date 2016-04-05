#coding=utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fitness_website.settings')
import django
django.setup()

from fitness_app.models import People, Source, Project, Subject
    
def testscript():
    #images/fulls/01.jpg
    people_t = add_People('Tom', 20, 175, 60, '减肥','1995-03-03', 
    'NewYork', 84, 3,'今天我又喝了木瓜牛奶')
    add_Source(people_t, 'userImages/1.jpg', '你喜欢这样的我吗？呵呵，叔叔不约？', '2010-01-09')
    first_cat = add_project(1,'活力燃脂','images/fulls/01.jpg')
    add_subject(pid=first_cat,
        sname='HIIT适应性训练',
        stime=30,
        slvl=1)
    add_subject(pid=first_cat,
        sname='Tabata4分钟初级燃脂',
        stime=40,
        slvl=1)
    add_subject(pid=first_cat,
        sname='Tabata4分钟进阶燃脂',
        stime=40,
        slvl=1)    
    add_subject(pid=first_cat,
        sname='Tabata4分钟强化燃脂',
        stime=40,
        slvl=1)
    add_subject(pid=first_cat,
        sname='HIIT燃脂初级',
        stime=40,
        slvl=1)
        
    people_t = add_People('JACK', 20, 175, 60, '减肥','1995-03-03', 
    'NewYork', 84, 3,'今天我又喝了木瓜牛奶')
    add_Source(people_t, 'userImages/2.jpg', '你喜欢这样的我吗？呵呵，叔叔不约？', '2010-01-09')
    first_cat = add_project(2,'腹肌雕刻','images/fulls/02.jpg')
    add_subject(pid=first_cat,
        sname='健身球核心训练',
        stime=30,
        slvl=1)
    add_subject(pid=first_cat,
        sname='腹肌训练入门',
        stime=40,
        slvl=1)
    add_subject(pid=first_cat,
        sname='人鱼线雕刻',
        stime=40,
        slvl=1)    
    add_subject(pid=first_cat,
        sname='腹肌撕裂者强化',
        stime=40,
        slvl=1)
    add_subject(pid=first_cat,
        sname='核心改造',
        stime=40,
        slvl=1)
        
    people_t = add_People('邢文鹏', 20, 175, 60, '减肥','1995-03-03', 
    'NewYork', 84, 3,'今天我又喝了木瓜牛奶')
    add_Source(people_t, 'userImages/1.jpg', '你喜欢这样的我吗？呵呵，叔叔不约？', '2010-01-09')
    first_cat = add_project(3,'动作入门','images/fulls/01.jpg')
    add_subject(pid=first_cat,
        sname='零基础适应性训练',
        stime=30,
        slvl=1)
    add_subject(pid=first_cat,
        sname='腹肌训练入门',
        stime=40,
        slvl=1)
    add_subject(pid=first_cat,
        sname='健身房基础入门',
        stime=40,
        slvl=1)    
    add_subject(pid=first_cat,
        sname='俯卧撑入门',
        stime=40,
        slvl=1)
    add_subject(pid=first_cat,
        sname='深蹲入门',
        stime=40,
        slvl=1)
        
    people_t = add_People('林艳浩', 20, 175, 60, '减肥','1995-03-03', 
    'NewYork', 84, 3,'今天我又喝了木瓜牛奶')
    add_Source(people_t, 'userImages/1.jpg', '你喜欢这样的我吗？呵呵，叔叔不约？', '2010-01-09')
    first_cat = add_project(4,'跑步基础','images/fulls/01.jpg')
    add_subject(pid=first_cat,
        sname='跑步机HIIT变速跑',
        stime=30,
        slvl=1)
    add_subject(pid=first_cat,
        sname='跑步机有氧慢跑',
        stime=40,
        slvl=1)
    add_subject(pid=first_cat,
        sname='跑步机有氧健步走',
        stime=40,
        slvl=1)    
    add_subject(pid=first_cat,
        sname='下肢运动能力训练',
        stime=40,
        slvl=1)
    add_subject(pid=first_cat,
        sname='HIIT燃脂初级',
        stime=40,
        slvl=1)
        
    people_t = add_People('林艳浩', 20, 175, 60, '减肥','1995-03-03', 
    'NewYork', 84, 3,'今天我又喝了木瓜牛奶')
    add_Source(people_t, 'userImages/1.jpg', '你喜欢这样的我吗？呵呵，叔叔不约？', '2010-01-09')
    first_cat = add_project(5,'女生专题','images/fulls/01.jpg')
    add_subject(pid=first_cat,
        sname='一字马横叉',
        stime=30,
        slvl=1)
    add_subject(pid=first_cat,
        sname='一字马竖叉',
        stime=40,
        slvl=1)
    add_subject(pid=first_cat,
        sname='生理期舒缓训练',
        stime=40,
        slvl=1)    
    add_subject(pid=first_cat,
        sname='翘臀养成',
        stime=40,
        slvl=1)
    add_subject(pid=first_cat,
        sname='瘦腿训练',
        stime=40,
        slvl=1)                        
        
        
                          
  
#get_or_create       
def add_project(id,name,path):
    c = Project.objects.get_or_create(projectid=id,projectname=name,imgpath=path)[0]
    return c
    
def add_subject(pid,sname,stime,slvl=0):
    #pd = Project.objects.get(projectid=pid.projectid)
    p = Subject.objects.get_or_create(project_s=pid,exername=sname,exertime=stime,level=slvl)[0]
    return p

        
def add_People(myname, myage, myhight, myweight, myaim, mybirth, mycity, myfollowed, mylike, mydynamic):
    #mypro = Project.objects.get(projectid=myprojectid.projectid)
    c = People.objects.get_or_create(name=myname, 
    age=myage, hight=myhight, weight=myweight, 
    aim=myaim,birth=mybirth, city=mycity, followed=myfollowed, like=mylike, dynamic=mydynamic)[0]
    return c

def add_Source(myuid, mypicpath, mytext, mysendtime):
    #myu = People.objects.get(uid=myuid.uid)
    p = Source.objects.get_or_create(user=myuid, picpath=mypicpath, text=mytext, sendtime=mysendtime)[0]
    return p
    
if __name__ =='__main__':
    print "Starting test..."
    testscript()