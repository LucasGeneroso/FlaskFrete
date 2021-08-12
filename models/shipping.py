from db import db
from typing import List


class ShippingModel(db.Model):
    __tablename__ = "shippings"

    id = db.Column(db.Integer, primary_key=True)
    carrier_name = db.Column(db.String(80), nullable=False, unique=True)
    constant_freight_calc = db.Column(db.Float, nullable=False)
    minimum_height = db.Column(db.Float, nullable=False)
    maximum_height = db.Column(db.Float, nullable=False)
    minimum_width = db.Column(db.Float, nullable=False)
    maximum_width = db.Column(db.Float, nullable=False)
    delivery_time = db.Column(db.Float, nullable=False)

    def __init__(self, carrier_name, constant_freight_calc, minimum_height, maximum_height, minimum_width, maximum_width, delivery_time):
        self.carrier_name = carrier_name
        self.constant_freight_calc = constant_freight_calc
        self.minimum_height = minimum_height
        self.maximum_height = maximum_height
        self.minimum_width = minimum_width
        self.maximum_width = maximum_width
        self.delivery_time = delivery_time

    def __repr__(self, ):
        return f'ShippingModel(carrier_name={self.carrier_name}, constant_freight_calc={self.constant_freight_calc}, minimum_height={self.minimum_height}, maximum_height={self.maximum_height}, minimum_width={self.minimum_width}, maximum_width={self.maximum_width}, delivery_time={self.delivery_time})'

    def json(self, ):
        return {'carrier_name': self.carrier_name, 'constant_freight_calc': self.constant_freight_calc, 'minimum_height': self.minimum_height, 'maximum_height': self.maximum_height, 'minimum_width': self.minimum_width, 'maximum_width': self.maximum_width, 'delivery_time': self.delivery_time}
    
    @classmethod
    def find_by_carrier_name(cls, carrier_name) -> "ShippingModel":
        return cls.query.filter_by(carrier_name=carrier_name).first()

    @classmethod
    def find_by_id(cls, _id) -> "ShippingModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["ShippingModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()


class FreigthModel(db.Model):
    __tablename__ = "freights"

    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
   
    def __init__(self, height, width, weight):
        self.height = height
        self.width = width
        self.weight = weight

    def __repr__(self, ):
        return f'FreigthModel(height={self.height}, width={self.width}, weight={self.weight})'

    def json(self, ):
        return {'height': self.height, 'width': self.width, 'weight': self.weight}

    @classmethod
    def freight_calc(cls, height, width, weight) -> "ShippingModel":
        carriers = ShippingModel.find_all()

        eligible_carriers = []

        for carrier in carriers:
            c_name = carrier.carrier_name
            c_height_maximium = carrier.maximum_height
            c_height__minimum = carrier.minimum_height
            c_width_maximum = carrier.maximum_width
            c_width_minimum = carrier.minimum_width
            c_constant_freight = carrier.constant_freight_calc
            c_delivery_time = carrier.delivery_time

            height_calc = False
            if height > c_height__minimum and height < c_height_maximium:
                height_calc = True

            width_calc = False
            if width > c_width_minimum and width < c_width_maximum:
                width_calc = True

            if height_calc and width_calc:
                cost_of_freight = ((weight * c_constant_freight) / 10)
                
                response = {
                  "nome": c_name,
                  "valor_frete": float(cost_of_freight),
                  "prazo_dias": c_delivery_time
                }

                eligible_carriers.append(response)

        return eligible_carriers

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
