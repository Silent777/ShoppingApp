from db import db


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

    @staticmethod
    def create(items, first_name=None, last_name=None):

        user = User()
        user.first_name = first_name
        user.last_name = last_name
        db.session.add(user)
        try:
            for item in items:
                user.items.append(item[0])
            db.session.commit()
            return user
        except ():
            pass

    def __repr__(self):
        return '<id {}>'.format(self.id)