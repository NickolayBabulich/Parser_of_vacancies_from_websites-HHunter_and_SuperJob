# Parser of vacancies with DB

## Описание:

Программа получает данные о вакансиях и работодателях с HeadHunter (в настройках заданы конкретные компании) и на основе их загружает данные в таблицы базы данных PostgreSQL для дальнейшей работы
В программе реализованны принципы ООП, работа с базой данных postgresql

## Технологии:

[![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
  [![JSON](https://img.shields.io/badge/-JSON-000000?style=flat&logo=json&logoColor=white)](https://www.json.org/)
[![OOP](https://img.shields.io/badge/-OOP-FF5733?style=flat)](https://en.wikipedia.org/wiki/Object-oriented_programming) [![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

## Реализовано:

- заполнение базы данных вакансиями указанных компаний
- отображение списка компаний и количества имеющихся вакансий
- отображение списка всех найденных вакансий
- отображение средней зарплаты по вакансиям
- отображение списка списка вакансей с зарплатой выше средней
- отображение вакансий по ключевому слову в поиске
- сохранение данных в JSON

## Дополнительно:

- для работы необходимо клонировать проект, установить зависимости
- Необходимо указать конфигурации в database.ini следующего вида:

    [postgresql]  
    host=localhost  
    user=postgres  
    password=12345  
    port=5432
- после запустить программу из файла main.py
