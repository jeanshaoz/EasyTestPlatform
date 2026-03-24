# monitor.py (系统资源监控工具)
import psutil
import time
import threading


class SystemMonitor:
    def __init__(self):
        self.is_running = False
        self.metrics = []  # 存放监控数据的列表

    def start(self):
        """启动监控线程"""
        self.is_running = True
        # 开启一个守护线程，主程序结束它会自动关闭
        t = threading.Thread(target=self._collect)
        t.daemon = True
        t.start()

    def _collect(self):
        """采集数据的具体逻辑"""
        while self.is_running:
            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory().percent
            # 记录数据
            self.metrics.append({"cpu": cpu, "memory": memory})
            # 可选：打印到控制台实时观察
            print(f"[Monitor] CPU: {cpu}% | Memory: {memory}%")

    def stop(self):
        """停止监控并返回数据"""
        self.is_running = False
        return self.metrics


# 使用示例（调试用）
if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.start()
    time.sleep(5)  # 模拟运行5秒
    data = monitor.stop()
    print(f"采集到 {len(data)} 条数据")