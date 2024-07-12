from src.app.scrapper import RestCountriesRequestAPI
from src.config.config import load_config


def test_extract_country_info():
    sample_country = {
        "name": {"common": "Ukraine"},
        "capital": ["Kyiv"],
        "flags": {"png": "https://restcountries.com/data/ukr.png"},
    }
    name, capital, flag = RestCountriesRequestAPI().extract_country_info(sample_country)
    assert name == "Ukraine"
    assert capital == "Kyiv"
    assert flag == "https://restcountries.com/data/ukr.png"


def test_get_country_data(monkeypatch):
    config = load_config("./.env")

    class MockResponse:
        @staticmethod
        def json():
            return [
                {
                    "name": {"common": "Ukraine"},
                    "capital": ["Kyiv"],
                    "flags": {"png": "https://restcountries.com/data/ukr.png"},
                },
            ]

        status_code = 200

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)

    countries_data = RestCountriesRequestAPI().get_country_data(url=config.BASE_URL)
    assert len(countries_data) == 1
    assert countries_data[0]["name"]["common"] == "Ukraine"
