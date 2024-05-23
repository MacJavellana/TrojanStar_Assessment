from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Recipe(db.Model):
    __tablename__ = 'Recipes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    preparation_time = db.Column(db.Integer, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    steps = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    comments = db.relationship('Comment', backref='Recipes', cascade='all, delete-orphan')
    ratings = db.relationship('Rating', backref='Recipes', cascade='all, delete-orphan')


class Comment(db.Model):
    __tablename__ = 'Comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipes.id', ondelete='CASCADE'), nullable=False)

class Rating(db.Model):
    __tablename__ = 'Ratings'
    id = db.Column(db.Integer, primary_key=True)
    rate = db.Column(db.Integer, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipes.id', ondelete='CASCADE'), nullable=False)