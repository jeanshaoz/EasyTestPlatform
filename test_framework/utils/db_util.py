# test_framework/utils/db_util.py
import sqlite3
import os

# 获取数据库文件的绝对路径（处理路径兼容性问题）
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'test.db')


class DBUtil:
    """数据库操作工具类"""

    def __init__(self):
        # 连接到项目根目录下的 test.db
        self.conn = sqlite3.connect(DB_PATH)

    def query_one(self, sql):
        """执行查询语句，返回单条数据"""
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        # 记得关闭连接
        self.conn.close()
        return result

    # 进阶写法：支持 with 语句自动关闭连接
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()