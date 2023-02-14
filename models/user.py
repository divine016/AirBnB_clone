#!usr/bin/python3
"""creates a User class that inherits from base model"""

from models.base_model import BaseModel

class User(BaseModel):
    """ User class """

    
    email = ""
    Password = ""
    first_name = ""
    last_name = ""