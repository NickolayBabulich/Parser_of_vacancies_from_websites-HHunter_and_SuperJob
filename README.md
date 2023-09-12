Программа получает данные о вакансиях и работодателях с HeadHunter и на основе их загружает данные в таблицы базы данных PostgresSQL
Для полноценной работы программы установите зависимости в файле requirement.txt
Необходимо указать конфигурации в database.ini следующего вида
[postgresql]
host=localhost
user=postgres
password=12345
port=5432
