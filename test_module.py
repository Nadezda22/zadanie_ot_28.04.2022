import requests


def tests_url_status(base_url, status_code):
    response = requests.get(url=base_url)
    assert response.status_code == status_code
