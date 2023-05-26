from src.json_saver import JSONSaver
from src.table_creator import TableCreator
from src.vacancy import Vacancy


from os.path import join
from time import sleep

from tqdm import tqdm
from art import tprint
from prettytable import PrettyTable


def print_intro() -> None:
    """Функция печатает приветствие"""

    print('\n' + '\t' * 4 + 'Hi There, this is...\n')
    tprint('Job-Job')

    input('Press Enter to start:')

    pbar = tqdm(range(100),
                leave=False,
                ncols=60,
                colour='#747671',
                bar_format='The program is loading:|{bar}|{n_fmt}/{total_fmt}%'
                )

    for i in pbar:
        sleep(0.025)
        pbar.set_description()


def print_main_menu_table(table: PrettyTable) -> None:
    """
    Функция принимает таблицу главного меню и печатает ее
    :param table: Инициализированный таблицей объект PrettyTable
    """

    print('\t' * 4 + '           Главное меню')
    print(table)
    print()


def print_vacancy_table(table: PrettyTable) -> None:
    """
    Функция принимает таблицу с вакансиями и печатает ее
    :param table: Инициализированный таблицей объект PrettyTable
    """
    print(table)
    print('[1] - Предыдущая страница \t\t\t\t[2] - Следующая страница \n'
          '[*n] - Добавить вакансию в избранное \t[3] - Главное меню')


def print_featured_vacancy(table: PrettyTable) -> None:
    """
    Функция принимает таблицу с вакансиями и печатает ее
    :param table: Инициализированный таблицей объект PrettyTable
    """
    print(table)
    print('[1] - Предыдущая вакансия \t\t\t\t[2] - Следующая страница \n'
          '[3] - Удалить вакансию из избранного \t[4] - Главное меню')


def get_action_number(total_numbers: int) -> int or str:
    """
    Функция запрашивает ввод пользователя для выбора действия в меню, число от 1 до total_numbers
    или [*n] n - число от 1 до 8.
    :param total_numbers: Инициализированный таблицей объект PrettyTable
    :return: int, Число о 1 до total_numbers, которое ввел пользователь.
    """

    while True:

        action_num = input('Выберите номер действия: ')
        print()

        if action_num.isdigit():
            if 0 < int(action_num) <= total_numbers:
                action_num = int(action_num)
                return action_num
            else:
                print(f'Выберите другое действие!!!')

        elif action_num.startswith('*') \
                and len(action_num) == 2 \
                and action_num[1].isdigit() \
                and int(action_num[1]) in range(1, 9):
            return action_num

        else:
            print(f'Выберите другое действие!!!')


def vacancy_scroller(api_obj) -> None:
    """
    Функция для просмотра вакансий в консоли с hh.ru либо с SuperJob.ru
    :param api_obj: Экземпляр класса HeadHunterAPI или SuperJobAPI
    """

    path_to_file = join('data', 'featured_vacancies.json')

    while True:

        # Получил данные по вакансиям с hh.ru или c SuperJob.ru и записал их в 'vacancies'.
        vacancies = api_obj.basic_info_about_vacancies

        # Создал таблицу с данными, передав данные 'vacancies' в создателя таблиц.
        vacancies_table = TableCreator.vacancies(vacancies)
        print('\n\n\n')

        # Печать таблицы, но перед этим проварка ее на пустоту, если пусто, цикл прерывается, выкидывает в обратно меню.
        if not vacancies:
            print('По вашему запросу ничего не найдено!!!')
            break

        print(f'Номер страницы: {api_obj.page}')
        print_vacancy_table(vacancies_table)
        print()

        # Ввод пользователя с выбором действия
        vacancy_action = get_action_number(3)

        # Блок с вариантами действий в зависимости от выбора пользователя.
        if vacancy_action == 1 and api_obj.page > 1:
            api_obj.page -= 1

        elif vacancy_action == 2:
            api_obj.page += 1

        elif vacancy_action == 3:
            break

        elif vacancy_action in ['*1', '*2', '*3', '*4', '*5', '*6', '*7', '*8']:

            # Записали номер вакансии.
            vacancy_number = int(vacancy_action[1])

            # Тут по номеру вакансии ищем ее на странице, если номер совпадает, записываем ее в JSON.
            for vacancy in vacancies:

                if vacancy['number'] == vacancy_number:
                    JSONSaver.save_to_file(path_to_file, vacancy)


def featured_scroller(featured_vacancies: list) -> None:
    """
    Функция для просмотра вакансий из избранного.
    Так как она принимает список, логика перелистывания страниц завязана на индексе списка.
    :param featured_vacancies: List, Список словарей, с данными о вакансии.
    """

    path_to_file = join('..', 'data', 'featured_vacancies.json')

    max_page = len(featured_vacancies)
    index = 0

    while True:
        print('\n\n\n')
        print(f'Вакансия номер: {index + 1}')
        vacancy_table = TableCreator.featured_vacancies(featured_vacancies[index])
        print_featured_vacancy(vacancy_table)
        print()
        vacancy_action = get_action_number(4)

        if vacancy_action == 1:
            if index > 0:
                index -= 1

        elif vacancy_action == 2:
            if index <= max_page - 2:
                index += 1

        elif vacancy_action == 3:
            try:
                JSONSaver.remove_from_file(path_to_file, index)
            except FileNotFoundError:
                print('Вы еще не добавили в избранное ни одной вакансии!!!')

        elif vacancy_action == 4:
            break


def get_top_five_vacancy(featured_vacancies: list) -> list:
    """
    Принимает список словарей с данными о вакансиях, из этого списка инициализирует список экземпляров класса Vacancy.
    Отсортированных по зарплате в порядке убывания.
    :param featured_vacancies: List, Список словарей с данными о вакансиях.
    :return: List, Список из пяти или меньше экземпляров класса Vacancy.
    """

    top_five_vacancy = list()
    for vacancy in featured_vacancies:

        top_five_vacancy.append(Vacancy(
            vacancy["name"],
            vacancy["city"],
            vacancy["experience"],
            vacancy["url"],
            vacancy["salary_from"],
            vacancy["salary_to"]
        ))
        if featured_vacancies.index(vacancy) == 4:
            break

    top_five_vacancy = sorted(top_five_vacancy, key=lambda x: x.salary, reverse=True)

    return top_five_vacancy
