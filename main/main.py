from utils.utils import print_intro, print_main_menu_table, get_action_number, vacancy_scroller, featured_scroller
from src.table_creator import TableCreator
from src.head_hunter_api import HeadHunterAPI
from src.super_job_api import SuperJobAPI
from src.json_saver import JSONSaver
from json import JSONDecodeError

from os.path import join


PATH_TO_FILE = join('..', 'data', 'featured_vacancies.json')


def main():

    hh_ru_api = HeadHunterAPI()
    super_job_api = SuperJobAPI()

    # Вывел интро программы на экран.
    print_intro()

    # Основной цикл
    while True:

        # Создал объект главного меню и напечатал его
        main_menu = TableCreator.main_menu()
        print_main_menu_table(main_menu)

        # Прочитал ввод пользователя и запомнил его, это число от 1 до 5, соответствует пункту меню.
        action_in_menu = get_action_number(5)

        # Тут блок if/elif из пяти действий в зависимости от выбора пользователя.
        if action_in_menu == 1:
            # Cкроллим вакансии с hh.ru

            vacancy_scroller(hh_ru_api)

        elif action_in_menu == 2:
            # Cкроллим вакансии с hh.ru
            vacancy_scroller(super_job_api)

        elif action_in_menu == 3:
            try:
                # Получили данные из файла
                featured_vacancies = JSONSaver.get_from_file(PATH_TO_FILE)

                # Скроллим избранные вакансии
                featured_scroller(featured_vacancies)
            except JSONDecodeError:
                print('Вы еще не добавили в избранное ни одной вакансии!!!')

        elif action_in_menu == 4:

            # Очистить файл с избранными вакансиями
            JSONSaver.clear_file(PATH_TO_FILE)

        elif action_in_menu == 5:

            # Прервать цикл и выйти из программы
            break


if __name__ == '__main__':
    main()
