from abc import ABC, abstractmethod


class AbstarctApiClass(ABC):

    @abstractmethod
    def get_vacancies(self): pass

    @abstractmethod
    def get_employers(self): pass
