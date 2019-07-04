#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os,re
from shutil import copyfile
from base_config.read_base_config import ReadBaseConfig
from TimeConfig.config_time import ConfigTime
class BaseFile():
    def __init__(self):
        filepaths = ReadBaseConfig()
        self.filepath = filepaths.get_filepath('filepath')
        nowtime = ConfigTime()
        self.nt = nowtime.gettime
    def read_fileall(self):
        files = os.listdir(self.filepath)
        return files
    def find_file(self,name):
        for i in range(len(self.read_fileall())):
            filename = self.read_fileall()[i]
            if re.findall(name,filename):
                return filename
class ConfigFile(BaseFile):
    def __init__(self):
        filepaths = ReadBaseConfig()
        self.filepath = filepaths.get_filepath('filepath')
        self.copypath = filepaths.get_filepath('dstpath')
        nowtime = ConfigTime()
        self.nt = nowtime.gettime
    #创建目录
    def create_content(self):
        new_ct = os.path.join(self.copypath,self.nt)
        folder = os.path.exists(new_ct)
        if not folder:
            os.mkdir(new_ct)
            print("创建"+str(self.nt)+"文件夹成功")
        else:
            print("创建的文件夹已存在")
        return new_ct
    #备份文件
    def copy_file(self):
        c_dst = self.create_content()
        count = 0
        for i in self.read_fileall():
            src = os.path.join(self.filepath,i)
            dst = os.path.join(c_dst,i)
            copyfile(src,dst=dst)
            count+=1
        print("成功备份"+str(count)+"文件")
        return count
    #删除文件
    def del_file(self):
        count = 0
        for i in self.read_fileall():
            del_file = os.path.join(self.filepath, i)
            os.remove(del_file)
            count += 1
        print("成功删除" + str(count) + "文件")
    def run_del_file(self):
        if len(self.read_fileall())== self.copy_file():
            self.del_file()
        else:
            print("备份文件未成功")


if __name__ == '__main__':
    # data = BaseFile()
    # print(data.find_file('gpu.xls'))
    data = ConfigFile()
    data.run_del_file()