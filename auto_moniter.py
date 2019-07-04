#-*- coding:utf-8 -*-
import time,threading
import psutil,pynvml
#获取当前系统时间
from TimeConfig.config_time import ConfigTime
#获取基础配置信息
from base_config.read_base_config import ReadBaseConfig
#获取可视化图像接口
from PictureConfig import Picture
#数据备份到Excel文档接口
from ExcelConfig.excel_config import ConfigExcel,ReadExcel
from BaseFile.base_file import BaseFile
from wmi_get_pid import GetPid
from BaseFile.base_file import ConfigFile
#获取内存信息
class MemoryInfo():
    def __init__(self):
        data_time = ReadBaseConfig()
        self.time_count = int(data_time.get_monitor_time('get_monitor_time'))
    #统计内存数据
    def get_memory(self):
        memory_list = []
        # 获取系统的物理内存
        mem = psutil.virtual_memory()
        mem_total = str(round(mem.total / 1024 / 1024 / 1024))  # 内存转换成GB，取整数
        # print("系统物理总内存：", mem_total)
        # 获取系统总的内存：物理内存+虚拟内存
        swap = psutil.swap_memory()
        swap_total = round(swap.total / 1024 / 1024 / 1024,6)
        memory_list.append(swap_total)
        # print("系统总内存：", swap_total + "GB")
        swap_used = round(swap.used / 1024 / 1024 / 1024,6)
        memory_list.append(swap_used)
        # print("已使用的内存：", swap_used + "GB")
        return memory_list
    #计算内存数据
    def get_mem_count(self,time_sum):
        count_time = 0
        data_list = []
        while (count_time < time_sum):
            mem_data = self.get_memory()
            used_mem = round(mem_data[1], 2)
            data_list.append(used_mem)
            count_time += 1
            time.sleep(10)
        return data_list
    #运行内存，数据生成可是图片，同时备份Excel文档
    def get_mem_run(self):
        mem_list = self.get_mem_count(self.time_count)
        print("内存数据列表", mem_list)
        # 获取系统总内存数据
        mem_data = self.get_memory()
        total_mem = round(mem_data[0], 2)  # 系统总内存数据保留2位小数
        total_mem_list = 'Memory total='+ str(total_mem)+'GB'
        #数据备份Excel文档
        writefile = ConfigExcel(mem_list,'mem')
        writefile.new_write_excel()
        #数据生成可视化折线图
        # mem_picture = Picture(mem_list,total_mem_list,'Memory/(GB)',total_mem,'mem')
        # mem_picture.get_picture()
        print("Memory end off ...")
    def get_picture(self):
        findname = BaseFile()
        find_name = findname.find_file('mem.xls')
        if find_name:
            read_excel = ReadExcel()
            mem_list = read_excel.read_excel(find_name)
            # 获取系统总内存数据
            mem_data = self.get_memory()
            total_mem = round(mem_data[0], 2)  # 系统总内存数据保留2位小数
            total_mem_list = 'Memory total=' + str(total_mem) + 'GB'
            mem_picture = Picture(mem_list, total_mem_list, 'Memory/(GB)', total_mem, 'mem')
            mem_picture.get_picture()
        else:
            print("未正确生成内存文档")
#获取CPU数据信息
class CpuInfo(MemoryInfo):
    #获取CPU使用率
    def get_cpu(self):
        cpu = psutil.cpu_percent(interval=1,percpu=False)
        return cpu
    #计算cpu使用率数据
    def get_cpu_count(self,time_sum):
        count_time = 0
        data_list = []
        while (count_time < time_sum):
            mem_data = self.get_cpu()
            used_mem = round(mem_data,2)
            data_list.append(used_mem)
            count_time += 1
            time.sleep(10)
        return data_list
    #运行CPU生成数据统计折线图，同时备份数据到Excel文档
    def get_cpu_run(self):
        # 计算CPU使用率
        cpu_list = self.get_cpu_count(self.time_count)
        print("CPU数据列表", cpu_list)
        # cpu_title_list = 'Cpu_Total_Percent/100%'
        #获取Excel文件写入接口
        writefile = ConfigExcel(cpu_list,'cpu')
        writefile.new_write_excel()
        #获取生成可视化图片接口
        # cpu_picture = Picture(cpu_list,cpu_title_list,'CpuPercent/(%)',100,'cpu')
        # cpu_picture.get_picture()
        print("CPU end off ...")
    def get_picture(self):
        findname = BaseFile()
        find_name = findname.find_file('cpu.xls')
        if find_name:
            read_excel = ReadExcel()
            cpu_list = read_excel.read_excel(find_name)
            cpu_title_list = 'Cpu_Total_Percent/100%'
            cpu_picture = Picture(cpu_list,cpu_title_list,'CpuPercent/(%)',100,'cpu')
            cpu_picture.get_picture()
        else:
            print("未正确生成CPU数据文档")
