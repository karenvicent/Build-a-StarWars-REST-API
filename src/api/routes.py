"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Characters, Planets, Favorite_characters, Favorite_planets
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/characters', methods=['GET'])
def get_all_characters():
    all_charaters_query = Characters.query.all()
    all_characters = list(map(lambda x: x.serialize(), all_charaters_query))
    return jsonify(all_characters), 200

@api.route('/planets', methods=['GET'])
def get_all_planets():
    all_planets_query = Planets.query.all()
    all_planets = list(map(lambda x: x.serialize(), all_planets_query))
    return jsonify(all_planets), 200

@api.route('/addfavoriteplanet/<int:id>/', methods=['POST'])
def add_planet(id):
    planet_query = Planets.query.filter_by(id)
    favorite_planet = Favorite_planets(planet_name=planet_query['planet_name'])
    db.session.add(favorite_planet)
    db.session.commit()

    respuesta = {
    "message": "favorito agregado exitosamente"
    }

    return jsonify(respuesta), 200
