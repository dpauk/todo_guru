from flask import redirect, render_template, url_for

from . import main
from .forms import TodoEntryForm
from .. import db
from ..models import Todo  # , Category, Tag


@main.route('/', methods=['GET', 'POST'])
def index():
    # todos = Todo.query.
    return render_template('index.html')


@main.route('/add_todo', methods=['GET', 'POST'])
def add_todo():
    form = TodoEntryForm()
    if form.validate_on_submit():
        todo = Todo(name=form.name.data,
                    notes=form.notes.data,
                    due_on=form.due_on.data)
        db.session.add(todo)
        return redirect(url_for('.index'))
    return render_template('add_todo.html', form=form)
