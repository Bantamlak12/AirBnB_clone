#!/usr/bin/python3
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittesting for testing FileStorage class"""
    def setUp(self):
        self.fs = FileStorage()
        self.bm = BaseModel()

    def test_all(self):
        self.fs.new(self.bm)
        objects = self.fs.all()

    def test_new(self):
        self.fs.new(self.bm)
        objects = self.fs.all()
        obj = objects.get("BaseModel.{}".format(self.bm.id))
        self.assertIsInstance(obj, BaseModel)

    def test_save(self):
        self.fs.new(self.bm)
        self.fs.save()
        with open("file.json") as f:
            self.assertTrue("BaseModel.{}".format(self.bm.id) in json.load(f))

    def test_reload(self):
        self.fs.new(self.bm)
        self.fs.save()
        self.fs.reload()
        objects = self.fs.all()
        obj = objects.get("BaseModel.{}".format(self.bm.id))
        self.assertIsInstance(obj, BaseModel)


if __name__ == "__main__":
    unittest.main()
