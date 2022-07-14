# тест для сайта "https://dog.ceo/dog-api/"

import pytest
import requests


def test_get_all_breeds_list():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    data = response.json()
    assert response.status_code == 200
    assert not len(data["message"]) == 0, "list of breeds is empty"


def test_get_one_random_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    assert response.status_code == 200
    assert "images" in data["message"], "Image wasn't gotten from the server."


@pytest.mark.parametrize("n", [3, 7, 15])
def test_get_multiple_random_images(n):
    response = requests.get(f"https://dog.ceo/api/breeds/image/random/{n}")
    data = response.json()
    assert response.status_code == 200
    assert len(data["message"]) == n, f"Incorrect count of objects. Server returned {len(data['message'])} objects."
    for obj in data["message"]:
        assert "images" in obj, f"Server returned not image - {obj}."


@pytest.mark.parametrize("n", [4, 50])
@pytest.mark.parametrize("breed", ["terrier", "corgi", "chihuahua"])
def test_get_multiple_random_images_by_breed(n, breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random/{n}")
    data = response.json()
    assert response.status_code == 200
    assert len(data["message"]) == n, f"Incorrect count of objects. Server returned {len(data['message'])} objects."
    for obj in data["message"]:
        assert ("images" in obj) and (f"{breed}" in obj), f"Server returned not image or incorrect image - {obj}."


@pytest.mark.parametrize("breed", "sub_breed", [
    ("bulldog", "boston"),
    ("bulldog", "english"),
    ("hound", "afghan"),
    ("hound", "ibizan")
])
def test_get_list_all_sub_breed_imges(breed, sub_breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images")
    data = response.json()
    assert response.status_code == 200
    assert not len(data["message"]) == 0, f"Not images for {breed} {sub_breed}."
    for obj in data["message"]:
        assert "images" in obj and f"{breed}-{sub_breed}" in obj, f"Server returned not image or incorrect image - {obj}."
