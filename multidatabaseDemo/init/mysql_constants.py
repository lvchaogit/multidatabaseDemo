# coding:utf-8


TABLE_NAME = 'test_table'
CREATE_TABLE_SQL = """
CREATE TABLE `test_table`  (
  `id` varchar(42) NOT NULL ,
  `summary` varchar(4000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL ,
  `content` longblob NULL ,
  `createtime` timestamp NULL DEFAULT CURRENT_TIMESTAMP 
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

"""


MYSQL_TABLE_TO_CREATE_SQL_MAP = {
    TABLE_NAME: CREATE_TABLE_SQL
}
