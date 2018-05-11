# multidatabaseDemo
  一个基于python的 多数据源demo，目前只支持mysql oracle，不过如果是clob的话还是需要特殊处理一下的；
  
  demo是从项目中提取出来的，我们的业务需要连接多个数据源对多个数据源的数据进行处理；
  
  我们mysql使用的包是pymysql,oracle使用的是cx_Oracle
  
  网上搜索没有好的解决方案，然后就基于sql预编译的方式自己写了个，其实核心就在于mysql跟oracle对预编译的支持；
   
  mysql的占位符采用%s,而参数是以tuple的格式
  
  ```python
      sqlStr = """select  * from test_table  where id = %s"""
      param = ('test')
      self.db_operation.execSqlStr(sqlStr, param)
  ```
  
  oracle的占位符是:1,:2这种，参数是以list的格式
  
  ```python
      sqlStr = """select  * from test_table  where id = :1"""
      param = ['test']
      self.db_operation.execSqlStr(sqlStr, param)
  ```
  
  我这边目前就只是根据数据库类型对sql,param进行转换，目前默认的写法是oracle的，因为oracle的这种方便正则匹配替换。。
