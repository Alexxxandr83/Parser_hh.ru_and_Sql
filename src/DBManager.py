import psycopg2


class DBManager():
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(dbname=dbname,
                                     user=user,
                                     password=password,
                                     host=host,
                                     port=port)
        self.queries = 'queries.sql'

    def create_tables(self):
        with self.conn.cursor() as cur:
            with open(self.queries, 'r') as file:
                queries = file.read().split(';')
                for query in queries[:2]:
                    if query.strip():
                        cur.execute(query.strip() + ';')

        self.conn.commit()

    def drop_tables(self):
        with self.conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS vacancies;")
            cur.execute("DROP TABLE IF EXISTS companies;")
            self.conn.commit()

    def get_companies_and_vacansies_count(self):
        with self.conn.cursor() as cur:
            with open(self.queries, 'r', encoding='utf-8') as f:
                queries = f.read().split(';')
                query = queries[4].strip()
                cur.execute(query)
            results = cur.fetchall()
            return results

    def all_vacansies(self):
        with self.conn.cursor() as cur:
            with open(self.queries, 'r', encoding='utf-8') as f:
                queries = f.read().split(';')
                query = queries[5].strip()
                cur.execute(query)
            results = cur.fetchall()
            return results

    def get_avg_salary(self):
        with self.conn.cursor() as cur:
            with open(self.queries, 'r', encoding='utf-8') as f:
                queries = f.read().split(';')
                query = queries[6].strip()
                cur.execute(query)
            results = cur.fetchall()
            return results

    def get_vacancies_with_higher_salary(self):
        with self.conn.cursor() as cur:
            with open(self.queries, 'r', encoding='utf-8') as f:
                queries = f.read().split(';')
                query = queries[7].strip()
                cur.execute(query)
            results = cur.fetchall()
            return results

    def get_vacancies_with_keyword(self, keyword):
        with self.conn.cursor() as cur:
            with open(self.queries, 'r', encoding='utf-8') as f:
                queries = f.read().split(';')
                query = queries[8].strip()
                cur.execute(query)
            results = cur.fetchall()
            return results

    def close_connection(self):

        self.conn.close()
