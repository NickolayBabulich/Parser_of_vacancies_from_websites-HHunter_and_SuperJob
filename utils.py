import psycopg2

from classes.dbmanager import DBManager


def create_db(db_name, params):
    """Метод создает базу данных"""
    try:
        connection = psycopg2.connect(dbname='postgres', **params)
        connection.autocommit = True
        cursor = connection.cursor()

        cursor.execute(f"DROP DATABASE IF EXISTS {db_name};")
        cursor.execute(f"CREATE DATABASE {db_name};")
        cursor.close()
        connection.close()
        print(f'База данных {db_name} создана')
    except(Exception, psycopg2.DatabaseError) as error:
        print('Ошибка при создание базы данных:\n', error)


def create_tables(cursor, script_file):
    """Метод Создает таблицы с данными"""
    with open(script_file, 'r') as f:
        script = f.read()
    cursor.execute(script)


def fill_employers(cursor, employers):
    """Метод заполняет таблицу с данными о компаниях"""
    for employer_id, employer in employers.items():
        cursor.execute("INSERT INTO employers (employer_id, employer_name) "
                       "VALUES (%s, %s)",
                       (
                           employer_id,
                           employer
                       )
                       )


def fill_vacancies(cursor, vacancies):
    """Метод заполняет таблицу с данными о вакансиях"""
    for vacancy in vacancies:
        cursor.execute(
            "INSERT INTO vacancies (employer_id, vacancy_name, salary_from, salary_to, url) "
            "VALUES (%s, %s, %s, %s, %s)",
            (
                vacancy['employer_id'],
                vacancy['vacancy_name'],
                vacancy['salary_from'],
                vacancy['salary_to'],
                vacancy['url']
            )
        )


def add_foreign_key(cursor):
    """Метод добавляет связь foreign key в таблицу"""
    cursor.execute("ALTER TABLE vacancies ADD CONSTRAINT vacancies_by_employer "
                   "FOREIGN KEY (employer_id) REFERENCES employers (employer_id)")


def interface(params):
    """Метод для взаимодействия с пользователем"""
    dbmanager = DBManager(params)
    while True:
        user_input = input("""
        Для взаимодействия с базой данных введите номер команды:
        
        1. Показать список всех компаний и количество вакансий у каждой компании.
        2. Показать список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        3. Показать среднюю зарплату по вакансиям.
        4. Показать список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        5. Показать список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
        0. Завершить программу
        
        Введите номер команды: """)

        if user_input == '0':
            dbmanager.connection_close()
        elif user_input == '1':
            dbmanager.get_companies_and_vacancies_count()
        elif user_input == '2':
            dbmanager.get_all_vacancies()
        elif user_input == '3':
            dbmanager.get_avg_salary()
        elif user_input == '4':
            dbmanager.get_vacancies_with_higher_salary()
        elif user_input == '5':
            query = input("Поиск по ключевому слову в название вакансии, введите запрос: ")
            dbmanager.get_vacancies_with_keyword(query)
