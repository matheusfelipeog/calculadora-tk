# -*- coding: utf-8 -*-

# @autor: Matheus Felipe
# @github: github.com/matheusfelipeog

from json import load as json_load
from json import dump as json_dump
from os.path import exists, join, dirname


class History(object):
    """Класс для хранения и управления историей вычислений."""

    MAX_ITEMS = 10

    def __init__(self, path=None):
        if path is None:
            path = join(dirname(__file__), 'settings', 'history.json')
        self.path = path
        self.items = self._load()

    def _load(self):
        """Загружает историю из файла или возвращает пустой список."""
        if not exists(self.path):
            return []
        try:
            with open(self.path, mode='r', encoding='utf-8') as f:
                data = json_load(f)
            return data if isinstance(data, list) else []
        except (ValueError, OSError):
            return []

    def _save(self):
        """Сохраняет историю в файл."""
        try:
            with open(self.path, mode='w', encoding='utf-8') as f:
                json_dump(self.items, f, indent=4, ensure_ascii=False)
        except OSError:
            pass  # Не критично, если не удалось сохранить

    def add(self, expression, result):
        """Добавляет новую запись в историю."""
        entry = {'expression': expression, 'result': result}
        if self.items and self.items[-1] == entry:
            return
        self.items.append(entry)
        if len(self.items) > self.MAX_ITEMS:
            self.items = self.items[-self.MAX_ITEMS:]
        self._save()

    def clear(self):
        """Очищает историю."""
        self.items = []
        self._save()

    def last(self):
        """Возвращает последнюю запись или None."""
        return self.items[-1] if self.items else None

    def all(self):
        """Возвращает все записи."""
        return list(self.items)