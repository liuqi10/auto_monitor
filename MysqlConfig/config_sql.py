#-*- coding:utf-8 -*-
import pymysql
from  BaseConfig.read_base_config import ReadBaseConfig

class ConfigMysql():
    def __init__(self):
        basedata = ReadBaseConfig()
        self.host = basedata.get_db('host')
        self.username = basedata.get_db('username')
        self.password = basedata.get_db('password')
        self.port = basedata.get_db('port')
        self.dbname = basedata.get_db('database')
    #连接数据库
    def connectmysql(self):
        # 链接数据库
        connect = pymysql.connect(self.host,self.username,self.password,self.dbname, charset='utf8')
        return connect
    #读取数据库内容
    def readmysql(self,sql):
        # 链接数据库
        conn = self.connectmysql()
        # 获取操作游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 使用execute执行sql语句
        cursor.execute(sql)
        # 获取数据
        data = cursor.fetchall()
        return data
        # 关闭数据库链接
        conn.close()
    #插入数据内容
    def insertmysql(self,sql):
        # 链接数据库
        conn = self.connectmysql()
        # 获取操作游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # SQL 插入语句
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            #遇到错误时回滚
            conn.rollback()
        # 关闭数据库连接
        conn.close()
    # 更新数据库表数据
    def updatemysql(self,sql):
        # 链接数据库
        conn = self.connectmysql()
        # 获取操作游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # SQL 插入语句
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 发生错误时回滚
            conn.rollback()
        # 关闭数据库链接
        conn.close()
    def run(self):
        print(self.host)

# if __name__ == '__main__':
#     sql = """INSERT INTO version_manage(storage_path,type_id) VALUES ('testfile/mirror/XMind_18@185497.exe',100)"""
#     con = ConfigMysql()
#     con.insertmysql(sql)
#       mysql = ConfigMysql()
#       sql = """select * from version_manage"""
#       data = mysql.readmysql(sql)
#       print(data)



