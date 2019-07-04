#-*- coding:utf-8 -*-
from MysqlConfig.config_sql import ConfigMysql

class BaseSql(object):
    def __init__(self):
        self.mysql = ConfigMysql()
    def ftpsql(self,i):
        sql = "insert into version_manage (storage_path,type_id) values ('%s',100) " % (i)
        self.mysql.insertmysql(sql)
    def countsql(self,a,b,c,d,e,f):
        sql = "insert into monitor (IP,memory_percent,cpu_percent,disk_percent,net_sent_count,net_recv_count,create_time) values ('%s','%s','%s','%s','%s','%s',NOW()) " % (a,b,c,d,e,f)
        self.mysql.insertmysql(sql)
        print(a,b,c,d,e,f)
if __name__ == "__main__":
    bs = BaseSql()
    bs.countsql()

