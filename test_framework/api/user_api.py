# test_framework/api/user_api.py
import requests

BASE_URL = "http://127.0.0.1:5000"


class UserAPI:
    """用户相关接口封装"""

    def login(self, username, password):
        """
        登录接口
        :param username: 用户名
        :param password: 密码
        :return: Response 对象
        """
        url = f"{BASE_URL}/api/login"
        payload = {
            "username": username,
            "password": password
        }
        # 发送 post 请求
        return requests.post(url, json=payload)

    def get_balance(self, user_id):
        """
        查询余额接口
        :param user_id: 用户ID
        :return: Response 对象
        """
        url = f"{BASE_URL}/api/balance/{user_id}"
        return requests.get(url)