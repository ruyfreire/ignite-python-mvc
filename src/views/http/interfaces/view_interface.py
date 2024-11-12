from abc import ABC, abstractmethod
from src.views.http.types.http_request import HttpRequest
from src.views.http.types.http_response import HttpResponse


class ViewInterface(ABC):

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass
