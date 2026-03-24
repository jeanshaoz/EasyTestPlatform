# test_framework/conftest.py
import pytest
import sys
import os

# 引入根目录下的 monitor.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from monitor import SystemMonitor


@pytest.fixture(scope="session", autouse=True)
def setup_monitor():
    """
    Session 级别的 Hook，整个测试会话只执行一次。
    autouse=True 表示自动应用，无需在用例中显式调用。
    """
    monitor = SystemMonitor()
    print("\n>>> 启动性能监控守护线程...")
    monitor.start()
    yield  # 这里是测试执行的地方
    print("\n>>> 测试结束，停止监控...")
    data = monitor.stop()
    # 计算平均资源使用率并输出
    if data:
        avg_cpu = sum([d['cpu'] for d in data]) / len(data)
        avg_mem = sum([d['memory'] for d in data]) / len(data)
        print(f"\n===== 性能监控报告 =====")
        print(f"采集样本数: {len(data)}")
        print(f"平均 CPU: {avg_cpu:.2f}%")
        print(f"平均 内存: {avg_mem:.2f}%")
        print(f"=========================")