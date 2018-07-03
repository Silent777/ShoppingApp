from db import db

basket_item = db.Table('baskets_items', db.metadata,
                       db.Column('id', db.Integer, primary_key=True),
                       db.Column('baskets', db.Integer, db.ForeignKey('baskets.id', ondelete='CASCADE')),
                       db.Column('items', db.Integer, db.ForeignKey('items.id', ondelete='CASCADE'))
                       )
