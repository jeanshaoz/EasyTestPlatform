	# 🚀 EasyTest - 一站式自动化测试与性能监控平台
	<div align="center">
	  ![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
	  ![Pytest](https://img.shields.io/badge/Pytest-7.x-green.svg)
	  ![Flask](https://img.shields.io/badge/Flask-2.x-white.svg)
	  ![License](https://img.shields.io/badge/License-MIT-yellow.svg)
	  **基于 Python + Flask + Pytest 构建的轻量级测试开发平台**
	  [特性](#-核心特性) • [快速开始](#-快速开始) • [架构设计](#-项目架构) • [文档](#-文档)
	</div>
	---
	## 📖 项目简介
	**EasyTest** 是一个结合了**接口自动化测试**、**数据库断言**、**实时性能监控**与 **Web 可视化管理**的综合性测试平台。
	项目旨在解决传统测试过程中“功能与性能分离”、“执行入口分散”、“数据一致性难以校验”的痛点。通过集成多线程监控与 CI/CD 流水线，实现了从代码提交到测试报告生成的全流程自动化。
	> 💡 **亮点**：本平台创新性地将 `psutil` 系统监控集成至 Pytest Hook 中，实现了“边做功能测试，边看系统资源”，有效识别内存泄漏与 CPU 飙升等隐性 Bug。
	---
	## ✨ 核心特性
	| 模块 | 功能描述 | 技术实现 |
	| :--- | :--- | :--- |
	| **🤖 自动化测试** | 基于 Session/Cookie 的接口自动化，支持多环境配置 | `Requests`, `Pytest` |
	| **🗄️ 数据校验** | 接口响应与数据库落库的双重断言，确保数据一致性 | `SQLite3/MySQL`, `SQLAlchemy` |
	| **📊 性能监控** | 测试执行过程中实时采集 CPU/内存，生成性能趋势报告 | `Psutil`, `Threading` |
	| **🖥️ Web 管理台** | 简洁的 Web 界面，支持远程触发测试并实时查看日志 | `Flask`, `Axios` |
	| **🔄 CI/CD 集成** | 模拟 Jenkins 流水线，支持代码提交后的自动构建与测试 | `Jenkinsfile`, `PowerShell` |
	---
	## 🚀 快速开始
	### 环境要求
	*   Python 3.8+
	*   pip
	### 1️⃣ 获取项目
	```bash
	git clone https://github.com/your-username/EasyTestPlatform.git
	cd EasyTestPlatform