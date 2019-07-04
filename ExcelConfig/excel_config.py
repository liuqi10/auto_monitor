#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import xlwt,os,xlrd
#获取当前系统时间
from TimeConfig.config_time import ConfigTime
from TimeConfig.config_time import ConfigTime
#获取基础配置信息
from base_config.read_base_config import ReadBaseConfig

class ConfigExcel():
    def __init__(self,type_list,typename):
        #获取当前系统的时间
        base_time = ConfigTime()
        self.nowtime =base_time.gettime + typename+".xls"
        #获取基础配置信息
        base_info = ReadBaseConfig()
        picture_filepath = base_info.get_filepath('picturepath')
        self.save_filepath = os.path.join(picture_filepath,self.nowtime)#保存备份数据的地址
        print(self.save_filepath)
        self.type_value = type_list
    def new_write_excel(self):
        # 创建一个workbook 设置编码,创建一个工作簿
        wb = xlwt.Workbook(encoding='utf-8')
        # 创建一个名为worksheet表单
        ws = wb.add_sheet('AB')
        mem_list = len(self.type_value)
        for i in range(mem_list):
            # 插入数据
            ws.write(i,0,self.type_value[i])
        #保存文件的名称
        wb.save(self.save_filepath)
class ReadExcel():
    def __init__(self):
        # 获取基础配置信息
        base_info = ReadBaseConfig()
        self.filepath = base_info.get_filepath('picturepath')
        base_info = ReadBaseConfig()
        self.save_filepath = os.path.join(base_info.get_filepath('picturepath'),'pid.xls')
        # print(self.save_filepath)
    def new_write_excel(self,pid_list):
        # 创建一个workbook 设置编码,创建一个工作簿
        wb = xlwt.Workbook(encoding='utf-8')
        # 创建一个名为worksheet表单
        ws = wb.add_sheet('AB')
        mem_list = len(pid_list)
        for i in range(mem_list):
            # 插入数据
            ws.write(i,0,pid_list[i])
        #保存文件的名称
        wb.save(self.save_filepath)
    def read_excel(self,filename):
        file_path = os.path.join(self.filepath,filename)
        #打开指定目录下的文档
        try:
            openfile = xlrd.open_workbook(file_path)
            # 获取sheet文档
            sheets = openfile.sheet_by_name('AB')
            nrows = sheets.nrows  # 获取行数
            data_list = []
        except Exception as e:
            print(e)
        try:
            for i in range(nrows):
                data_list.append(sheets.cell(i, 0).value)
            return data_list
        except Exception as e:
            print(e)

if __name__ == "__main__":
    # pid_list = [16228, 9804]
    # data = ReadExcel()
    # data.new_write_excel(pid_list)
    # abc = data.read_excel('pid.xls')
    # print(abc)
    pass