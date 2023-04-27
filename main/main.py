from utils.utils import print_intro, print_main_menu_table, create_main_menu_table,  get_action_number
from utils.utils import create_vacancies_table, print_vacancy_table

from src.head_hunter_api import HeadHunterAPI
from src.super_job_api import SuperJobAPI


def main():

    print_intro()
    main_menu = create_main_menu_table()
    print_main_menu_table(main_menu)
    action_number = get_action_number(5)

    super_job_api = SuperJobAPI()
    table = create_vacancies_table(super_job_api.basic_info_about_vacancies)
    print_vacancy_table(table)


if __name__ == '__main__':

    main()

