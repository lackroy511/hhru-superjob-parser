from time import sleep


from tqdm import tqdm
from art import tprint
from prettytable import PrettyTable, ALL, MSWORD_FRIENDLY, SINGLE_BORDER


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


def create_main_menu_table() -> PrettyTable:
    """
    Функция создает и возвращает объект таблицы главного меню

    :return: Инициализированный таблицей объект PrettyTable
    """

    table = PrettyTable(hrules=ALL)
    table.field_names = ['Номер дейсвия', 'Описание']

    table.add_rows([
        ['[1]', 'Смотреть вакансии на hh.ru'],
        ['[2]', 'Смотреть вакансии на SuperJob.ru'],
        ['[3]', 'Смотреть вакансии в избранном'],
        ['[4]', 'Очистить избранное'],
        ['[5]', 'Выйти из программы']
    ])

    table.set_style(MSWORD_FRIENDLY)

    return table


def print_main_menu_table(table: PrettyTable) -> None:
    """
    Функция принимает таблицу главного меню и печатает ее

    :param table: Инициализированный таблицей объект PrettyTable
    :return action_number:  int, Номер действия в меню
    """

    print('\t' * 4 + '   Главное меню')
    print(table)
    print()


def create_vacancies_table(vacancies: dict) -> PrettyTable:

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


def print_vacancy_table(table: PrettyTable) -> None:

    print(table)


def get_action_number(total_numbers: int) -> int:
    """
    Функция запрашивает ввод пользователя для выбора действия в меню, число от 1 до total_numbers.
    :param total_numbers: Инициализированный таблицей объект PrettyTable
    :return: int, Число о 1 до total_numbers
    """
    try:
        action_number = int(input('Выберите номер действия: '))

        if not 0 < action_number <= total_numbers:
            print()
            print(f'Нет такого действия!!! Выберите другое, от 1 до {total_numbers}!')
            get_action_number(total_numbers)

        return action_number

    except ValueError:
        print()
        print(f'Нет такого действия!!! Выберите другое, от 1 до {total_numbers}!')
        get_action_number(total_numbers)
