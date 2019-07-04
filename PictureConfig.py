#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import os
#生成可视化图标
from matplotlib import pyplot
#获取当前系统时间
from TimeConfig.config_time import ConfigTime
#获取基础配置信息
from base_config.read_base_config import ReadBaseConfig
class Picture():
    def __init__(self,mem_list,mem_title,ytarget,yheight,typename):
        #获取当前系统的时间
        base_time = ConfigTime()
        self.nowtime =base_time.gettime
        self.name = self.nowtime + typename+".png"
        #获取基础配置信息
        base_info = ReadBaseConfig()
        picture_filepath = base_info.get_filepath('picturepath')
        self.save_picture = os.path.join(picture_filepath,self.name)#保存生成报告图片的路径地址
        print(self.save_picture)
        self.mem_list = mem_list
        self.mem_title = mem_title
        self.ytarget = ytarget
        self.yheight = yheight
    #生成折线图函数，三个参数分别为数据列表，数据标题，纵坐标name
    def get_picture(self):
        x = []
        y = self.mem_list
        count = 0
        # mem_title = 'Memory total='+ str(memtotal)+'GB'
        for i in range(len(self.mem_list)):
            count +=10
            x.append(count)
        print("横坐标：",x)
        print("纵坐标：",y)
        # 生成图表
        # pyplot.plot(x,y,label='Frist line',linewidth=1,color='b',marker='o',markerfacecolor='red',markersize=6)
        pyplot.plot(x,y)
        # 设置横坐标为year，纵坐标为population，标题为Population year correspondence
        pyplot.xlabel(self.nowtime+'Time/(s)')
        pyplot.ylabel(self.ytarget)
        pyplot.title(self.mem_title)
        #设置折线图的横纵坐标取值范围,count表示横坐标取值范围，100表示纵坐标的取值范围
        pyplot.axis([0,count, 0, self.yheight])
        #保存生成的折线图
        pyplot.savefig(self.save_picture)
        #每次调用完关闭，防止二次调用未清空数据
        pyplot.close()
        print("图片生成成功")
        #显示图表
        # pyplot.show()