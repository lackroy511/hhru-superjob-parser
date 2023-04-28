from utils.utils import print_intro, print_main_menu_table, print_vacancy_table, get_action_number, vacancy_scroller
from src.table_creator import TableCreator
from src.head_hunter_api import HeadHunterAPI
from src.super_job_api import SuperJobAPI
from src.json_saver import JSONSaver

from os.path import join


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

        if action_in_menu == 3:
            pass


if __name__ == '__main__':

    main()
