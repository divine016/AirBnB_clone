#!/usr/bin/python3
""" creates a User class that inherits from base model"""

import uuid
from models.base_model import BaseModel


class User(BaseModel):
    """ User class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""