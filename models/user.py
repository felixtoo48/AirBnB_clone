#!/usr/bin/python3
""" User class module that inherits from
BaseModel"""

from modules.base_model import BaseModel


class User(BaseModel):
    """ initializes the user class
    Sub class of base model
    Methods:
        __init__(self)
    """
    def __init__(self, email=None, password=None, first_name=None, last_name=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
