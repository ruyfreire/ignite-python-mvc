import pytest
from .people_creator_controller import PeopleCreatorController


class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass


def test_create():
    people = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 1
    }

    controller = PeopleCreatorController(MockPeopleRepository())
    response = controller.create(people)

    assert response['data']['type'] == 'Person'
    assert response['data']['count'] == 1
    assert response['data']['attributes'] == people


def test_create_error():
    people = {
        "first_name": "John123",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 1
    }

    controller = PeopleCreatorController(MockPeopleRepository())

    with pytest.raises(ValueError):
        controller.create(people)
