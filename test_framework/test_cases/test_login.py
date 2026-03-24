# test_framework/test_cases/test_login.py
import pytest
import sys
import os

# 动态添加路径，确保能引用到 api 和 utils 模块
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.user_api import UserAPI
from utils.db_util import DBUtil


class TestLogin:
    """登录模块测试集"""

    def test_login_success(self):
        """测试登录成功场景"""
        # 1. 初始化 API 对象
        api = UserAPI()
        # 2. 调用登录接口
        response = api.login("admin", "123456")
        # 3. 断言 HTTP 状态码
        assert response.status_code == 200, f"状态码错误，实际为: {response.status_code}"
        # 4. 断言业务返回码
        result = response.json()
        assert result['code'] == 0, f"业务码错误，实际为: {result['code']}"
        # 5. 数据库断言（亮点！）
        # 验证数据库中确实存在该用户，且余额正确
        user_id = result['data']['user_id']
        with DBUtil() as db:
            db_result = db.query_one(f"SELECT balance FROM users WHERE id={user_id}")
        assert db_result is not None, "数据库中未找到该用户"
        assert db_result[0] == 100.0, f"用户余额不正确，实际为: {db_result[0]}"

    def test_login_fail_wrong_password(self):
        """测试密码错误场景"""
        api = UserAPI()
        response = api.login("admin", "wrong_password")
        # 断言返回 401 未授权
        assert response.status_code == 401
        assert response.json()['code'] == 1


# 调试模式：直接运行此文件时执行测试
if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_login.py"])