#监控系统独立显卡GPU信息
class GpuInfo():
    def __init__(self):
        data_time = ReadBaseConfig()
        self.time_count = int(data_time.get_monitor_time('get_monitor_time'))
    def get_gpu(self):
        pynvml.nvmlInit()
        # 获取GPU的数量
        deviceCount = pynvml.nvmlDeviceGetCount()
        #通过循环计算每个CPU的情况
        gpu_list = []
        for i in range(deviceCount):
            gpu_dict = {}
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            gpu_type = pynvml.nvmlDeviceGetName(handle)#获取GPU型号
            gpu_dict['GPUTYPE']=gpu_type
            gpu_info = pynvml.nvmlDeviceGetMemoryInfo(handle)#获取GPU信息
            gpu_total = round(gpu_info.total / 1024 / 1024 / 1024,2) # 第二块显卡总的显存大小GB
            gpu_used = round(gpu_info.used / 1024 / 1024 / 1024,2)  # 这里是字节bytes，所以要想得到以兆M为单位就需要除以1024**2
            gpu_free = round(gpu_info.free / 1024 / 1024 / 1024,2)  # 第二块显卡剩余显存大小
            gpu_dict['total'] = gpu_total
            gpu_dict['used'] = gpu_used
            gpu_dict['free'] = gpu_free
            gpu_list.append(gpu_dict)
        return gpu_list#返回系统所有GPU的使用信息
    # 计算内存数据
    def get_gpu_count(self, time_sum):
        count_time = 0
        gpu_list = []
        while (count_time < time_sum):
            gpu_data = self.get_gpu()
            used_gpu = gpu_data[0]['used']
            gpu_list.append(used_gpu)
            count_time += 1
            time.sleep(10)
        return gpu_list
    # 运行GPU生成数据统计折线图，同时备份数据到Excel文档
    def get_gpu_run(self):
        # 计算GPU使用率
        gpu_list = self.get_gpu_count(self.time_count)
        print("GPU数据列表", gpu_list)
        # gpu_data = self.get_gpu()
        # yheight = gpu_data[0]['total']
        # gpu_title_list = 'Gpu_Total_Percent='+str(yheight)+'GB'
        # 获取Excel文件写入接口
        writefile = ConfigExcel(gpu_list,'gpu')
        writefile.new_write_excel()
        # 获取生成可视化图片接口
        # gpu_picture = Picture(gpu_list, gpu_title_list, 'GpuPercent/(GB)',yheight,'gpu')
        # gpu_picture.get_picture()
        print("GPU end off ...")
    def get_picture(self):
        findname = BaseFile()
        find_name = findname.find_file('gpu.xls')
        if find_name:
            read_excel = ReadExcel()
            gpu_list = read_excel.read_excel(find_name)
            gpu_data = self.get_gpu()
            yheight = gpu_data[0]['total']
            gpu_title_list = 'Gpu_Total_Percent=' + str(yheight) + 'GB'
            gpu_picture = Picture(gpu_list, gpu_title_list, 'GpuPercent/(GB)', yheight, 'gpu')
            gpu_picture.get_picture()
        else:
            print("未生成GPU文档")
