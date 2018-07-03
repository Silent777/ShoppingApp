from marshmallow import fields

from db import ma


class BasketSchema(ma.Schema):
    id = fields.Integer()
    price = fields.Integer()
