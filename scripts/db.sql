DROP TABLE IF EXISTS employers;
DROP TABLE IF EXISTS vacancies;

CREATE TABLE employers
(
	employer_id VARCHAR(10) PRIMARY KEY,
	employer_name VARCHAR(40)
);

CREATE TABLE vacancies
(
	employer_id VARCHAR(10) NOT NULL REFERENCES employers(employer_id),
	vacancy_name VARCHAR(100),
	salary_from INT,
	salary_to INT,
	url TEXT
)