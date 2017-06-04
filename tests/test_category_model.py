import unittest

from sqlalchemy.exc import IntegrityError

from todo_guru import create_app, db
from todo_guru.models import Category


class CategoryModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_category_success(self):
        category = Category(name='Test category', notes='Test notes')
        db.session.add(category)
        db.session.commit()
        self.assertTrue(category.id is not None)
        self.assertEqual(category.name, 'Test category')
        self.assertEqual(category.notes, 'Test notes')
        self.assertTrue(category.created_on is not None)

    def test_create_category_without_name(self):
        category = Category()
        db.session.add(category)
        self.assertRaises(IntegrityError, db.session.commit)
