#!/usr/bin/python3
""" User class module that inherits from
BaseModel"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """ initializes the user class
    Sub class of base model
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
