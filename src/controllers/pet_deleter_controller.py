from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from .interfaces.pet_deleter_controller import PetDeleterControllerInterface


class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pets_repository: PetsRepositoryInterface):
        self.pets_repository = pets_repository

    def delete(self, name: str) -> None:
        self.pets_repository.delete_pets(name)
