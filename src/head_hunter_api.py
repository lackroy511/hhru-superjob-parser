from src.base_class_for_api import BaseClassForAPI

import requests


class HeadHunterAPI(BaseClassForAPI):
    """Класс для работы с API Head Hunter"""
    url = 'https://api.hh.ru/vacancies'

    def __init__(self):
        """
        :param self.text: Ключевые слова для поиска вакансий
        :param self.page: Номер страницы,
        """
        self.keywords = ''
        self.page = 1

    @property
    def get_vacancies(self) -> dict:
        """
        Функция получает дынные о вакансиях через GET запрос.
        :return: Словарь с данными о вакансиях.
        """
        params = {
            'page': self.page,
            'per_page': 8,
            'locale': 'RU',
            'text': self.keywords
        }

        response = requests.get(self.url, params=params)
        data = response.json()

        return data

    @property
    def basic_info_about_vacancies(self):
        """
        Функция работает с данными вакансий, достает только ключевую информацию и возвращает список словарей
        с основными данными вакансий.
        :return: List, список словарей с вакансиями.
        """
        list_of_vacancies = []
        data = self.get_vacancies
        number = 1
        for vacancy in data['items']:
            try:
                list_of_vacancies.append({
                    'number': number,
                    'name': vacancy['name'],
                    'city': vacancy['area']['name'],
                    'experience': vacancy['experience']['name'],
                    'salary_from': vacancy['salary']['from'],
                    'salary_to': vacancy['salary']['to'],
                    'url': vacancy['alternate_url']
                })
                number += 1
            except (TypeError, KeyError):
                list_of_vacancies.append({
                    'number': number,
                    'name': vacancy['name'],
                    'city': vacancy['area']['name'],
                    'experience': vacancy['experience']['name'],
                    'salary_from': None,
                    'salary_to': None,
                    'url': vacancy['alternate_url']
                })
                number += 1

        return list_of_vacancies