#获取单个进程的内存使用
class PidMemory():
    def __init__(self,pid_name,pid):
        self.pid_name = pid_name
        data_time = ReadBaseConfig()
        self.time_count = int(data_time.get_monitor_time('get_monitor_time'))
        self.pid = round(pid)
    #获取指定进程的内存使用数据
    def get_pid(self):
        pid_list = self.pid
        if pid_list:
            p = psutil.Process(pid_list)
            p_vsz = round(p.memory_info().vms / 1024 / 1024 / 1024, 2)
            return p_vsz
        else:
            print("程序未启动")
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
    # 运行备份数据到Excel文档
    def get_pid_run(self,file_name):
        # 计算GPU使用率
        pid_list = self.get_pid_count(self.time_count)
        print("pid数据列表", pid_list)
        writefile = ConfigExcel(pid_list,file_name)
        writefile.new_write_excel()
        print(file_name+"end off ...")
    #根据统计数据生成图片
    def get_picture(self,file_name,pid_name):
        findname = BaseFile()
        find_name = findname.find_file(file_name)
        print(find_name)
        if find_name:
            read_excel = ReadExcel()
            gpu_list = read_excel.read_excel(find_name)
            # 获取系统总内存数据
            base_total_mem = MemoryInfo()
            mem_data = base_total_mem.get_memory()
            total_mem = round(mem_data[0], 2)  # 系统总内存数据保留2位小数
            yheight = total_mem
            gpu_title_list = self.pid_name+'_Memory_Count(Total_Memory=' + str(total_mem) + 'GB)'
            gpu_picture = Picture(gpu_list, gpu_title_list, self.pid_name + '_Used_Memory/(GB)', yheight, pid_name)
            gpu_picture.get_picture()
        else:
            print("未正确生成文档")
#获取单个进程的cpu使用
class PidCpu():
    def __init__(self,pid_name,pid):
        self.pid_name = pid_name
        data_time = ReadBaseConfig()
        self.time_count = int(data_time.get_monitor_time('get_monitor_time'))
        self.pid = round(pid)
    #获取指定进程的内存使用数据
    def get_pid_cpu(self):
        pid_list = self.pid
        if pid_list:
            # 找出本机CPU的逻辑核个数
            cpucount = psutil.cpu_count(logical=True)
            # 监控指定进程的CPU使用
            p = psutil.Process(pid_list)
            p_cpu = p.cpu_percent(interval=1)
            cpu_pec = round(p_cpu / cpucount, 2)
            return cpu_pec
        else:
            print("程序未启动")
    # 计算pid单进程内存数据
    def get_pid_count(self, time_sum):
        count_time = 0
        pid_list = []
        while (count_time < time_sum):
            used_pid_data = self.get_pid_cpu()
            pid_list.append(used_pid_data)
            count_time += 1
            time.sleep(10)
        return pid_list
    # 运行备份数据到Excel文档
    def get_pid_run(self,file_name):
        # 计算cpu使用率
        pid_list = self.get_pid_count(self.time_count)
        print("pid数据列表", pid_list)
        writefile = ConfigExcel(pid_list,file_name)
        writefile.new_write_excel()
        print(file_name+"end off ...")
    #根据统计数据生成图片
    def get_picture(self,file_name,pid_name):
        findname = BaseFile()
        find_name = findname.find_file(file_name)
        if find_name:
            read_excel = ReadExcel()
            cpu_list = read_excel.read_excel(find_name)
            cpu_title_list = self.pid_name+'_Cpu_Count/%'
            cpu_picture = Picture(cpu_list, cpu_title_list, pid_name+'Percent/(%)', 100, pid_name)
            cpu_picture.get_picture()
        else:
            print("未正确生成但进程CPU数据文档")
#设置运行memory多线程函数
def A():
    base_data = MemoryInfo()
    base_data.get_mem_run()
    # base_data.get_picture()
#设置运行CPU多线程函数
def B():
    base_data = CpuInfo()
    base_data.get_cpu_run()
    # base_data.get_picture()
#设置运行memory多线程函数
def C():
    base_gpu = GpuInfo()
    base_gpu.get_gpu_run()
    # base_gpu.get_picture()
#设置运行TALLivePlatform.exe多线程函数，统计单个进程的memory使用情况
def D():
    pid_lists = ReadExcel()
    pids= pid_lists.read_excel('pid.xls')
    pid_name = 'TALLivePlatform.exe'
    data = PidMemory(pid_name,pids[0])
    data.get_pid_run('TALLivePlatform_memory')
