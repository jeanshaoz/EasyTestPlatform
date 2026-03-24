	// Jenkinsfile (声明式流水线)
	pipeline {
	    // 定义在任何可用代理上运行
	    agent any
	    // 定义环境变量，方便后续使用
	    environment {
	        PYTHON_PATH = 'python' // 或你的 python 绝对路径
	    }
	    stages {
	        stage('1. 代码检查与依赖安装') {
	            steps {
	                echo '>>> 正在检查代码并安装依赖...'
	                // 在真实 Jenkins 中，这里通常是 sh 'pip install -r requirements.txt'
	                // 这里模拟打印日志
	                script {
	                    println "模拟：安装 Flask, Pytest, Allure 依赖完成"
	                }
	            }
	        }
	        stage('2. 部署测试环境') {
	            steps {
	                echo '>>> 正在启动被测服务...'
	                // 实际生产中，通常使用 Docker 或 Shell 脚本后台启动
	                script {
	                    // 模拟启动命令：python app.py &
	                    // 注意：Jenkinsfile 中直接运行 app.py 会挂起，实际需用 nohup 或 Docker
	                    println "模拟：服务已启动在 http://127.0.0.1:5000"
	                }
	            }
	        }
	        stage('3. 执行自动化测试') {
	            steps {
	                echo '>>> 正在执行 Pytest 测试套件...'
	                script {
	                    // 真实命令：sh 'pytest test_framework/test_cases/ -v --alluredir=reports'
	                    println "模拟：正在运行 500 条测试用例..."
	                }
	            }
	        }
	        stage('4. 生成测试报告') {
	            steps {
	                echo '>>> 测试执行完毕，发布 Allure 报告...'
	                // allure include results...
	            }
	        }
	    }
	    // 后置处理：失败时的动作
	    post {
	        failure {
	            echo '❌ 测试失败！已发送邮件/钉钉通知，禁止部署上线！'
	            // 在这里配置邮件或钉钉机器人通知
	        }
	        success {
	            echo '✅ 测试通过！允许合并代码。'
	        }
	    }
	}