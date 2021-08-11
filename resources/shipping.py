from flask import request
from flask_restplus import Resource, fields

from models.shipping import ShippingModel
from schemas.shipping import ShippingSchema
from models.shipping import FreigthModel
from schemas.shipping import FreigthSchema

from server.instance import server

shipping_ns = server.shipping_ns
freigth_ns = server.freigth_ns

ITEM_NOT_FOUND = "Shipping not found."
FREIGHT_NOT_FOUND = "no carrier was elected"

shipping_schema = ShippingSchema()
shipping_list_schema = ShippingSchema(many=True)
freigth_schema = FreigthSchema()
freigth_list_schema = FreigthSchema(many=True)

# Model required by flask_restplus for expect
shipping_item = shipping_ns.model('Shipping', {
    'carrier_name': fields.String(),
    'constant_freight_calc': fields.Float(),
    'minimum_height': fields.Float(),
    'maximum_height': fields.Float(),
    'minimum_width': fields.Float(),
    'maximum_width': fields.Float(),
    'delivery_time': fields.Float()
})

freight_item = freigth_ns.model('Freigth', {
    'altura': fields.Float(),
    'largura': fields.Float(),
    'peso': fields.Float()
})

# arrumar o payload de post do matchFreach, que nao ta igual a kabum pede
# trazer o valor do frete em float
# arrumar pra trazer ordenado sempre os mesmos campos no get
# deixar a api em portgues igual da doc

class Shipping(Resource):

    def get(self, id):
        shipping_data = ShippingModel.find_by_id(id)
        if shipping_data:
            return shipping_schema.dump(shipping_data)
        return {'message': ITEM_NOT_FOUND}, 404

    def delete(self, id):
        shipping_data = ShippingModel.find_by_id(id)
        if shipping_data:
            shipping_data.delete_from_db()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

    @shipping_ns.expect(shipping_item)
    def put(self, id):
        shipping_data = ShippingModel.find_by_id(id)
        shipping_json = request.get_json()

        if shipping_data:
            shipping_data.carrier_name = shipping_json['carrier_name']
            shipping_data.constant_freight_calc = shipping_json['constant_freight_calc']
            shipping_data.minimum_height = shipping_json['minimum_height']
            shipping_data.maximum_height = shipping_json['maximum_height']
            shipping_data.minimum_width = shipping_json['minimum_width']
            shipping_data.maximum_width = shipping_json['maximum_width']
            shipping_data.delivery_time = shipping_json['delivery_time']

        else:
            shipping_data = shipping_schema.load(shipping_json)

        shipping_data.save_to_db()
        return shipping_schema.dump(shipping_data), 200

class ShippingList(Resource):

    @shipping_ns.doc('Get all the Items')
    def get(self):
        return shipping_list_schema.dump(ShippingModel.find_all()), 200

    @shipping_ns.expect(shipping_item)
    @shipping_ns.doc('Create an Item')
    def post(self):
        shipping_json = request.get_json()
        shipping_data = shipping_schema.load(shipping_json)

        shipping_data.save_to_db()

        return shipping_schema.dump(shipping_data), 201

class MatchFreigth(Resource):

    @freigth_ns.expect(freight_item)
    @freigth_ns.doc('Create an Item')
    def post(self):
        freigth_json = request.get_json()

        r_height = freigth_json['altura']
        r_width = freigth_json['largura']
        r_weight = freigth_json['peso']

        freigth_data = FreigthModel.freight_calc(r_height, r_width, r_weight)

        if freigth_data:
            return freigth_data, 201
        return {'message': FREIGHT_NOT_FOUND, 'return': '[]'}, 404

