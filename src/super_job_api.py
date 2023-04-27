from src.base_class_for_api import BaseClassForAPI
import requests


class SuperJobAPI(BaseClassForAPI):

    ID = 2351
    TOKEN = 'v3.r.124548971.2c48a89110f1ed83764cdaeb3ce58f5a3afa09ed.f7ff0c2d7f8b31e9c49d1e8ee696acf8f761ac94'
    url = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self):

        self.page = 1
        self.keywords = ''

    def get_vacancies(self) -> dict:
        """
        Функция получает дынные о вакансиях
        :return: Словарь с данными о вакансиях
        """
        params = {
            'page': self.page,
            'count': 8,
            'keyword': self.keywords
        }

        response = requests.get(self.url, params=params, headers={'X-Api-App-Id': self.TOKEN})
        data = response.json()

        return data

    @property
    def basic_info_about_vacancies(self):

        list_of_vacancies = []
        data = self.get_vacancies()
        number = 1
        for vacancy in data['objects']:
            list_of_vacancies.append({
                'number': number,
                'name': vacancy['profession'],
                'city': vacancy['client']['town']['title'],
                'experience': vacancy['experience']['title'],
                'salary_from': vacancy['payment_from'],
                'salary_to': vacancy['payment_to'],
                'url': vacancy['link']
            })
            number += 1

        return list_of_vacancies
