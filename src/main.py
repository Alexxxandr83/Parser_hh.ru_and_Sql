from DBManager import DBManager
from hh_get_data import HH_vacancies_employers
from insert_data import insert_vacansy_data_to_db, insert_employer_data_to_db
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    # Подключаемся к БД
    db = DBManager(
        dbname='CorseWork5',
        user=os.environ.get('USER'),
        password=os.environ.get('DB_PASSWORD'),
        host='localhost',
        port='5432'
    )
    db.drop_tables()  # Удаляем таблицы если они уже есть
    db.create_tables()  # Создаем таблицы

    # Подключаемся к api.hh.ru и получаем данные по вакансиям и работодателям
    hh_data = HH_vacancies_employers()  # Подключаемся к api.hh.ru
    vacansy_list = hh_data.get_vacancies()  # Получаем список вакансий
    employers_list = hh_data.get_employers()  # Получаемя список работадалетей, с id, названием и url

    # Заполняем таблицы данными
    insert_employer_data_to_db(employers_list, db)
    insert_vacansy_data_to_db(vacansy_list, db)

    print(f'Колличество вакансий у выбранных работодателей:{db.get_companies_and_vacansies_count()}')
    print(f'Все вакансии выбранных работодаьелей: {db.all_vacansies()}')
    print(f'Размер средней зарплаты по вакансиям: {db.get_avg_salary()}')
    print(f'Вакансии с зарплатой выше средней: {db.get_vacancies_with_higher_salary()}')
    user_input = input('Введите ключевое слово для поиска: ')
    print(f'Получение вакансий по ключевому слову: {db.get_vacancies_with_keyword(user_input)}')

    db.close_connection()  # Закрываем соеднение БД
