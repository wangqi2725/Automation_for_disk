from django.shortcuts import render,get_object_or_404
from django.shortcuts import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json,re
from datetime import datetime,date
from app import models
from app import asset_handler



@csrf_exempt
def report(request):
    if request.method == "POST":
        asset_data = request.POST.get('asset_data')
        data = json.loads(asset_data)
        if not data:
            return HttpResponse("No Data!")
        if not issubclass(dict,type(data)):
            return HttpResponse("Only Support Dict!")
        sn = data.get('sn',None)
        if sn:
            asset_obj = models.Asset.objects.filter(sn=sn)
            if asset_obj:
                update_asset = asset_handler.UpdateAsset(request,asset_obj[0],data)
                return HttpResponse("Data is Update!")
            else:
                obj = asset_handler.NewAsset(request,data)
                response = obj.add_to_new_assets_zone()
                return HttpResponse(response)
        else:
            return HttpResponse("no sn ,please check data!")
    return HttpResponse("200 ok")

def index(request):
    assets = models.Asset.objects.all()
    return render(request,'assets/index.html',locals())

def dashboard(request):
    total = models.Asset.objects.count()
    upline = models.Asset.objects.filter(status=0).count()
    offline = models.Asset.objects.filter(status=1).count()
    unknown = models.Asset.objects.filter(status=2).count()
    breakdown = models.Asset.objects.filter(status=3).count()
    backup = models.Asset.objects.filter(status=4).count()
    up_rate = round(upline/total*100)
    o_rate = round(offline/total*100)
    un_rate = round(unknown/total*100)
    db_rate = round(breakdown/total*100)
    bu_rate = round(backup/total*100)
    server_number = models.Server.objects.count()
    networkdevice_number = models.NetworkDevice.objects.count()
    storagedevice_number = models.StorageDevice.objects.count()
    securitydevice_number = models.SecurityDevice.objects.count()
    software_number = models.Software.objects.count()

    return render(request,'assets/dashboard.html',locals())

def detail(request,asset_id):
    """"""
    asset = get_object_or_404(models.Asset,id=asset_id)
    return render(request,'assets/detail.html',locals())




# V2.0 新增 2021/4/22 K
@csrf_exempt
def exccmd(request):
    machines = models.ExeMachine.objects.all()

    if request.method == "GET":
        return render(request,'assets/exccmd.html',{"machines":machines})

    #TODO
    if request.method == "POST":
        from app.common.exccmd import Win_Server
        check_id = request.POST.get('vehicle')
        #TODO 优化
        cmd = request.POST.get('cmd')
        if len(cmd) == 0:
            message = "请输入执行命令,不可空指令运行!"
        elif check_id == None:
            message = "请选择执行机!"
        else:
            machine_obj = models.ExeMachine.objects.get(id=check_id)
            #TODO 批量运行 暂不实现
            status = machine_obj.status
            if status != "正常":
                message = "%s 设备组状态异常,命令未下发成功!"%(machine_obj.ip)
            else:
                try:
                    win = Win_Server(ip=machine_obj.ip,username=machine_obj.username,password=machine_obj.password)
                    wintest = win.Connect()
                    s_id = win.open(wintest)
                    c_id = win.send(wintest,s_id,cmd)
                    print("s_id:",s_id)
                    print("c_id:",c_id)
                    #修改执行机状态
                    EM = asset_handler.UpdateExcMachine(request,machine_obj,"占用")
                    EM.UpdateStatus()
                    message = "命令已下发：{0},实际执行结果请登录相关服务器查看!".format(cmd)
                except Exception as e:
                    print(e)
                    message = "check Target machine`s winrm service(cmd:net start winrm) or please check username and password"
        return render(request, 'assets/exccmd.html', {"message": message, "machines": machines})


@csrf_exempt
def CheckAndRelease(request):
    """"""
    if request.method == "GET":
        return render(request,'assets/Check.html')
    if request.method == "POST":
        from app.common.exccmd import Win_Server
        ip = request.POST.get('ip')
        username = request.POST.get('username')
        password = request.POST.get('password')
        s_id = request.POST.get('s_id')
        c_id = request.POST.get('c_id')
        machine_obj = models.ExeMachine.objects.get(ip=ip)
        try:
            win = Win_Server(str(ip),username=username,password=password)
            wintest = win.Connect()

            #TODO 此处存在bug，get_command_output需要等到命令执行完毕后才有回显，命令执行时间过长，这会卡顿或者持续不响应
            res = win.get_command_output(wintest,shell_id=s_id,command_id=c_id)

            # 修改执行机状态
            EM = asset_handler.UpdateExcMachine(request, machine_obj, "正常")
            EM.UpdateStatus()
            CMDRES = res.std_out.decode('GBK')
            return render(request,'assets/Check.html',{"CMDRES":CMDRES})

        except Exception as e:
            print(e)
            message = e
            return render(request,'assets/Check.html',{"message":message})

@csrf_exempt
def proposal(request):
    if request.method == "GET":
        return render(request,'assets/proposal.html')
    if request.method =="POST":
        pwd = request.POST.get('password')
        if pwd == "123":
            return render(request,'assets/proposal.html',{"body":True})
        else:
            return render(request,'assets/proposal.html',{"message":"你相信光吗？"})

def Inspection(request):
    return render(request,'assets/Inspection.html')

#需要单独创建页面
# @csrf_exempt
def upgrade(request):
    return render(request,'assets/upgrade.html')

def selectcase(request):
    return render(request,'assets/selectcase.html')
