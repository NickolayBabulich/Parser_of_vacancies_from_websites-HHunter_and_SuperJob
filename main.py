import os
from config import config
from utils import *
from classes.api_objects import HeadHunterAPI
from classes.work_with_data import JSON

params = config()


def main():
    employers = {
        1740: 'Яндекс',
        3776: 'МТС',
        23186: 'Группа Компаний РУСАГРО',
        577743: 'Госкорпорация Росатом',
        2869446: 'Skillfactory',
        1331661: 'html academy',
        1122462: 'Skyeng',
        15478: 'VK',
        740: 'Норникель',
        80: 'Альфа-Банк'
    }

    params = config()
    hh = HeadHunterAPI()
    data_from_json = JSON()

    json_data = os.path.join("data", "data.json")
    script_file = os.path.join('scripts', 'db.sql')
    db_name = 'my_new_db'

    load_vacancies = hh.get_all_vacancies(employers)
    data_from_json.save_to(load_vacancies)

    create_db(db_name, params)
    params.update({'dbname': db_name})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                create_tables(cur, script_file)
                print(f"В БД {db_name} созданы таблицы employers и vacancies")

                fill_employers(cur, employers)
                print("Таблица employers успешно заполнена данными")

                fill_vacancies(cur, data_from_json.read_to(json_data))
                print("Таблица vacancies успешно заполнена данными")

                add_foreign_key(cur)
                print("Связывание таблиц выполнено успешно")
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    interface(params)


if __name__ == '__main__':
    main()
