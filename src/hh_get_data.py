import requests
from abstract_class import AbstarctApiClass

from src.config import hh_api_config


class HH_vacancies_employers(AbstarctApiClass):
    def __init__(self, page: int = 0):
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
            "page": page,
            "employer_id": hh_api_config.get('employers_ids'),
            "only_with_salary": hh_api_config.get('only_with_salary'),
            "per_page": hh_api_config.get('vacancies_per_page'),
            "area": hh_api_config.get('area')
        }

    def get_vacancies(self) -> list[dict]:
        """ Получаем вакансии у заданных по id работодателей"""

        response = requests.get(self.url, params=self.params)

        return response.json()['items']

    def get_employers(self) -> list[dict]:
        """ Получаем список работодателей, их id и ссылку на страницу работодаьеля в hh.ru"""

        result = [
            {
                "id": uid,
                "name": requests.get(f'https://api.hh.ru/employers/{uid}').json().get('name'),
                "url": requests.get(f'https://api.hh.ru/employers/{uid}').json().get('alternate_url'),

            }
            for uid in self.params.get('employer_id') if uid is not None
        ]
        return result
