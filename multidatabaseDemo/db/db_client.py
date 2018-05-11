# coding:utf-8
import logging
import re

from constants import *


# 数据库操作抽象类
class DbOperation(object):

    def __init__(self, conn, cur):
        self.conn = conn
        self.cur = cur
        pass

    # 执行数据库方法
    def execSqlStr(self, sqlStr, paramList):
        pass


# mysql数据库操作类
class MysqlClient(DbOperation):

    # 执行数据库方法
    def execSqlStr(self, sqlStr, paramList):
        compatibleSql = re.sub(r':\d+', '%s', sqlStr)
        compatibleParam = tuple(paramList)
        try:
            self.cur.execute(compatibleSql, compatibleParam)
        except Exception as e:
            logging.error("Mysql执行SQL异常:%s,参数%s;信息：%s" % (str(compatibleSql), str(compatibleParam), str(e)))


# mysql数据库操作类
class OracleClient(DbOperation):

    # 执行数据库方法
    def execSqlStr(self, sqlStr, paramList):

        try:
            self.cur.execute(sqlStr, paramList)
        except Exception as e:
            logging.error("Oracle执行SQL异常:%s,参数%s;信息：%s" % (str(sqlStr), str(paramList), str(e)))


# 数据源操作工厂类
class DbOperationFactory(object):

    # 创建数据库操作类
    @staticmethod
    def createOperation(type, conn, cur):
        if type == DB_TYPE_MYSQL:
            return MysqlClient(conn, cur)
        elif type == DB_TYPE_ORACLE:
            return OracleClient(conn, cur)
        else:
            return DbOperation(conn, cur)
