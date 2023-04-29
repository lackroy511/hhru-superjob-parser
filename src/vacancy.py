

class Vacancy:
    """Класс для представления вакансии"""

    def __init__(
            self, name: str, city: str, experience: str, url: str,
            salary_from: int or None, salary_to: int or None
            ):

        """Конструктор для класса Vacancy"""

        # Тут просто для каждого атрибута проверка на принадлежность какому-то типу данных. (Валидация)
        if not isinstance(name, str):
            raise ValueError('Параметр "name" должен быть строкой')
        self.name = name

        if not isinstance(city, str):
            raise ValueError('Параметр "city" должен быть строкой')
        self.city = city

        if not isinstance(experience, str):
            raise ValueError('Параметр "experience" должен быть строкой')
        self.experience = experience

        if not isinstance(salary_from, int):
            if salary_from is not None:
                raise ValueError('Параметр "salary_from" должен быть целым числом или None')
        self.salary_from = salary_from

        if not isinstance(salary_to, int):
            if salary_to is not None:
                raise ValueError('Параметр "salary_to" должен быть целым числом или None')
        self.salary_to = salary_to

        if self.salary_from and self.salary_to:
            self.salary = (self.salary_from + self.salary_to) / 2

        elif not self.salary_from and self.salary_to:
            self.salary = self.salary_to

        elif self.salary_from and not self.salary_to:
            self.salary = self.salary_from

        elif not self.salary_from and not self.salary_to:
            self.salary = 0

        if not isinstance(url, str):
            raise ValueError('Параметр "url" должен быть строкой')
        self.url = url

    def __str__(self):
        return f"Название: {self.name}" \
               f"Город: {self.city}" \
               f"Опыт работы: {self.experience}" \
               f"Зарплата от: {self.salary_from}" \
               f"Зарплата до: {self.salary_to}" \
               f"Зарплата в среднем: {self.salary}" \
               f"url: {self.url}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', " \
                                         f"'{self.city}', " \
                                         f"'{self.experience}', " \
                                         f"'{self.salary_from}', " \
                                         f"'{self.salary_to}', " \
                                         f"'{self.salary}', " \
                                         f"'{self.url}')"

    def __gt__(self, other) -> bool:
        if isinstance(other, Vacancy):
            if int(self.salary) > int(other.salary):
                return True
        return False

    def __ge__(self, other) -> bool:
        if isinstance(other, Vacancy):
            if int(self.salary) >= int(other.salary):
                return True
        return False

    def __lt__(self, other) -> bool:
        if isinstance(other, Vacancy):
            if int(self.salary) < int(other.salary):
                return True
        return False

    def __le__(self, other) -> bool:
        if isinstance(other, Vacancy):
            if int(self.salary) <= int(other.salary):
                return True
        return False
