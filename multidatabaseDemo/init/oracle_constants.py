# coding:utf-8


# 新闻code
TABLE_NAME = 'test_table'
CREATE_TABLE_SQL = """
    CREATE TABLE test_table (
      id VARCHAR2(42) NOT NULL ,
      summary VARCHAR2(4000) ,
      content clob,
      createtime TIMESTAMP(6) 
     )
"""
# 创建索引 oracle方式
CREATE_TABLE_INDEX = """
  CREATE INDEX index_test_table ON test_table (id)
"""


# 创建新闻表语句
ORACLE_TABLE_TO_CREATE_SQL_MAP = {
    TABLE_NAME: CREATE_TABLE_SQL,

}

# 创建索引
ORACLE_INDEX_TO_CREATE_SQL_MAP = {
    TABLE_NAME: CREATE_TABLE_INDEX
}
