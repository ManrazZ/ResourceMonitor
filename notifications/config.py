import json
import yaml
import os


def load_config(config_path):
    """
    Загрузка конфигурации из файла.

    :param config_path: путь к файлу конфигурации
    :return: словарь с конфигурацией
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Файл конфигурации не найден: {config_path}")

    with open(config_path, 'r') as file:
        if config_path.endswith('.json'):
            config = json.load(file)
        elif config_path.endswith('.yaml') or config_path.endswith('.yml'):
            config = yaml.safe_load(file)
        else:
            raise ValueError("Неизвестный формат файла конфигурации. Используйте JSON или YAML.")

    return config
