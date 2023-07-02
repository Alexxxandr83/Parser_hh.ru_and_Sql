from DBManager import DBManager
from hh_get_data import HH_vacancies_employers
from utils import insert_vacansy_data_to_db, insert_employer_data_to_db

if __name__ == '__main__':
    # Подключаемся к БД
    db = DBManager(
        dbname='CorseWork5',
        user='postgres',
        password='neskaju',
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

    db.close_connection() # Закрываем соеднение БД
