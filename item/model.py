from basket_item.model import basket_item
from db import db


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    baskets = db.relationship('Basket', secondary=basket_item, backref=db.backref('baskets', lazy='dynamic'))
    price = db.Column(db.Integer)

    def __init__(self, name, price):
        self.name = name,
        self.price = price,