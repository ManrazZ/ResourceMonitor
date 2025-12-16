import psutil


class MetricCollector:
    """
    Класс для сбора метрик системы.
    """
    def collect_cpu(self):
        """Сбор метрик CPU."""
        return psutil.cpu_percent(interval=1)

    def collect_memory(self):
        """Сбор метрик памяти."""
        memory = psutil.virtual_memory()
        return {
            'percent': memory.percent,
            'total': memory.total,
            'available': memory.available,
            'used': memory.used
        }

    def collect_disk(self, path='/'):
        """Сбор метрик диска."""
        disk = psutil.disk_usage(path)
        return {
            'percent': disk.percent,
            'total': disk.total,
            'used': disk.used,
            'free': disk.free
        }

    def collect_network(self):
        """Сбор сетевых метрик."""
        net_io = psutil.net_io_counters()
        return {
            'bytes_sent': net_io.bytes_sent,
            'bytes_recv': net_io.bytes_recv,
            'packets_sent': net_io.packets_sent,
            'packets_recv': net_io.packets_recv
        }

    def collect_all(self):
        """Сбор всех метрик."""
        return {
            'cpu': self.collect_cpu(),
            'memory': self.collect_memory(),
            'disk': self.collect_disk(),
            'network': self.collect_network()
        }
