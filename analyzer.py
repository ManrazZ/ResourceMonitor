class Analyzer:
    """
    Класс для анализа метрик и сравнения с пороговыми значениями.
    """
    def __init__(self, thresholds):
        self.thresholds = thresholds

    def analyze(self, metrics):
        """
        Анализ метрик на превышение порогов.

        :param metrics: словарь с метриками
        :return: словарь с флагами превышения для каждой метрики
        """
        alerts = {}
        # Проверяем CPU
        if 'cpu' in self.thresholds and 'cpu' in metrics:
            alerts['cpu'] = metrics['cpu'] > self.thresholds['cpu']
        # Проверяем память
        if 'memory' in self.thresholds and 'memory' in metrics:
            # предполагаем, что metrics['memory'] - это словарь, и берем percent
            if isinstance(metrics['memory'], dict) and 'percent' in metrics['memory']:
                alerts['memory'] = metrics['memory']['percent'] > self.thresholds['memory']
            else:
                alerts['memory'] = metrics['memory'] > self.thresholds['memory']
        # Проверяем диск
        if 'disk' in self.thresholds and 'disk' in metrics:
            if isinstance(metrics['disk'], dict) and 'percent' in metrics['disk']:
                alerts['disk'] = metrics['disk']['percent'] > self.thresholds['disk']
            else:
                alerts['disk'] = metrics['disk'] > self.thresholds['disk']
        # Сеть пока не анализируем
        return alerts

    def set_thresholds(self, thresholds):
        """Установка новых порогов."""
        self.thresholds.update(thresholds)
