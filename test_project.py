#coding=utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fitness_website.settings')
import django
django.setup()

from fitness_app.models import Project,Subject
    
def testscript():
    #images/fulls/01.jpg
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
                          
    second_cat = add_project(2,'腹肌雕刻','images/fulls/02.jpg')
    add_subject(pid=second_cat,
        sname='健身球核心训练',
        stime=40,
        slvl=2)
    add_subject(pid=second_cat,
        sname='腹肌训练入门',
        stime=40,
        slvl=2) 
    add_subject(pid=second_cat,
        sname='人鱼线雕刻',
        stime=40,
        slvl=2) 
    add_subject(pid=second_cat,
        sname='腹肌撕裂者强化',
        stime=40,
        slvl=2)
    add_subject(pid=second_cat,
        sname='核心改造',
        stime=40,
        slvl=2)

    third_cat = add_project(3,'动作入门','images/fulls/03.jpg')
    add_subject(pid=third_cat,
        sname='零基础适应性训练',
        stime=40,
        slvl=3)
    add_subject(pid=third_cat,
        sname='腹肌训练入门',
        stime=40,
        slvl=3) 
    add_subject(pid=third_cat,
        sname='健身房基础入门',
        stime=40,
        slvl=3) 
    add_subject(pid=third_cat,
        sname='俯卧撑入门',
        stime=40,
        slvl=3)
    add_subject(pid=third_cat,
        sname='深蹲入门',
        stime=40,
        slvl=3)
        
    fourth_cat = add_project(4,'跑步基础','images/fulls/04.jpg')
    add_subject(pid=fourth_cat,
        sname='零基础适应性训练',
        stime=40,
        slvl=4)
    add_subject(pid=fourth_cat,
        sname='腹肌训练入门',
        stime=40,
        slvl=4) 
    add_subject(pid=fourth_cat,
        sname='健身房基础入门',
        stime=40,
        slvl=4) 
    add_subject(pid=fourth_cat,
        sname='俯卧撑入门',
        stime=40,
        slvl=4)
    add_subject(pid=fourth_cat,
        sname='深蹲入门',
        stime=40,
        slvl=4)
        
    fifth_cat = add_project(5,'女生专题','images/fulls/05.jpg')
    add_subject(pid=fifth_cat,
        sname='一字马横叉',
        stime=40,
        slvl=5)
    add_subject(pid=fifth_cat,
        sname='一字马竖叉',
        stime=40,
        slvl=5) 
    add_subject(pid=fifth_cat,
        sname='生理期舒缓训练',
        stime=40,
        slvl=5) 
    add_subject(pid=fifth_cat,
        sname='生理期有氧',
        stime=40,
        slvl=5)
    add_subject(pid=fifth_cat,
        sname='翘臀养成',
        stime=40,
        slvl=5)                   
        
        
           
    '''
    for c in Project.objects.all():
        for p in Subject.objects.filter(projectid=c.projectid):
            print "- {0} - {1}".format(str(c.projectname),str(p.exername))
    '''
       
def add_project(id,name,path):
    c = Project.objects.get_or_create(projectid=id,projectname=name,imgpath=path)[0]
    return c
    
def add_subject(pid,sname,stime,slvl=0):
    p = Subject.objects.get_or_create(projectid=pid,exername=sname,exertime=stime,level=slvl)[0]
    return p           

if __name__ =='__main__':
    print "Starting test..."
    testscript()