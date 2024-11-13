from flask import Blueprint, jsonify
from src.main.composer.pet_lister_composer import pet_lister_composer
from src.main.composer.pet_deleter_composer import pet_deleter_composer
from src.views.http.types.http_request import HttpRequest

pets_routes_bp = Blueprint('pets_routes', __name__)


@pets_routes_bp.route('/pets', methods=['GET'])
def list_pets():
    http_request = HttpRequest()

    view = pet_lister_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code


@pets_routes_bp.route('/pets/<name>', methods=['DELETE'])
def delete_pet(name):
    http_request = HttpRequest(param={"name": name})

    view = pet_deleter_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
