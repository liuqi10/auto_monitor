#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import wmi
c = wmi.WMI()
import psutil,time,threading
#数据备份到Excel文档接口
from ExcelConfig.excel_config import ReadExcel
#获取基础配置信息
from base_config.read_base_config import ReadBaseConfig
#获取单个进程的内存使用
class GetPid():
    def __init__(self):
        data_time = ReadBaseConfig()
        self.time_count = int(data_time.get_monitor_time('get_monitor_time'))
    def get_pid(self):
        pid_list = []
        p_name = ['TALLivePlatform.exe','TSClient.exe']
        for i in range(len(p_name)):
            for process in c.Win32_Process(name=p_name[i]):
                if process.Name==p_name[i]:
                    pid_list.append(process.ProcessId)
                else:
                    print("未找到" + p_name[i])
        return pid_list
    def pid_write_excel(self):
        writefile = ReadExcel()
        writefile.new_write_excel(self.get_pid())
    def run_pid(self):
        print("已获取的pid号：",self.get_pid())
        if len(self.get_pid()) < 2:
            time.sleep(1)
            self.run_pid()
        else:
            self.pid_write_excel()

if __name__ == '__main__':
    # data = GetPid()
    # pid_lists = data.run_pid()
    # datas = ReadExcel()
    # abc = datas.read_excel('pid.xls')
    # print(str(round(abc[0])))
    pass
