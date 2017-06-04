import unittest

from sqlalchemy.exc import IntegrityError

from todo_guru import create_app, db
from todo_guru.models import Tag


class TagModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_tag_success(self):
        tag = Tag(name='Test tag', notes='Test notes')
        db.session.add(tag)
        db.session.commit()
        self.assertTrue(tag.id is not None)
        self.assertEqual(tag.name, 'Test tag')
        self.assertEqual(tag.notes, 'Test notes')
        self.assertTrue(tag.created_on is not None)

    def test_create_tag_without_name(self):
        tag = Tag()
        db.session.add(tag)
        self.assertRaises(IntegrityError, db.session.commit)
