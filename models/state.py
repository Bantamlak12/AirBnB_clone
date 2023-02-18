#!/usr/bin/python3
"""Defines a module state"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Defines a state that inherits from BaseModel
        Public class attributes:
            name: string - empty string
    """
    name = ""
