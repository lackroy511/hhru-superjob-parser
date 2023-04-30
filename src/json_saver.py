from src.base_json_saver import BaseJsonSaver


import json
from json import JSONDecodeError


class JSONSaver(BaseJsonSaver):

    @classmethod
    def save_to_file(cls, path: str, data: dict) -> None:
        """
        Записывает данные в JSON файл.
        :param path: Str, Путь до файла.
        :param data: Словарь, который будет записан в файл
        :return:
        """
        try:
            del data["number"]
        except KeyError:
            pass

        with open(path, 'a'):
            pass

        with open(path, 'r') as file:

            try:
                temp_data = json.load(file)
                temp_data.append(data)
                with open(path, 'w') as f:
                    json.dump(temp_data, f, indent=4, ensure_ascii=False)

            except JSONDecodeError:
                temp_data = list()
                temp_data.append(data)
                with open(path, 'w') as f:
                    json.dump(temp_data, f, indent=4, ensure_ascii=False)

    @classmethod
    def get_from_file(cls, path: str) -> list:
        """
        Читает данные из файла JSON и возвращает их в виде списка.
        :param path: Str, Путь до файла.
        :return: List, Данные из файла.
        """

        with open(path, 'r') as file:
            data = json.load(file)
            return data


    @classmethod
    def remove_from_file(cls, path: str, index: int) -> None:
        """
        Удаляет один элемент (словарь) по индексу из файла (Список словарей).
        :param path: Str, Путь до файла.
        :param index: Int, Индекс удаляемого элемента.
        """

        with open(path, 'r') as file:
            data = json.load(file)
            del data[index]

        with open(path, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @classmethod
    def clear_file(cls, path: str) -> None:
        """
        Удаляет все данные из файла.
        :param path: Str, Путь до файла.
        """
        with open(path, 'w'):
            pass
