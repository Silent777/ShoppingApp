from flask import request
from flask_restful import Resource
from models import db, Basket, BasketSchema, Item

baskets_schema = BasketSchema(many=True)
basket_schema = BasketSchema()


def get_items(item_ids):

    items = []
    for item_id in item_ids:
        item = Item.query.filter_by(id=item_id).all()
        if item:
            items.append(item)
    return items


class BasketResource(Resource):
    def get(self):
        baskets = Basket.query.all()
        baskets = baskets_schema.dump(baskets).data
        return {'status': 'success', 'data': baskets}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = basket_schema.load(json_data)
        if errors:
            return errors, 422

        items = get_items(json_data['items'])

        basket = Basket.create(
            price=json_data['price'],
            items=items
        )

        db.session.add(basket)
        db.session.commit()

        result = basket_schema.dump(basket).data

        return {"status": 'success', 'data': result}, 201

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:

            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = basket_schema.load(json_data)
        if errors:
            return errors, 422
        basket = Basket.query.filter_by(id=data['id']).first()
        if not basket:
            return {'message': 'Category does not exist'}, 400
        basket.price = data['price']
        db.session.commit()

        result = basket_schema.dump(basket).data

        return {"status": 'success', 'data': result}, 204

    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = basket_schema.load(json_data)
        if errors:
            return errors, 422
        basket = Basket.query.filter_by(id=data['id']).delete()
        db.session.commit()

        result = basket_schema.dump(basket).data

        return {"status": 'success', 'data': result}, 204
