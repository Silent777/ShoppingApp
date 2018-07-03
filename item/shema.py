from marshmallow import fields, validate
from db import ma


class ItemSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(1))
    price = fields.Integer()