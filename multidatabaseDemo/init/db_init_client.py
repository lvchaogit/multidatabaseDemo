# coding:utf-8
import sys

from constants import *
from mysql_client import MysqlClient
from oracle_client import OracleClient

reload(sys)
sys.setdefaultencoding('utf-8')


# 初始化配置表
def initConfigTable(target_cur, db_config):
    dbType = int(db_config['db_type'])
    dbSid = db_config['db_sid']
    if dbType == DB_TYPE_ORACLE:
        OracleClient().initConfigTable(target_cur)
    elif dbType == DB_TYPE_MYSQL:
        MysqlClient().initConfigTable(target_cur, dbSid)
    elif dbType == DB_TYPE_MSSQL:
        pass



if __name__ == '__main__':
    # conn, cur = get_connection(db_config.targetMysql_dbConfig)
 
    pass
