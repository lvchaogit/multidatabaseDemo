# coding:utf-8
import logging
import sys

from mysql_constants import *

reload(sys)
sys.setdefaultencoding('utf-8')


class MysqlClient(object):

    # 检查表是否存在
    def __check_table_exists(self, cur, table_name, sid):
        sql = """
              SELECT table_name FROM information_schema.TABLES WHERE table_schema=%s and table_name =%s
              """
        try:
            param = (sid, table_name)
            count = cur.execute(sql, param)
            return count > 0
        except Exception as e:
            logging.error("Exception: %s" % e)
            return False
        pass

    # 创建表
    def __create_table_if_not_exist(self, cur, table_name, create_table_sql, sid):
        if not self.__check_table_exists(cur, table_name, sid):
            try:
                logging.info("MySQL table %s not exist, now create it." % table_name)
                cur.execute(create_table_sql)
                logging.info("MySQL table %s  created" % table_name)
            except Exception as e:
                logging.error("Exception: %s" % e)
        pass

    # 初始化 配置表
    def initConfigTable(self, target_cur, sid):
        # 创建配置表
        for table, createSql in MYSQL_TABLE_TO_CREATE_SQL_MAP.items():
            self.__create_table_if_not_exist(target_cur, table, createSql, sid)



if __name__ == '__main__':

    # conn.close()
    pass
