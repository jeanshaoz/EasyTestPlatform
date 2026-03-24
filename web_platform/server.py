# web_platform/server.py
from flask import Flask, render_template, jsonify
import subprocess
import os

app = Flask(__name__, template_folder='templates')


# 首页：展示控制面板
@app.route('/')
def index():
    return render_template('dashboard.html')


# API：触发测试执行
@app.route('/api/run_tests', methods=['POST'])
def run_tests():
    try:
        # 调用 pytest 命令
        # 注意：这里使用相对路径调用上一级目录的测试用例
        cmd = [
            "pytest",
            "../test_framework/test_cases/",
            "-v",
            "--alluredir=../reports"
        ]
        # 运行命令并捕获输出
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            cwd=os.path.dirname(os.path.abspath(__file__))  # 确保在当前目录执行
        )
        return jsonify({
            "status": "success",
            "output": result.stdout,
            "error": result.stderr,
            "return_code": result.returncode
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == '__main__':
    # 启动 Web 服务，端口 8080
    print("测试平台启动中：http://127.0.0.1:8080")
    app.run(debug=True, port=8080)