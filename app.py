# app.py
from flask import Flask, request, jsonify
import sqlite3
import time

app = Flask(__name__)


# 初始化数据库函数
def init_db():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    # 创建用户表
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  username TEXT, 
                  password TEXT, 
                  balance REAL)''')
    # 插入一条默认测试数据
    try:
        c.execute("INSERT INTO users (username, password, balance) VALUES ('admin', '123456', 100.0)")
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # 数据已存在，忽略
    finally:
        conn.close()


@app.route('/api/login', methods=['POST'])
def login():
    """模拟登录接口"""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    # 模拟一点业务耗时
    time.sleep(0.1)
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    if result:
        return jsonify({"code": 0, "msg": "Login success", "data": {"user_id": result[0]}})
    else:
        return jsonify({"code": 1, "msg": "User or password error"}), 401


@app.route('/api/balance/<int:user_id>', methods=['GET'])
def get_balance(user_id):
    """模拟查询余额接口"""
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("SELECT balance FROM users WHERE id=?", (user_id,))
    result = c.fetchone()
    conn.close()
    if result:
        return jsonify({"code": 0, "data": {"balance": result[0]}})
    else:
        return jsonify({"code": 1, "msg": "User not found"}), 404


if __name__ == '__main__':
    print("正在初始化数据库...")
    init_db()
    print("服务启动中，请访问 http://127.0.0.1:5000")
    # 启动服务
    app.run(debug=True, port=5000)