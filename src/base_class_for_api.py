from abc import ABC, abstractmethod

class BaseClassForAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def basic_info_about_vacancies(self):
        pass
