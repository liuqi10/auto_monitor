#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import psutil,wmi,time
def get_pid_cpu():
    #找出本机CPU的逻辑核个数
    cpucount = psutil.cpu_count(logical=True)
    #监控指定进程的CPU使用
    p = psutil.Process(11348)
    p_cpu = p.cpu_percent(interval=1)
    cpu_pec = round(p_cpu/cpucount,2)
    print(cpu_pec)
while True:
    get_pid_cpu()
    time.sleep(2)
# p1 = psutil.cpu_count()
# print(p1)
# p2 =psutil.cpu_count(logical=False)
# print(p2)
# p3 =psutil.cpu_count(logical=True)
# print(p3)