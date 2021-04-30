from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django_apscheduler import models
from app.common.exccmd import Win_Server
from datetime import date,datetime
import base64

schecduler = BackgroundScheduler()
schecduler.add_jobstore(DjangoJobStore(), 'default')


@csrf_exempt
def apschedulerpage(request):
    # jobs = models.DjangoJob.objects.all()
    jobs = DjangoJobStore().get_all_jobs()
    # print(jobs)

    jobexes = models.DjangoJobExecution.objects.all()


    # a = schecduler.get_jobs()
    # print(a)
    # schecduler.start()
    # d.remove_all_jobs()

    # job = schecduler.add_job(test, 'interval', seconds=5,args=['wq', 'wq', ])
    # print(job)
    # print(job.id)
    # print(job.name)
    # print(job.next_run_time)
    # print(job.executor)
    # D.add_job(job)
    # b = schecduler.get_jobs()

    # schecduler.start()

    if request.method == "GET":
        return render(request,'assets/Apscheduler.html',{"jobs":jobs,"jobexes":jobexes})

    if request.method == "POST":
        apscmd = request.POST.get('apscmd')
        aspmachine = request.POST.get("aspmachine")
        execute = request.POST.get('execute')
        try:
            # schecduler.remove_all_jobs()

            if execute == "interval":
                ITV_number = request.POST.get("number")
                ITV_size = request.POST.get("selecttime")
                s_time = request.POST.get("stime")
                e_time = request.POST.get("etime")
                if ITV_size == "s":
                    schecduler.add_job(test, execute, seconds = int(ITV_number),args=[apscmd,aspmachine,])
                    # schecduler.add_job(test, execute, seconds=int(ITV_number), start_date=s_time, end_date=e_time,
                    #                    args=[apscmd,aspmachine,])
                elif ITV_size == "m":
                    # schecduler.add_job(test, execute, minutes = int(ITV_number), args=['测试', ])
                    schecduler.add_job(test, execute, seconds=int(ITV_number), start_date=s_time, end_date=e_time,
                                       args=[apscmd,aspmachine,])
                elif ITV_size == "h":
                    # schecduler.add_job(test, execute, hours = int(ITV_number), args=['测试', ])
                    schecduler.add_job(test, execute, seconds=int(ITV_number), start_date=s_time, end_date=e_time,
                                       args=[apscmd,aspmachine,])
                elif ITV_size == "d":
                    # schecduler.add_job(test, execute, days=int(ITV_number), args=['测试', ])
                    schecduler.add_job(test, execute, seconds=int(ITV_number), start_date=s_time, end_date=e_time,
                                       args=[apscmd,aspmachine,])
                elif ITV_size == "w":
                    # schecduler.add_job(test, execute, weeks = int(ITV_number), args=['测试', ])
                    schecduler.add_job(test, execute, seconds=int(ITV_number), start_date=s_time, end_date=e_time,
                                       args=[apscmd,aspmachine,])

            elif execute == "date":
                year = request.POST.get("year")
                month = request.POST.get("month")
                day = request.POST.get("day")
                schecduler.add_job(test, execute, run_date=date("%s"%year,"%s"%month,"%s"%day), args=[apscmd,aspmachine,])

            elif execute == "cron":
                CIR = request.POST.get("cycle")
                schecduler.add_job(test,'cron',day_of_week=CIR,args=[apscmd,aspmachine,])


            message = "定时任务添加成功!"

            # schecduler.start()
            # default_jobs = schecduler.get_jobs(jobstore='default')
            # print(default_jobs)

        except Exception as e:
            message = e
        return render(request, 'assets/Apscheduler.html', {"jobs":jobs,"jobexes":jobexes,"message":message})


# def test(ip,username,password,cmd):
#     win = Win_Server(ip=ip,username=username,password=password)
#     wintest = win.Connect()
#     s_id = win.open(wintest=wintest)
#     c_id = win.send(wintest=wintest,shell_id=s_id,command=cmd)



def test(x,y):
    print("命令：{0},执行机：{1}".format(x,y))
