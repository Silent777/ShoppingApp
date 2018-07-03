from flask import request
from flask_restful import Resource

from user.model import User
from item.model import Item
from basket.shema import BasketSchema
from db import db

users_schema = BasketSchema(many=True)
user_schema = BasketSchema()


def get_items(item_ids):

    items = []
    for item_id in item_ids:
        item = Item.query.filter_by(id=item_id).all()
        if item:
            items.append(item)
    return items


class UserResource(Resource):
    def get(self):
        users = User.query.all()
        users = users_schema.dump(users).data
        return {'status': 'success', 'data': users}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422

        items = get_items(json_data['items'])

        user = User.create(
            first_name=json_data['price'],
            last_name=json_data['last_name'],
            items=items
        )

        db.session.add(user)
        db.session.commit()

        result = user_schema.dump(user).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:

            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422
        user = User.query.filter_by(id=data['id']).first()
        if not user:
            return {'message': 'Category does not exist'}, 400
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.is_loyal = data['is_loyal']

        db.session.commit()

        result = user_schema.dump(user).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422
        user = User.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = user_schema.dump(user).data

        return {"status": 'success', 'data': result}, 204
