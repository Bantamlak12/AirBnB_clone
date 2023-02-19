#!/usr/bin/python3
"""Defines unittests for base_model.py."""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A TestBaseModel unittesting class."""
    def setUp(self):
        self.bm = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, datetime.datetime)
        self.assertIsInstance(self.bm.updated_at, datetime.datetime)

    def test_str(self):
        e = f"[{self.bm.__class__.__name__}] ({self.bm.id}) {self.bm.__dict__}"
        self.assertEqual(str(self.bm), e)

    def test_save(self):
        current_time = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(current_time, self.bm.updated_at)

    def test_to_dict(self):
        bm_dict = self.bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertIn("__class__", bm_dict)
        self.assertIn("created_at", bm_dict)
        self.assertIn("updated_at", bm_dict)


if __name__ == "__main__":
    unittest.main()
