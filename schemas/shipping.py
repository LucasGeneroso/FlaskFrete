from ma import ma
from ma import Schema, fields
from models.shipping import ShippingModel, FreigthModel


class ShippingSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = ShippingModel
		load_instance = True


class DimensionSchema(Schema):
	heigth = fields.Float()
	width = fields.Float()


class FreigthSchema(Schema):
	dimension = fields.Nested(DimensionSchema)
	weigth = fields.Float()