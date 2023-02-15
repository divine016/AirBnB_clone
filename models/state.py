#!/usr/bin/python3
""" creates a mmodule for User class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class for managing state objects"""

    name = ""