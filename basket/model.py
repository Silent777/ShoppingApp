from basket_item.model import basket_item
from db import db


class Basket(db.Model):
    __tablename__ = 'baskets'

    id = db.Column(db.Integer, primary_key=True)
    items = db.relationship('Item', secondary=basket_item, backref=db.backref('items', lazy='dynamic'))
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
