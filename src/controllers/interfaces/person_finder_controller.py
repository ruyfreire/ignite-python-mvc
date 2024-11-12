from abc import ABC, abstractmethod


class PersonFinderControllerInterface(ABC):

    @abstractmethod
    def finder(self, person_id: int) -> dict:
        pass
