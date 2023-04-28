from prettytable import PrettyTable, ALL, MSWORD_FRIENDLY, SINGLE_BORDER


class TableCreator:

    @classmethod
    def main_menu(cls) -> PrettyTable:
        """
        Функция создает и возвращает объект таблицы главного меню.
        :return: Инициализированный таблицей объект PrettyTable
        """

        table = PrettyTable(hrules=ALL)

        table.field_names = ['Номер действия', 'Описание']

        table.add_rows([
            ['[1]', 'Смотреть вакансии на hh.ru'],
            ['[2]', 'Смотреть вакансии на SuperJob.ru'],
            ['[3]', 'Смотреть вакансии в избранном'],
            ['[4]', 'Очистить избранное'],
            ['[5]', 'Выйти из программы']
        ])

        table.set_style(MSWORD_FRIENDLY)

        return table

    @classmethod
    def vacancies(cls, vacancies: list) -> PrettyTable:
        """
        Создает таблицу, инициализирует ее данными из списка (список словарей) и возвращает ее.
        :param vacancies: List, Список словарей
        :return: PrettyTable, объект таблицы
        """
        table = PrettyTable(hrules=ALL)

        table.field_names = ['Номер', 'Название вакансии', 'город', 'опыт работы', 'зарплата']

        for vacancy in vacancies:

            number = vacancy['number']
            name = vacancy['name']
            city = vacancy['city']
            experience = vacancy['experience']
            salary_from = vacancy['salary_from']
            salary_to = vacancy['salary_to']

            if not salary_from and not salary_to:
                salary = 'Зарплата не указана'
            elif not salary_from and salary_to:
                salary = f'Зарплата до {salary_to}'
            elif salary_from and not salary_to:
                salary = f'Зарплата от {salary_from}'

            else:
                salary = f'Зарплата от {salary_from} до {salary_to}'

            table.add_row([number, name, city, experience, salary])

        table.set_style(SINGLE_BORDER)

        return table

    @classmethod
    def featured_vacancies(cls, vacancy: dict) -> PrettyTable:
        """
        Создает таблицу, инициализирует ее данными о вакансии из словаря и возвращает ее.
        :param vacancy: Dict, словарь с данными о вакансии
        :return: PrettyTable, объект таблицы
        """

        table = PrettyTable(hrules=ALL)
        table.field_names = ['Название вакансии', 'город', 'опыт работы', 'зарплата']

        name = vacancy['name']
        city = vacancy['city']
        experience = vacancy['experience']
        salary_from = vacancy['salary_from']
        salary_to = vacancy['salary_to']

        if not salary_from and not salary_to:
            salary = 'Зарплата не указана'
        elif not salary_from and salary_to:
            salary = f'Зарплата до {salary_to}'
        elif salary_from and not salary_to:
            salary = f'Зарплата от {salary_from}'

        else:
            salary = f'Зарплата от {salary_from} до {salary_to}'

        table.add_row([name, city, experience, salary])
        table.set_style(SINGLE_BORDER)
        table.add_row(['URL', vacancy['url'], '', ''])

        return table
