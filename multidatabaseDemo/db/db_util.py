# coding:utf-8
import re
from cx_Oracle import Connection

###兼容处理类 用于针对不同类型的数据库的格式转换

# 返回兼容的条件
def getCompatibleParam(conn, paramList):
    # oracle操作 暂时
    if isinstance(conn, Connection):
        return paramList
    else:
        return tuple(paramList)


# 返回兼容的SQL
def getCompatibleSql(conn, sqlStr):
    if isinstance(conn, Connection):
        return sqlStr
    else:
        return re.sub(r':\d+', '%s', sqlStr)
