#-*- coding:utf-8 -*-
import psutil,socket,time
from TimeConfig.config_time import ConfigTime
from MysqlConfig.base_sql import BaseSql
from pynvml import *
#windows系统监控
class WindowsMonitor(object):
    def __init__(self):
        pass
    def getIp(self):
        myname = socket.getfqdn(socket.gethostname())
        myaddr = socket.gethostbyname(myname)
        return myaddr
    def getmemory(self):
        memo = psutil.virtual_memory() #获取系统的内存
        total = memo.total  #内容总数
        mp = memo.percent
        return mp
    #获取cpu信息
    def getcpu(self):
        data = psutil.cpu_times() #获取CPU的详细信息
        cpupercent = psutil.cpu_percent(1) #获取CPU的使用率

        return cpupercent
    #获取GPU信息
    def getgpu(self):
        # nvmlInit()
        data = nvmlSystemGetDriverVersion()
        print(data)
    #获取指定磁盘监控
    def getdisk(self0):
        fq = psutil.disk_partitions()#获取磁盘分区情况
        pe = psutil.disk_usage(fq[0].device)#获取指定磁盘使用率
        return pe.percent
    #获取指定网口的信息
    def getnet(self):
        net = psutil.net_io_counters(pernic=True)#获取每个网口的监控信息
        sent = net.get('以太网').packets_sent #获取网络发包
        recv = net.get('以太网').packets_recv #获取网络收包
        return sent,recv
    def run_main(self):
        while(True):
            dtime = ConfigTime().gettime
            data = BaseSql()

            # if self.getcpu()>5.0:
            #     print(self.getcpu())
            data.countsql(self.getIp(),self.getmemory(),self.getcpu(),self.getdisk(),self.getnet()[0],self.getnet()[1])
            # else:
            #     # print(self.getIp(),self.getmemory(),self.getcpu(),self.getdisk(),self.getnet()[0],self.getnet()[1],dtime)
            #     print("小于5.0：",self.getcpu())
            time.sleep(3)
if __name__ == "__main__":
    moniter = WindowsMonitor()
    moniter.run_main()
