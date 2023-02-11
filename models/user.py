#!usr/bin/python3
"""User class"""
import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel

class User(BaseModel):
    """ User class """
    email = ""
    Password = ""
    first_name = ""
    last_name = ""