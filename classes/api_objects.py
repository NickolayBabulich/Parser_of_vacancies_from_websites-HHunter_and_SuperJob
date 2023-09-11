from abc import ABC, abstractmethod
from tqdm import tqdm
import requests


class APIObjects(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def get_all_vacancies(self, employers):
        pass


class HeadHunterAPI(APIObjects):
    """Класс для работы с API HeadHunter"""

    def get_all_vacancies(self, employers: dict) -> list:
        """
        Метод получения вакансий с заданных компаний
        :param employers: список компаний
        :return: возвращает списко вакансий заданных компаний
        """
        vacancies_by_companies = []
        url = "https://api.hh.ru/vacancies"
        for employer in tqdm(employers, ncols=100, colour='green', desc='Выполняется загрузка вакансий, ожидайте...'):
            params = {
                "page": 0,
                "per_page": 100,
                "area": 113,
                "only_with_salary": True,
                "employer_id": employer
            }
            response = requests.get(url, params)
            response_data = response.json()
            all_vacancies = response_data["items"]
            while response_data["page"] != 1:
                params["page"] += 1
                response = requests.get(url, params)
                response_data = response.json()
                all_vacancies.extend(response_data["items"])
            for vacancy in all_vacancies:
                vacancies_by_companies.append(
                    {
                        'employer_id': vacancy['employer']['id'],
                        'employer_name': vacancy['employer']['name'],
                        'vacancy_name': vacancy['name'],
                        'salary_from': vacancy['salary']['from'],
                        'salary_to': vacancy['salary']['to'],
                        'url': vacancy['alternate_url']
                    }
                )
        return vacancies_by_companies
