#!/usr/bin/python3
"""
objects that handles all default RestFul API actions:
"""
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State


"""Retrieves the list"""


@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['GET'])
def city_id(city_id):
    ''' busca una ciudad a partir de su id '''
    objeto = storage.get(City, city_id)
    if objeto is None:
        abort(404)
    return jsonify(objeto.to_dict())


@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['DELETE'])
def del_city_id(city_id):
    ''' elimina una ciudad a partir de su id '''
    objeto = storage.get(City, city_id)
    if objeto is None:
        abort(404)
    objeto.delete()
    storage.save()
    return jsonify({})


@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['PUT'])
def update_city_id(city_id):
    ''' actualiza una ciudad a partir de su id '''
    dic = request.get_json()
    objeto = storage.get(City, city_id)
    if objeto is None:
        abort(404)
    if not dic:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key in dic.keys():
        if key not in ["id", "state_id", "created_at", "updated_at"]:
            setattr(objeto, key, dic[key])
    objeto.save()
    return jsonify(objeto.to_dict())


@app_views.route('/states/<state_id>/cities',
                 strict_slashes=False, methods=['GET'])
def state_city(state_id):
    ''' listar estados a partir de su id '''
    objeto = storage.get(State, state_id)
    if objeto is None:
        abort(404)
    lista = [city.to_dict() for city in objeto.cities]
    return jsonify(lista)


@app_views.route('/states/<state_id>/cities',
                 strict_slashes=False, methods=['POST'])
def state_city_post(state_id):
    '''  estados a partir de su id '''
    objeto = storage.get(State, state_id)
    dic = request.get_json()
    if objeto is None:
        abort(404)
    if not dic:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if "name" not in dic:
        return make_response(jsonify({'error': 'Missing name'}), 400)
    dic["state_id"] = state_id
    new_object = City(**dic)
    print(City(**dic))
    new_object.save()
    return make_response(jsonify(new_object.to_dict()), 201)
