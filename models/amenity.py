#!/usr/bin/python3
""" creates an Amenity class that inherits from base model """

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class """
    name = ""