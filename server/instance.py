from flask import Flask, Blueprint
from flask_restplus import Api
from ma import ma
from db import db

from marshmallow import ValidationError


class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.bluePrint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.bluePrint, doc='/doc', title='Sample Flask-RestPlus Application Shipping')
        self.app.register_blueprint(self.bluePrint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True

        self.shipping_ns = self.shipping_ns()
        self.freigth_ns = self.freigth_ns()

        super().__init__()

    def shipping_ns(self, ):
        return self.api.namespace(name='Shippings', description='shipping related operations', path='/')

    def freigth_ns(self, ):
        return self.api.namespace(name='Freigths', description='freigth related operations', path='/')

    def run(self, ):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0'
        )


server = Server()
