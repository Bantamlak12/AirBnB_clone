#!/usr/bin/python3
"""Defines a module city"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Defines a new City that inherits from BaseModel.

        Public class attributes:
            state_id: string - empty string: it will be the State.id
            name: string - empty string
    """
    state_id = ""
    name = ""
