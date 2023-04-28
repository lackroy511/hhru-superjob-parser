from abc import ABC, abstractmethod


class BaseClassForAPI(ABC):
    """Базовый класс для API сайтов с вакансиями"""

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def basic_info_about_vacancies(self):
        pass
