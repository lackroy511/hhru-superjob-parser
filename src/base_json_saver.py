from abc import ABC, abstractmethod


class BaseJsonSaver(ABC):
    """Базовый класс для работы с JSON файлом."""

    @abstractmethod
    def save_to_file(self, path, data):
        pass

    @abstractmethod
    def get_from_file(self, path):
        pass

    def remove_from_file(self, path, index):
        pass

    def clear_file(self, path):
        pass
