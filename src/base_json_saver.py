from abc import ABC, abstractmethod


class BaseJsonSaver(ABC):

    @abstractmethod
    def save_to_file(self, path, data):
        pass

    @abstractmethod
    def get_from_file(self, path):
        pass

    @abstractmethod
    def remove_from_file(self):
        pass

    @abstractmethod
    def clear_file(self):
        pass
