# coding:utf-8
import datetime
import json
import sys

import cx_Oracle

from config import db_config
from db.conn_client import DBConnectionClient
from db.db_client import *
from init import db_init_client

reload(sys)
sys.setdefaultencoding('utf-8')


class InforMationMain(object):

    # 主程序数据源连接
    target_con, target_cur = 0, 0

    db_operation  = 0
    def main(self):

        # 获取数据源库连接
        self.target_con, self.target_cur = DBConnectionClient(db_config.target_dbConfig).getConnection()
        # 获取操作对象
        self.db_operation = DbOperationFactory().createOperation(int(db_config.target_dbConfig['db_type']),
                                                                 self.target_con, self.target_cur)
        # 初始化创建表
        db_init_client.initConfigTable(self.target_cur, db_config.target_dbConfig)

        self.__create()
        self._query()
        self.__update()
        self._query()
        self.__del()
        self._query()



    def __create(self):

        json_summary = "testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttest"
        content = "大字段！！！！！！！！！！！！！！！！！！！！！"
        sqlStr = """
                      insert into test_table(id, summary, content, createtime) values (:1,:2,:3,:4)
                    """
        json_content = json.dumps(content, ensure_ascii=False)
        # oracle的才需要这样做 mysql的话就不需要
        # raw_content = self.target_cur.var(cx_Oracle.CLOB)
        # raw_content.setvalue(0, json_content.encode('utf-8'))
        param = ['test', json_summary, json_content, datetime.datetime.now()]
        self.db_operation.execSqlStr(sqlStr, param)
        self.target_con.commit()
        pass

    def __update(self):
        sqlStr = """
                  update test_table set content = :1 where id = :2
                  """

        content = "修改后的大字段！！！！！！！！！！！！！！！！！！！！！"
        json_content = json.dumps(content, ensure_ascii=False)
        # raw_content = self.target_cur.var(cx_Oracle.CLOB)
        # raw_content.setvalue(0, json_content.encode('utf-8'))
        param = [json_content, 'test']
        self.db_operation.execSqlStr(sqlStr, param)
        self.target_con.commit()
        pass

    def __del(self):
        sqlStr = """ delete from test_table  where id = :1  """
        param = ['test']
        self.db_operation.execSqlStr(sqlStr, param)
        self.target_con.commit()
        pass

    def _query(self):
        sqlStr = """select  * from test_table  where id = :1"""
        param = ['test']
        self.db_operation.execSqlStr(sqlStr, param)
        print self.target_cur.fetchmany()
        pass


    def _query(self):
        sqlStr = """select  * from test_table  where id = %s"""
        param = ('test')
        self.db_operation.execSqlStr(sqlStr, param)
        print self.target_cur.fetchmany()
        pass


if __name__ == '__main__':
    InforMationMain().main()

    pass
