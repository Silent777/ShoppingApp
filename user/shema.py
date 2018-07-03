from marshmallow import fields, validate

from db import ma


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    category_id = fields.Integer(required=True)
    first_name = fields.String(required=True, validate=validate.Length(1))
    last_name = fields.String(required=True, validate=validate.Length(1))
    is_loyal = fields.Boolean()
    creation_date = fields.DateTime()