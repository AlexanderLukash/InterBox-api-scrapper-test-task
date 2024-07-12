from src.app.scrapper import RestCountriesRequestAPI
from src.app.utils import print_country_data
from src.config.config import load_config


def main():
    config = load_config("./.env")
    countries_data = RestCountriesRequestAPI().get_country_data(url=config.BASE_URL)
    countries_info = [
        RestCountriesRequestAPI().extract_country_info(country)
        for country in countries_data
    ]
    print_country_data(countries_info)


if __name__ == "__main__":
    main()
