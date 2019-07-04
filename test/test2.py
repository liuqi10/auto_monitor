# coding: utf8
import threading
import time
import os, sys
import csv
from PIL import Image
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文

# 画图片
def draw_single_pic(y):
    timeValue = time.strftime('"%Y-%m-%d %H:%M:%S"', time.localtime(time.time()))
    print(timeValue)
    x_ = [x + 1 for x in range(len(y))]
    y_ = []
    for i in y:
        if i == ' ':
            y_.append(0)
        else:
            y_.append(float(i))
    plt.figure()
    plt.xlabel('time(10S)')
    plt.ylabel('cpu_D_vulue(G)')
    plt.title('cpu')
    plt.plot(x_, y_)

    plt.savefig("E:\\lib\\remote\\img.png")
    plt.show()

    return plt
# 真正要执行的函数
def getData():
    TotalVirtualMemory = 'wmic os get TotalVirtualMemorySize /format:value'
    FreeVirtualMemory = 'wmic os get FreeVirtualMemory /format:value'
    t = os.popen(TotalVirtualMemory, 'r', 1)
    f = os.popen(FreeVirtualMemory, 'r', 1)
    buffert = t.read()
    buffertf = f.read()

    # 打开文件，追加a
    out = open('E:\\lib\\remote\\memory.csv', 'a', newline='')
    # 设定写入模式
    csv_write = csv.writer(out, dialect='excel')
    # 写入具体内容
    tatal=f
    free=float(buffertf.split('=')[1][0:6])/1024/1024*10
    cha=tatal-free

    print(round(tatal, 2))
    print(round(free, 2))
    print(round(cha, 2))
    timeValue = time.strftime('"%Y-%m-%d %H:%M:%S"', time.localtime(time.time()))
    print(timeValue)
    csv_write.writerow([str(round(tatal, 2)), str(round(free, 2)), str(round(cha, 2)),str(timeValue)])
    print("write over")

    t.close()
    f.close()
#i<3600为监控一个小时 每隔S监测一次
def t2():
    i=0
    while i<limit:
        getData()
        time.sleep(10)
        i=i+10
#删除CSV文件
def del_files(path):
        for root, dirs, files in os.walk(path):
            for name in files:
                if '.csv' in name:
                    os.remove(os.path.join(root, name))
def makeRemote():
	pl = os.popen(r'D:\code\python1\makeRemote.bat')

def moveRemote():
	pl = os.popen(r'D:\code\python1\history_data.bat')

	buffer = pl.read()
	print (buffer)

if __name__ == '__main__':
    makeRemote()
    path = r'E:\lib'
    del_files(path)
    # i=3600为监控一个小时 limit为设定时间
    limit = 10800
    t = threading.Thread(target=t2)
    t.start()
    # 此处写你主线程要处理的事情.....
    t.join()

    with open('E:\\lib\\remote\\memory.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        column0 = [row[0] for row in reader]
    print(column0)
    with open('E:\\lib\\remote\\memory.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        column1= [row[1] for row in reader]
    print(column1)
    with open('E:\\lib\\remote\\memory.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        column2 = [row[2] for row in reader]
    print (column2)
    print("CPU最大值所在时间")
    print(column2.index(max(column2)) ) # 返回最大值
    print("CPU 的极大值为：")
    print(column2[column2.index(max(column2))])

    draw_single_pic(column2)
    moveRemote()


