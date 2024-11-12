from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController


class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(id=1, name="Dog"),
            PetsTable(id=2, name="Cat"),
        ]


def test_list():
    controller = PetListerController(MockPetsRepository())
    response = controller.list_pets()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"id": 1, "name": "Dog"},
                {"id": 2, "name": "Cat"},
            ]
        }
    }

    assert response == expected_response
