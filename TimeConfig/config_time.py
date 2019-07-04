#-*- coding:utf-8 -*-
import time

class ConfigTime(object):
    @property
    def gettime(self):
        #简单可读形式
        datatime1 = time.asctime(time.localtime(time.time()))
        #格式化时间
        datatime = time.strftime("%Y-%m-%d_%H%M%S",time.localtime(time.time()))
        return datatime
if __name__ == "__main__":
    dt = ConfigTime()
    while(True):
        print(dt.gettime)
        time.sleep(1)