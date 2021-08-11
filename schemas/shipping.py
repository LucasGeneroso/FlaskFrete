from ma import ma
from models.shipping import ShippingModel, FreigthModel


class ShippingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ShippingModel
        load_instance = True

class FreigthSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FreigthModel
        load_instance = True
