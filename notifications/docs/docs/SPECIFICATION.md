# Спецификация модулей

## 1. Core Module

### 1.1 ResourceMonitor

Входные данные:

# Аргументы конструктора:
- update_interval: int = 1 # Интервал обновления метрик в секундах
- config_path: Optional[str] # Путь к файлу конфигурации (JSON/YAML)

# Аргументы метода start_monitoring:
- None # Запуск мониторинга ресурсов

# Аргументы метода stop_monitoring:
- None # Остановка мониторинга

# Аргументы метода get_current_stats:
- None # Получение текущих метрик ресурсов

# Аргументы метода set_thresholds:
- cpu_threshold: Optional[float] # Порог загрузки CPU (%)
- memory_threshold: Optional[float] # Порог использования памяти (%)
- disk_threshold: Optional[float] # Порог заполнения диска (%)

Выходные данные:

# Возвращаемые значения:
- Dict[str, Any] # Текущие метрики системы (CPU, RAM, Disk, Network)
- None # Для методов start_monitoring, stop_monitoring, set_thresholds

# Исключения:
- ValueError # Некорректные значения порогов
- RuntimeError # Ошибка запуска мониторинга
- PermissionError # Недостаточно прав для доступа к системным метрикам
- FileNotFoundError # Файл конфигурации не найден

Side effects:
- Инициализация экземпляров MetricCollector, Analyzer и NotificationManager
- Запуск фонового цикла мониторинга
- Чтение системных метрик через psutil
- Логирование всех операций мониторинга
- Потребление системных ресурсов (CPU, память)
- Возможная генерация уведомлений при превышении порогов

... и так далее, остальные модули по аналогии из отчета.
