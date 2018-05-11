# coding:utf-8
import logging
import sys

from oracle_constants import *

reload(sys)
sys.setdefaultencoding('utf-8')


class OracleClient(object):

    # 检查表是否存在
    def __check_table_exists(self, cur, table_name):
        sql = """select * from user_tables t where t.table_name  =:1"""
        try:

            param = [table_name.upper()]
            count = cur.execute(sql, param)
            return count.rowcount > 0
        except Exception as e:
            logging.error("Exception: %s" % e)
            return False
        pass

    # 创建表
    def __create_table_if_not_exist(self, cur, table_name, create_table_sql):
        if not self.__check_table_exists(cur, table_name):
            try:
                logging.info("Oracle table %s not exist, now create it." % table_name)
                cur.execute(create_table_sql)
                # 创建索引
                self.__initIndex(cur, table_name)
                logging.info("Oracle table %s  created" % table_name)
            except Exception as e:
                logging.error("Exception: %s,sqlStr:%s" % (e, create_table_sql))
        pass

    # 初始化 配置表
    def initConfigTable(self, target_cur):
        # 创建配置表
        for table, createSql in ORACLE_TABLE_TO_CREATE_SQL_MAP.items():
            self.__create_table_if_not_exist(target_cur, table, createSql)

    def __initIndex(self, cur, table_name):

        indexStr = ORACLE_INDEX_TO_CREATE_SQL_MAP.get(table_name)
        # 创建索引
        if indexStr is not None:
            cur.execute(indexStr)


if __name__ == '__main__':
    # conn, cur = get_connection(db_config.targetMysql_dbConfig)
    #
    # data = cur.execute("""desc t_stock_dict""")
    # result = cur.fetchone()
    #
    # result = check_table_exists(cur, 't_stock_dict')
    # result = check_table_exists(cur, 'tt')
    #
    # conn.commit()
    # cur.close()
    # conn.close()
    pass
