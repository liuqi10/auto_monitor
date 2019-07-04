#-*- coding:utf-8 -*-
import re,xlrd
import psutil,time
#数据备份到Excel文档接口
from ExcelConfig.excel_config import ConfigExcel,ReadExcel
#获取基础配置信息
from base_config.read_base_config import ReadBaseConfig
#获取单个进程的内存使用
class PidMemory():
    def __init__(self,pid_name):
        self.pid_name = pid_name
        data_time = ReadBaseConfig()
        self.time_count = int(data_time.get_monitor_time('get_monitor_time'))
    def get_pid_memory(self):
        pid_list = psutil.pids()
        p_name_list = []
        for i in range(len(pid_list)):
            p_info = psutil.Process(pid_list[i])
            p_name = p_info.name()
            if p_name == self.pid_name:
                p_name_list.append(pid_list[i])
        return p_name_list
    def get_pid(self):
        pid_mem =7768
        if pid_mem:
            p = psutil.Process(pid_mem)
            p_vsz = round(p.memory_info().vms/1024/1024/1024,2)
        else:
            print("程序未启动")
        return p_vsz
    # 计算pid单进程内存数据
    def get_pid_count(self, time_sum):
        count_time = 0
        pid_list = []
        while (count_time < time_sum):
            used_pid_data = self.get_pid()
            pid_list.append(used_pid_data)
            count_time += 1
            time.sleep(10)
        return pid_list

    # 运行GPU生成数据统计折线图，同时备份数据到Excel文档
    def get_pid_run(self):
        # 计算GPU使用率
        pid_list = self.get_pid_count(self.time_count)
        print("pid数据列表", pid_list)
        writefile = ConfigExcel(pid_list, 'TALLivePlatform')
        writefile.new_write_excel()

if __name__ == '__main__':
    pid_name = 'TALLivePlatform.exe'
    while True:
        data = PidMemory(pid_name)
        print(data.get_pid_memory())
        time.sleep(5)
    # while True:
    #     data.pid_memory()
    #     psutil.test()
    #     time.sleep(3)




