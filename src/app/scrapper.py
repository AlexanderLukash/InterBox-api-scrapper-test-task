from abc import ABC, abstractmethod

import requests


class BaseRequestAPI(ABC):
    @abstractmethod
    def get_country_data(self, url: str): ...

    @abstractmethod
    def extract_country_info(self, country): ...


class RestCountriesRequestAPI(BaseRequestAPI):
    def get_country_data(self, url: str):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def extract_country_info(self, country):
        name = country.get("name", {}).get("common", "N/A")
        capital = country.get("capital", ["N/A"])[0]
        flag = country.get("flags", {}).get("png", "N/A")
        return name, capital, flag
