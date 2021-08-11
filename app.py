from flask import Flask, Blueprint, jsonify
from flask_restplus import Api
from ma import ma
from db import db

from resources.shipping import Shipping, ShippingList, MatchFreigth, shipping_ns 
from marshmallow import ValidationError

from server.instance import server

api = server.api
app = server.app

@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400

api.add_resource(Shipping, '/shippings/<int:id>')
api.add_resource(ShippingList, '/shippings')
api.add_resource(MatchFreigth, '/freight')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    server.run()
