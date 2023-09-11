import psycopg2


class DBManager:
    """Класс для взаимодействия с базой данных Postgres"""

    def __init__(self, params):
        """
        Метод инициализирует подключение к БД
        :param params: параметры для подключения к БД
        """
        self.connection = psycopg2.connect(**params)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def get_companies_and_vacancies_count(self):
        """Метод получает список всех компаний и количество вакансий у каждой компании"""
        self.cursor.execute("SELECT employer_name, COUNT(vacancy_name) FROM vacancies "
                            "JOIN employers USING (employer_id) "
                            "GROUP BY employer_name")
        result = self.cursor.fetchall()
        for item in result:
            print(f"Название компании: {item[0].ljust(30)} Вакансий: {item[1]}")

    def get_all_vacancies(self):
        """Метод получает список всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию"""
        self.cursor.execute("SELECT employer_name, vacancy_name, salary_from, salary_to, url FROM vacancies "
                            "JOIN employers USING(employer_id)")
        result = self.cursor.fetchall()
        for item in result:
            print(item)

    def get_avg_salary(self):
        """Метод получает среднюю зарплату по вакансиям"""
        self.cursor.execute("SELECT AVG(salary_from) as средняя_зарплата_от FROM vacancies")
        result = self.cursor.fetchall()
        for item in result:
            print(f"Средняя зарплата от: {int(item[0])} руб.")

    def get_vacancies_with_higher_salary(self):
        """Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        self.cursor.execute("SELECT * FROM vacancies "
                            "WHERE salary_from > (SELECT AVG(salary_from+salary_to) FROM vacancies) "
                            "OR salary_to > (SELECT AVG(salary_from+salary_to) FROM vacancies)")
        result = self.cursor.fetchall()
        for item in result:
            print(f"Вакансия: {item[1]}, "
                  f"зарплата от {item[2]} - до {item[3]}, "
                  f"Ссылка на вакансию: {item[4]}")

    def get_vacancies_with_keyword(self, query):
        """Метод получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python"""
        for word in query.split():
            self.cursor.execute(f"SELECT * FROM vacancies "
                                f"WHERE vacancy_name LIKE '%{word.capitalize()}%'")
            result = self.cursor.fetchall()
            if result:
                print(f'Результаты по ключевому слову "{word}":')
            for item in result:
                print(f"Вакансия: {item[1]}, "
                      f"зарплата от {item[2]} - до {item[3]}, "
                      f"Ссылка на вакансию: {item[4]}")

    def connection_close(self):
        self.cursor.close()
        self.connection.close()
        exit()