#设置运行TSClient.exe多线程函数，统计单个进程的memory使用情况
def E():
    pid_lists = ReadExcel()
    pids = pid_lists.read_excel('pid.xls')
    pid_name = 'TSClient.exe'
    data = PidMemory(pid_name,pids[1])
    data.get_pid_run('TSClient_memory')
#设置运行TALLivePlatform.exe多线程函数,统计单个进程的CPU使用情况
def F():
    pid_lists = ReadExcel()
    pids = pid_lists.read_excel('pid.xls')
    pid_name = 'TALLivePlatform.exe'
    data = PidCpu(pid_name,pids[0])
    data.get_pid_run('TALLivePlatform_cpu')
#设置运行TSClient.exe多线程函数，统计单个进程的CPU使用情况
def G():
    pid_lists = ReadExcel()
    pids = pid_lists.read_excel('pid.xls')
    pid_name = 'TSClient.exe'
    data = PidCpu(pid_name,pids[1])
    data.get_pid_run('TSClient_cpu')
#启动多线程监控系统的CPU、GPU、memory
def run_monitor():
    print("cpu/mem/gpu开始并行执行...")
    t1 = threading.Thread(target=A,name='A')
    t2 = threading.Thread(target=B,name='B')
    t3 = threading.Thread(target=C,name='C')
    t1.start()
    t2.start()
    t3.start()
#启动多线程运行单进程的监控
def run_pid_monitor():
    print("pid(mem/cpu)开始并行执行...")
    t4 = threading.Thread(target=D,name='D')
    t5 = threading.Thread(target=E,name='E')
    t6 = threading.Thread(target=F,name='F')
    t7 = threading.Thread(target=G,name='G')
    t4.start()
    t5.start()
    t6.start()
    t7.start()
#通过实时获取需要监控进程的pid，控制多线程监控函数
def run_pid_monitor_main():
    data = GetPid()
    data.run_pid()
    pid_lists = ReadExcel()
    pids = pid_lists.read_excel('pid.xls')
    if len(pids)==2:
        run_pid_monitor()
    else:
        print("error")
        run_pid_monitor_main()
#设置生成曲线图等待时间
def control_time():
    data_time = ReadBaseConfig()
    time_count = int(data_time.get_monitor_time('get_monitor_time'))
    second_time = (time_count*10)+3600
    return second_time

#对所有的监控数据生成图片
def run_picture():
    #读取数据生成内存的曲线图
    base_data = MemoryInfo()
    base_data.get_picture()
    # #读取数据生成CPU的曲线图
    base_data = CpuInfo()
    base_data.get_picture()
    # #读取数据生成GPU的曲线图
    # base_gpu = GpuInfo()
    # base_gpu.get_picture()
    #读取数据生成单个线程的memory曲线图
    pid_name = 'TALLivePlatform.exe'
    file_name = 'TALLivePlatform_memory.xls'
    base_pid_mem = PidMemory(pid_name,1)
    base_pid_mem.get_picture(file_name,'TALLivePlatform_memory')
    #读取数据生成单个线程的memory曲线图
    pid_name = 'TSClient.exe'
    file_name = 'TSClient_memory.xls'
    base_pid_mem = PidMemory(pid_name,2)
    base_pid_mem.get_picture(file_name,'TSClient_memory')
    #读取数据生成单个线程的cpu曲线图
    pid_name = 'TALLivePlatform.exe'
    file_name = 'TALLivePlatform_cpu.xls'
    base_pid_mem = PidCpu(pid_name,1)
    base_pid_mem.get_picture(file_name,'TALLivePlatform_cpu')
    #读取数据生成单个线程的cpu曲线图
    pid_name = 'TSClient.exe'
    file_name = 'TSClient_cpu.xls'
    base_pid_mem = PidCpu(pid_name,2)
    base_pid_mem.get_picture(file_name,'TSClient_cpu')
if __name__ == '__main__':
    #运行前删除测试报告
    # cf = ConfigFile()
    # cf.run_del_file()
    # #运行cpu/gpu/mem监控函数
    # run_monitor()
    # #等待监控到phoenix进程起来获取到进程id，运行监控制定进程的memory使用
    # run_pid_monitor_main()
    #设置等待时间，等待多线程跑完所有监控
    # time.sleep(control_time())
    # #运行生成图片函数，对所有的统计数据绘制成曲线图
    # run_picture()










