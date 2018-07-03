from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, validate
from flask_marshmallow import Marshmallow

ma = Marshmallow()
db = SQLAlchemy()

'''
basket_item = db.Table('baskets_items', db.metadata,
                        db.Column('id', db.Integer, primary_key=True),
                        db.Column('baskets', db.Integer, db.ForeignKey('baskets.id', ondelete='CASCADE')),
                        db.Column('items', db.Integer, db.ForeignKey('items.id',ondelete='CASCADE'))
                        )


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    is_loyal = db.Column(db.Boolean, unique=False, default=False)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    basket_id = db.Column(db.Integer, db.ForeignKey('baskets.id', ondelete='CASCADE'), nullable=False)
    basket = db.relationship('Basket', backref=db.backref('users', lazy='dynamic'))

    def __init__(self, first_name, last_name, basket_id):
        self.first_name = first_name
        self.last_name = last_name
        self.basket_id = basket_id




class Basket(db.Model):
    __tablename__ = 'baskets'

    id = db.Column(db.Integer, primary_key=True)
    items = db.relationship('Item', secondary=basket_items, backref=db.backref('items', lazy='dynamic'))
    price = db.Column(db.Integer)

    @staticmethod
    def create(items, price=None):

        basket = Basket()
        basket.price = price
        db.session.add(basket)
        try:
            for item in items:
                basket.items.append(item[0])
            db.session.commit()
            return basket
        except ():
            pass

    def __repr__(self):
        return '<id {}>'.format(self.id)



class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    baskets = db.relationship('Basket', secondary=basket_items, backref=db.backref('baskets', lazy='dynamic'))
    price = db.Column(db.Integer)

    def __init__(self, name, price):
        self.name = name,
        self.price = price,
'''


class BasketSchema(ma.Schema):
    id = fields.Integer()
    price = fields.Integer()


class ItemSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(1))
    price = fields.Integer()


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    category_id = fields.Integer(required=True)
    first_name = fields.String(required=True, validate=validate.Length(1))
    last_name = fields.String(required=True, validate=validate.Length(1))
    is_loyal = fields.Boolean()
    creation_date = fields.DateTime()
