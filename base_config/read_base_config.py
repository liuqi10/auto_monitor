#-*- coding:utf-8 -*-
import configparser
import os
#读取config.ini配置文件的配置数据
class ReadBaseConfig():
    def __init__(self):
        #获取当前目录所在路径
        proDir = os.path.split(os.path.realpath(__file__))[0]#获取当前的绝对路径
        configPath = os.path.join(proDir, "config.ini") #输出文档路径
        self.config_path = os.path.abspath(configPath) #返回规范化的绝对路径
        # self.config_path = os.path.join(self.get_base_path, self.get_config_filename) #输出config.ini基础路径
        #读取config.ini基础路径内容
        self.cf = configparser.ConfigParser()
        self.cf.read(self.config_path,encoding='UTF-8')#获取配置文件数据内容，注意字符编码格式
        # self.cf.read(r'D:\python_auto\base_config\config.ini',encoding='UTF-8')#获取配置文件数据内容，注意字符编码格式
    #获取数据库基础配置信息
    def get_db(self,name):
        value = self.cf.get("DB",name)
        return value
    #获取发送邮件的基础数据信息
    def get_smtp(self,name):
        value = self.cf.get("SMTP",name)
        return value
    def get_casepath(self,name):
        value = self.cf.get("CASE_PATH",name)
        return value
    #获取登录的账号信息
    def get_login(self,name):
        value = self.cf.get("LOGIN",name)
        return value
    #获取接口的URL和参数配置信息
    def get_http(self,name):
        value = self.cf.get("HTTP",name)
        return value
    #获取存储报告的基础路径
    def get_filepath(self,name):
        value = self.cf.get("FILE_PATH",name)
        return value
    # 获取参数化文档路径
    def get_excel_filepath(self, name):
        value = self.cf.get("CONFIG_EXCEL_PATH", name)
        return value
    # 获取设定监控性能的时间参数
    def get_monitor_time(self, name):
        value = self.cf.get("CASE_MONITOR_TIME", name)
        return value

if __name__ == "__main__":
    # data = ReadBaseConfig()
    # name = data.get_reportpath('reportpath')
    # print(data.config_path)
    # print(name)
    pass