#!/usr/bin/python3
"""Defines a module amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Defines a amenity that inherits from BaseModel.

        public class attributes:
                name: string - empty string
    """
    name = ""
