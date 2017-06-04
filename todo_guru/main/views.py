from flask import render_template

from . import main
# from .. import db
from ..models import Todo, Category, Tag


@main.route('/', methods=['GET', 'POST'])
def index():
    # todos = Todo.query.
    return render_template('index.html')
