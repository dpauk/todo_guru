from datetime import datetime

from . import db


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False)
    notes = db.Column(db.String(1000))
    parent_id = db.Column(db.Integer, index=True)
    categories = db.relationship('Category', backref='todo', lazy='dynamic')
    tags = db.relationship('Tag', backref='todo', lazy='dynamic')
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    done_on = db.Column(db.DateTime())


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, index=True, nullable=False)
    notes = db.Column(db.String(1000))
    todo_id = db.Column(db.Integer, db.ForeignKey('todos.id'))
    parent_id = db.Column(db.Integer, index=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, index=True, nullable=False)
    notes = db.Column(db.String(1000))
    todo_id = db.Column(db.Integer, db.ForeignKey('todos.id'))
    parent_id = db.Column(db.Integer, index=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
