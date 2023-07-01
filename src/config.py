from typing import Dict, List, Any

hh_api_config: dict[str, int | list[str | Any] | bool] = {
    'employers_ids': [
        '67611',  # Тензор
        '78638',  # Тинькофф
        '1740',  # Yandex
        '3529',  # СБЕР
        '3776',  # MTC
        '3127',  # Мегафон
        '15478',  # VC
        '2180',  # OZON
        '80',  # Альфа-Банк
        '681672',  # Usetech
        '4759060'  # HR Prime
    ],
    'vacancies_per_page': 100,
    'only_with_salary': True,
    'area': 113  # Россия
}
