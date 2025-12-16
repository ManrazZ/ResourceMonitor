import psutil
import time
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import threading


class MetricsCollector:
    def collect(self):
        return {
            "cpu": psutil.cpu_percent(interval=1),
            "memory": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage("/").percent
        }


class ResourceMonitorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("System Metrics Monitor")
        self.root.geometry("500x350")

        self.collector = MetricsCollector()
        self.running = False
        self.monitor_thread = None

        self.setup_ui()

    def setup_ui(self):

        header_label = ttk.Label(
            self.root,
            text="System Resources Monitor",
            font=("Arial", 16, "bold")
        )
        header_label.pack(pady=10)

        metrics_frame = ttk.Frame(self.root, padding=20)
        metrics_frame.pack(fill="both", expand=True)

        # CPU метрика
        cpu_frame = ttk.LabelFrame(metrics_frame, text="CPU Usage", padding=15)
        cpu_frame.pack(fill="x", pady=10)

        self.cpu_label = ttk.Label(cpu_frame, text="0%", font=("Arial", 24))
        self.cpu_label.pack()

        self.cpu_progress = ttk.Progressbar(cpu_frame, length=400, mode='determinate')
        self.cpu_progress.pack(fill="x", pady=5)

        # Memory метрика
        memory_frame = ttk.LabelFrame(metrics_frame, text="Memory Usage", padding=15)
        memory_frame.pack(fill="x", pady=10)

        self.memory_label = ttk.Label(memory_frame, text="0%", font=("Arial", 24))
        self.memory_label.pack()

        self.memory_progress = ttk.Progressbar(memory_frame, length=400, mode='determinate')
        self.memory_progress.pack(fill="x", pady=5)

        # Disk метрика
        disk_frame = ttk.LabelFrame(metrics_frame, text="Disk Usage", padding=15)
        disk_frame.pack(fill="x", pady=10)

        self.disk_label = ttk.Label(disk_frame, text="0%", font=("Arial", 24))
        self.disk_label.pack()

        self.disk_progress = ttk.Progressbar(disk_frame, length=400, mode='determinate')
        self.disk_progress.pack(fill="x", pady=5)

        control_frame = ttk.Frame(self.root, padding=10)
        control_frame.pack(fill="x")

        self.start_button = ttk.Button(
            control_frame,
            text="Start Monitoring",
            command=self.start_monitoring,
            width=15
        )
        self.start_button.pack(side="left", padx=5)

        self.stop_button = ttk.Button(
            control_frame,
            text="Stop Monitoring",
            command=self.stop_monitoring,
            state="disabled",
            width=15
        )
        self.stop_button.pack(side="left", padx=5)

        self.update_label = ttk.Label(control_frame, text="Last update: -")
        self.update_label.pack(side="right", padx=10)

    def update_metrics_display(self, metrics):

        self.cpu_label.config(text=f"{metrics['cpu']:.1f}%")
        self.cpu_progress['value'] = metrics['cpu']

        self.memory_label.config(text=f"{metrics['memory']:.1f}%")
        self.memory_progress['value'] = metrics['memory']

        self.disk_label.config(text=f"{metrics['disk']:.1f}%")
        self.disk_progress['value'] = metrics['disk']

        self.update_progress_color(self.cpu_progress, metrics['cpu'])
        self.update_progress_color(self.memory_progress, metrics['memory'])
        self.update_progress_color(self.disk_progress, metrics['disk'])

        current_time = datetime.now().strftime("%H:%M:%S")
        self.update_label.config(text=f"Last update: {current_time}")

    def update_progress_color(self, progress_bar, value):
        """Изменяет цвет прогресс-бара в зависимости от значения"""
        if value > 80:
            progress_bar.configure(style="Red.Horizontal.TProgressbar")
        elif value > 60:
            progress_bar.configure(style="Yellow.Horizontal.TProgressbar")
        else:
            progress_bar.configure(style="Green.Horizontal.TProgressbar")

    def monitoring_loop(self):
        while self.running:
            try:
                metrics = self.collector.collect()

                self.root.after(0, self.update_metrics_display, metrics)

                time.sleep(2)
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(2)

    def start_monitoring(self):
        if not self.running:
            self.running = True
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")

            self.monitor_thread = threading.Thread(target=self.monitoring_loop, daemon=True)
            self.monitor_thread.start()

    def stop_monitoring(self):
        if self.running:
            self.running = False
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")

            if self.monitor_thread:
                self.monitor_thread.join(timeout=1)

    def on_closing(self):
        """Обработка закрытия окна"""
        self.stop_monitoring()
        self.root.destroy()

    def run(self):

        style = ttk.Style()
        style.configure("Green.Horizontal.TProgressbar", troughcolor='light gray', background='green')
        style.configure("Yellow.Horizontal.TProgressbar", troughcolor='light gray', background='orange')
        style.configure("Red.Horizontal.TProgressbar", troughcolor='light gray', background='red')

        self.cpu_progress.configure(style="Green.Horizontal.TProgressbar")
        self.memory_progress.configure(style="Green.Horizontal.TProgressbar")
        self.disk_progress.configure(style="Green.Horizontal.TProgressbar")

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()


if __name__ == "__main__":
    app = ResourceMonitorGUI()
    app.run()
