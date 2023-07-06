# -*- coding: utf-8 -*-
import psycopg2


class DBManager():
    """
    Инициализирует объект dbmanager и устанавливает соединение с базой данных.

        Аргументы:
        - dbname (str): Имя базы данных.
        - user (str): Имя пользователя для доступа к базе данных.
        - password (str): Пароль пользователя для доступа к базе данных.
        - host (str): Хост базы данных.
        - port (str): Порт базы данных.
    """

    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(dbname=dbname,
                                     user=user,
                                     password=password,
                                     host=host,
                                     port=port)
        self.queries = 'queries.sql'

    def create_tables(self) -> None:
        """
        Создает таблицы в базе данных, используя предоставленные файлы с запросами.

        Returns:
            None
        """
        with self.conn.cursor() as cur:
            with open(self.queries, 'r') as file:
                queries = file.read().split(';')
                for query in queries[:2]:
                    if query.strip():
                        cur.execute(query.strip() + ';')

        self.conn.commit()

    def drop_tables(self) -> None:
        """
        Метод для удаления таблиц vacancies и companies из базы данных.

        Returns:
            None
        """
        with self.conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS vacancies;")
            cur.execute("DROP TABLE IF EXISTS companies;")
            self.conn.commit()

    def get_companies_and_vacansies_count(self) -> list:
        """
        Метод get_companies_and_vacancies_count получает количество компаний и вакансий.


        :return: результаты выполнения запроса
        :rtype: list
        """
        with self.conn.cursor() as cur:
            with open(self.queries, 'r', encoding='utf-8') as f:
                queries = f.read().split(';')
                query = queries[4].strip()
                cur.execute(query)
            results = cur.fetchall()
            return results

    def all_vacancies(self) -> list[tuple]:
        """
        Получает все вакансии из базы данных.

        :return: Список кортежей с результатами запроса.
        :rtype: List[Tuple]
        """
        with self.conn.cursor() as cur:
            with open(self.queries, 'r', encoding='utf-8') as f:
                queries = f.read().split(';')
                query = queries[5].strip()
                cur.execute(query)
            results = cur.fetchall()
            return results

    def get_avg_salary(self) -> list[tuple]:
        """
        Получает среднюю зарплату.

        :return: Список кортежей с результатами запроса
        """
        with self.conn.cursor() as cur:
            with open(self.queries, 'r', encoding='utf-8') as f:
                queries = f.read().split(';')
                query = queries[6].strip()
                cur.execute(query)
            results = cur.fetchall()
            return results

    def get_vacancies_with_higher_salary(self) -> list[tuple]:
        """Получает вакансии с более высокой заработной платой.

        Returns:
            List[Tuple]: Список кортежей с результатами запроса.
        """
        avg_salary = self.get_avg_salary()
        with self.conn.cursor() as cur:
            with open(self.queries, 'r', encoding='utf-8') as f:
                queries = f.read().split(';')
                query = queries[7].strip()
                cur.execute(query, avg_salary)
            results = cur.fetchall()
            return results

    def get_vacancies_with_keyword(self, keyword: str) -> list:
        """
        Получает вакансии по ключевому слову.

        Параметры:
            - keyword (str): Ключевое слово для поиска вакансий.

        Возвращает:
            - results (list): Список результатов поиска вакансий.
        """
        with self.conn.cursor() as cur:
            with open(self.queries, 'r', encoding='utf-8') as f:
                queries = f.read().split(';')
                query = queries[8].strip()
                cur.execute(query, (f"%{keyword}%)",))
                results = cur.fetchall()
            return results

    def close_connection(self):
        """
         Закрывает соединение с базой данных.
         """
        self.conn.close()
