# setup_day2.py
import os

# 定义要创建的目录结构
dirs = [
    "test_framework",
    "test_framework/api",
    "test_framework/utils",
    "test_framework/test_cases",
    "reports"
]
# 定义要创建的文件及其内容
files_content = {
    "test_framework/api/user_api.py": '''# test_framework/api/user_api.py
import requests
BASE_URL = "http://127.0.0.1:5000"
class UserAPI:
    """用户相关接口封装"""
    def login(self, username, password):
        url = f"{BASE_URL}/api/login"
        payload = {"username": username, "password": password}
        return requests.post(url, json=payload)
    def get_balance(self, user_id):
        url = f"{BASE_URL}/api/balance/{user_id}"
        return requests.get(url)
''',
    "test_framework/utils/db_util.py": '''# test_framework/utils/db_util.py
import sqlite3
import os
# 智能定位数据库路径
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'test.db')
class DBUtil:
    """数据库操作工具类"""
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
    def query_one(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        self.conn.close()
        return result
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
''',
    "test_framework/test_cases/test_login.py": '''# test_framework/test_cases/test_login.py
import pytest
import sys
import os
# 动态添加路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.user_api import UserAPI
from utils.db_util import DBUtil
class TestLogin:
    """登录模块测试集"""
    def test_login_success(self):
        """测试登录成功场景"""
        api = UserAPI()
        response = api.login("admin", "123456")
        # 断言 HTTP 状态码
        assert response.status_code == 200
        # 断言业务返回码
        result = response.json()
        assert result['code'] == 0
        # 数据库断言
        user_id = result['data']['user_id']
        with DBUtil() as db:
            db_result = db.query_one(f"SELECT balance FROM users WHERE id={user_id}")
        assert db_result is not None
        assert db_result[0] == 100.0
    def test_login_fail_wrong_password(self):
        """测试密码错误场景"""
        api = UserAPI()
        response = api.login("admin", "wrong_password")
        assert response.status_code == 401
        assert response.json()['code'] == 1
if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_login.py"])
'''
}


def create_structure():
    print("开始生成目录结构...")
    # 创建文件夹
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"创建文件夹: {d}")
    print("\n开始生成文件...")
    # 创建文件并写入内容
    for file_path, content in files_content.items():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"创建文件: {file_path}")
    print("\nDay 2 结构生成完毕！")


if __name__ == "__main__":
    create_structure()