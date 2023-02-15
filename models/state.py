#!/usr/bin/python3
""" creates a State class that inherits from base model """

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""
