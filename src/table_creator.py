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
        table.add_row(['[1]', 'Смотреть вакансии на hh.ru'])
        table.add_row(['[2]', 'Смотреть вакансии на SuperJob.ru'], divider=True)
        table.add_row(['[3]', 'Смотреть вакансии в избранном.'])
        table.add_row(['[4]', 'Вывести топ 5 вакансий из избранного по зарплате.'])
        table.add_row(['[5]', 'Очистить избранное.'], divider=True)
        table.add_row(['[6]', 'Выйти из программы.'])

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
        url = vacancy['url']

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
        table.add_row(['URL', url, '', ''])

        return table

    @classmethod
    def top_five_table(cls, top_five_vacancy: list) -> PrettyTable:
        """
        Функция создает таблицу из списка экземпляров класса Vacancy
        :param top_five_vacancy: List, список экземпляров класса vacancy
        :return: PrettyTable, объект таблицы
        """
        table = PrettyTable(hrules=ALL)
        table.field_names = ['Название вакансии', 'URL', 'зарплата']

        for vacancy in top_five_vacancy:

            table.add_row([vacancy.name, vacancy.url, f'З.П. - {vacancy.salary}'])

        table.set_style(SINGLE_BORDER)

        return table
