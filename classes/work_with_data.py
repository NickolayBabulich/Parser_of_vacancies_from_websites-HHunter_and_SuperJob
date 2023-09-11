from abc import ABC, abstractmethod
import os
import json


class Engine(ABC):
    """Абстрактный класс для работы с данными"""

    @abstractmethod
    def save_to(self, data):
        pass

    @abstractmethod
    def read_to(self, data):
        pass


class JSON(Engine):
    """Класс для обработки данных в JSON формате"""

    def save_to(self, data: list):
        """
        Метод для сохранения данных в JSON
        :param data: данные для сохранения
        """
        FILENAME = os.path.join("data", "data.json")
        if not os.path.isdir("data"):
            os.mkdir("data")
        with open(FILENAME, "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def read_to(self, data):
        """
        Метод для чтения данных из JSON
        :param data: данные для чтения
        :return: возвращает данные в формате JSON
        """
        with open(data, 'r') as f:
            load_vacancies = json.load(f)
        return load_vacancies
