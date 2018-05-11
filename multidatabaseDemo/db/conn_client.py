# coding:utf-8


import logging

import cx_Oracle
# import MySQLdb.cursors
import pymysql

from constants import *


# 获取数据库连接类
class DBConnectionClient(object):

    def __init__(self, configStr):
        self.configStr = configStr

    # 返回配置的数据源连接
    def getConnection(self):
        # 如果是tuple类型，则进行组装成字典类型
        if isinstance(self.configStr, tuple):
            self.configStr = self.__getConnConfigByTuple()
        try:
            type = int(self.configStr['db_type'])
            if type == DB_TYPE_MYSQL:
                return self.__get_MysqlConnection()
            elif type == DB_TYPE_ORACLE:
                return self.__get_OralceSqlConnection()
            elif type == DB_TYPE_MSSQL:
                pass
        except Exception as e:
            logging.error("获取数据库连接失败——参数:%s;%s" % (str(self.configStr),str(e)))
        pass

    # 根据数据库返回的值拼装成对象
    def __getConnConfigByTuple(self):
        return {
            'db_host': self.configStr[3].encode("utf-8"),
            'db_port': self.configStr[4],
            'db_username': self.configStr[5].encode("utf-8"),
            'db_password': self.configStr[6].encode("utf-8"),
            'db_sid': self.configStr[2].encode("utf-8"),
            # 1-Oracle 2-mysql 3-sqlserver
            'db_type': self.configStr[1]
        }

    # 返回mysql 数据库连接
    def __get_MysqlConnection(self):
        conn = pymysql.connect(
            host=self.configStr['db_host'],
            port=int(self.configStr['db_port']),
            user=self.configStr['db_username'],
            passwd=self.configStr['db_password'],
            db=self.configStr['db_sid'],
            charset='utf8mb4',
        )

        cur = conn.cursor()

        return conn, cur

    # 返回oracle 数据库连接
    def __get_OralceSqlConnection(self):

        conn_uri = '%s/%s@%s:%s/%s' % (self.configStr['db_username'], self.configStr['db_password'],
                                       self.configStr['db_host'], int(self.configStr['db_port']),
                                       self.configStr['db_sid'])
        conn = cx_Oracle.connect(conn_uri)

        cur = conn.cursor()

        return conn, cur

    # 返回mssql 数据库连接
    def __get_MsSqlConnection(self):
        conn = pymysql.connect(
            host=self.configStr['db_host'],
            port=int(self.configStr['db_port']),
            user=self.configStr['db_username'],
            passwd=self.configStr['db_password'],
            db=self.configStr['db_sid'],
            charset='utf8',
        )

        cur = conn.cursor()

        return conn, cur
