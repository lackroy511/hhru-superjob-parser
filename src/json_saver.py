from src.base_json_saver import BaseJsonSaver


import json
from json import JSONDecodeError


class JSONSaver(BaseJsonSaver):

    @classmethod
    def save_to_file(cls, path: str, data: dict):

        try:
            del data["number"]
        except KeyError:
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
    def get_from_file(cls, path: str):

        with open(path, 'r') as file:
            data = json.load(file)
            return data
    @classmethod
    def remove_from_file(cls):
        pass

    @classmethod
    def clear_file(cls):
        pass
