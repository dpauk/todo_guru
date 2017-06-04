import unittest

from sqlalchemy.exc import IntegrityError

from todo_guru import create_app, db
from todo_guru.models import Todo


class TodoModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_todo_success(self):
        todo = Todo(name='Test todo', notes='Test notes')
        db.session.add(todo)
        db.session.commit()
        self.assertTrue(todo.id is not None)
        self.assertEqual(todo.name, 'Test todo')
        self.assertEqual(todo.notes, 'Test notes')
        self.assertTrue(todo.parent_id is None)
        self.assertTrue(todo.created_on is not None)
        self.assertTrue(todo.updated_on is not None)
        self.assertTrue(todo.done_on is None)

    def test_create_todo_without_name(self):
        todo = Todo()
        db.session.add(todo)
        self.assertRaises(IntegrityError, db.session.commit)

