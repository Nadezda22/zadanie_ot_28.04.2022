# тесты для REST API - https://www.openbrewerydb.org/
import random

import pytest
import requests


@pytest.fixture
def bewery_id():
    response = requests.get("https://api.openbrewerydb.org/breweries")
    ids = []
    for i in response.json():
        ids.append(i["id"])
        return random.choise(ids)


def test_get_all_breweries():
    response = requests.get("https://api.openbrewerydb.org/breweries")
    data = response.json()
    assert response.status_code == 200
    assert not len(data) == 0, "List of all breweries is empty."


@pytest.mark.parmetrize("filter_by, value", [
    ("by_city", "san_diego"),
    ("by_dist", "38.8977,77.0365"),
    ("by_name", "cooper"),
    ("by_state", "ohio"),
    ("by_postal", "44107")
])
def test_filter_by_type(btype):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_type={btype}")
    assert response.status_code == 200
    data = response.json()
    assert not len(data) == 0, "List of breweries filtering by type is empty."
    for i in data:
        assert i[
                   "brewery_type"] == btype, f"Type of brewery = {i['brewery_type']} doesn't match with filter by {btype}."


def test_get_brewery(berwery_id):
    response = requests.get(f"https://api.openbrewerydb.org/breweries/{brewery_id}")
    assert response.status_code == 200
    data = response.json()
    assert brewery_id == data["id"], "ID's doesn't match"


def test_search_breawery():
    query = "dog"
    response = requests.get(f"https://api.openbrewerydb.org/breweries/search?query={query}")
    assert response.status_code == 200
    data = response.json()
    assert not len(data) == 0, f"List of search results by query '{query}' is empty."
