#!usr/bin/python3
"""creates a Review class that inherits from base model"""

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel

class Review(BaseModel):
    """ Review class """


    place_id = ""
    user_id = ""
    text = ""