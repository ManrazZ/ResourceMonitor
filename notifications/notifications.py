import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class NotificationManager:
    """
    Класс для управления уведомлениями.
    """
    def __init__(self, methods=None):
        if methods is None:
            methods = ['console']
        self.methods = methods

    def notify(self, alerts, metrics):
        """
        Отправка уведомлений.

        :param alerts: словарь с флагами превышения
        :param metrics: словарь с текущими метриками
        """
        message = self._format_message(alerts, metrics)
        for method in self.methods:
            if method == 'console':
                self._console_notification(message)
            elif method == 'log':
                self._log_notification(message)
            elif method == 'email':
                self._email_notification(message)
            else:
                raise ValueError(f"Неизвестный метод уведомления: {method}")

    def _format_message(self, alerts, metrics):
        """Форматирование сообщения."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"[{timestamp}] Обнаружено превышение порогов:\n"
        for resource, alert in alerts.items():
            if alert:
                message += f"  - {resource}: {metrics.get(resource, 'N/A')}\n"
        return message

    def _console_notification(self, message):
        """Вывод уведомления в консоль."""
        print(message)

    def _log_notification(self, message):
        """Запись уведомления в лог."""
        logging.warning(message)

    def _email_notification(self, message):
        """Отправка уведомления по email (заглушка)."""
        # В реальности здесь должна быть реализация отправки email
        logging.info(f"Email notification: {message}")
