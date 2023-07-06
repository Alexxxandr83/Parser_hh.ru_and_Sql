# -*- coding: utf-8 -*-
def insert_vacansy_data_to_db(data: list[dict[str, any]], db: any) -> None:
    """
    Вставляет данные о вакансиях в базу данных.

    Аргументы:
    - data (List[Dict[str, Any]]): Список словарей с данными о вакансиях.
    - db (Any): Объект подключения к базе данных.

    Возвращаемое значение:
    - None
    """
    with db.conn.cursor() as cur:
        for vacancy in data:
            cur.execute("""
            INSERT INTO vacancies (id, name, company_id, salary_from, salary_to, url)
            VALUES (%s, %s, %s, %s, %s, %s);
            """, (
                vacancy['id'],
                vacancy['name'],
                vacancy['employer']['id'],
                vacancy['salary']['from'],
                vacancy['salary']['to'],
                vacancy['alternate_url']
            )
                        )
            db.conn.commit()


def insert_employer_data_to_db(data: list[dict[str, any]], db: any) -> None:
    """
    Вставляет данные о работодателях в базу данных.

    Аргументы:
    - data (List[Dict[str, Any]]): Список словарей с данными о работодателях.
    - db (Any): Объект подключения к базе данных.

    Возвращаемое значение:
    - None

    Исключения:
    - Ошибки, связанные с базой данных.
    """
    with db.conn.cursor() as cur:
        for employer in data:
            cur.execute("""UPDATE employers SET name = %s, url = %s WHERE id = %s;""",
                        (employer['name'], employer['url'], employer['id']))
    db.conn.commit()
