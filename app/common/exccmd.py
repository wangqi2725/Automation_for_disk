
import subprocess
import paramiko
import re
import winrm
import time
"""
旨在解决RF脚本发送到目标机
目标机-->执行。
目标机返回结果-->服务器。
目标机释放
"""


#1.RF脚本发送特定执行机（该执行机锁定）  （执行机每台机子都事先存放好最新的RF脚本）
#此步展示不需要代码实现
#2.链接执行机（windows，linux）   分发任务，发送执行命令：pybot

#local
# type = ''
# cmd = 'ping 127.0.0.1 -t'
# res = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
# while res.poll() is None:
#     line = res.stdout.readline()
#     line = line.strip()
#     if line:
#         print(line.decode('GBK','ignore'))


#linux
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname='192.168.225.183', port=22, username='root', password='abc@123')
#
# stdin, stdout, stderr = ssh_client.exec_command("ls", get_pty=True)
#
# while not stdout.channel.exit_status_ready():
#     result = stdout.readline()
#     print(result)
#
#     # 由于在退出时，stdout还是会有一次输出，因此需要单独处理，处理完之后，就可以跳出了
#     if stdout.channel.exit_status_ready():
#         a = stdout.readlines()
#         print(a)
#         break
#
# ssh_client.close()


#windows 1
class Win_Server(object):
    def __init__(self,ip,username,password):
        self.ip = ip
        self.username = username
        self.password = password
        # self.wintest = ''
        # self.shell_id = ''
        # self.command = ''

    def Connect(self):
        wintest = winrm.Session('http://' + self.ip + ':5985/wsman',auth=(self.username,self.password))
        return wintest

    def open(self,wintest):
        shell_id = wintest.protocol.open_shell()
        return shell_id

    def send(self,wintest,shell_id,command):
        command_id = wintest.protocol.run_command(shell_id=shell_id,command=command)
        return command_id

    def close(self,wintest,shell_id,command_id):
        wintest.protocol.cleanup_command(shell_id,command_id)
        wintest.protocol.close_shell(shell_id)

    def get_command_output(self,wintest,shell_id,command_id):
        res = winrm.Response(wintest.protocol.get_command_output(shell_id,command_id))
        self.close(wintest,shell_id,command_id)
        return res



#Linux
# class Server:
#     def __init__(self,server_ip,username,password,timeout=30):
#         self.server_ip = server_ip
#         self.username = username
#         self.password = password
#         self.timeout = timeout
#         self.retry_times = 3
#         self.transport = ''
#         self.conn = ''
#
#     def Connection_Server(self):
#         while True:
#             try:
#                 self.transport = paramiko.Transport(sock=(self.server_ip,22))
#                 self.transport.connect(username=self.username,password=self.password)
#                 self.conn = self.transport.open_session()
#                 self.conn.settimeout(self.timeout)
#                 self.conn.get_pty()
#                 self.conn.invoke_shell()
#                 print(u"------- 链接 {0} 成功 -------".format(self.server_ip))
#                 #数据解码
#                 print(self.conn.recv(65535).decode('utf-8'))
#                 return
#             except Exception:
#                 if self.retry_times != 0:
#                     print(u"------- 链接 {0} 失败,进行重试 -------" % self.server_ip)
#                     self.retry_times -= 1
#                 else:
#                     print(u'------- 重试 3次,程序退出! -------')
#                     exit()
#
#     def Disconnect(self):
#         self.transport.close()
#         self.conn.close()
#         print("Host Connect Close")
#
#     def send(self, cmd, patt='#'):
#         cmd += '\r'
#         p = re.compile(patt)
#         result = ''
#         self.conn.send(cmd)


#3.等待执行结果，收集日志，分析汇总
#4.服务端收集到信息后展示，释放执行机