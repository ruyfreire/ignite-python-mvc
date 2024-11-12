from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable
from .interfaces.pet_lister_controller import PetListerControllerInterface


class PetListerController(PetListerControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.pets_repository = pets_repository

    def list_pets(self):
        pets = self.__list_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __list_pets_in_db(self) -> list[PetsTable]:
        pets = self.pets_repository.list_pets()
        return pets

    def __format_response(self, pets: list[PetsTable]):
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({
                "id": pet.id,
                "name": pet.name,
            })

        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets
            }
        }
