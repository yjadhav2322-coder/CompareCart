from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class Product(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(200),
        nullable=False
    )

    category = db.Column(
        db.String(100)
    )

    image = db.Column(
        db.String(500)
    )

    description = db.Column(
        db.Text
    )

    prices = db.relationship(
        'Price',
        backref='product',
        lazy=True
    )

    feedbacks = db.relationship(
        'Feedback',
        backref='product',
        lazy=True
    )


class Seller(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    website = db.Column(
        db.String(500)
    )

    prices = db.relationship(
        'Price',
        backref='seller',
        lazy=True
    )


class Price(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey('product.id'),
        nullable=False
    )

    seller_id = db.Column(
        db.Integer,
        db.ForeignKey('seller.id'),
        nullable=False
    )

    price = db.Column(
        db.Float
    )

    availability = db.Column(
        db.String(50)
    )

    url = db.Column(
        db.String(500)
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

class Feedback(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey('product.id'),
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    rating = db.Column(
        db.Integer,
        nullable=False
    )

    comment = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    wishlist_items = db.relationship(
        'Wishlist',
        backref='user',
        lazy=True,
        cascade='all, delete-orphan'
    )

    cart_items = db.relationship(
        'CartItem',
        backref='user',
        lazy=True,
        cascade='all, delete-orphan'
    )


class Wishlist(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey('product.id'),
        nullable=False
    )

    product = db.relationship(
        'Product',
        backref='wishlist_items'
    )


class CartItem(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey('product.id'),
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        default=1,
        nullable=False
    )

    product = db.relationship(
        'Product',
        backref='cart_items'
    )