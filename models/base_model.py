#!/usr/bin/python3
""" Module contains class BaseModel
base class of all the classes in the project
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Parent class for AirBnB clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """
    def __init__(self, id):
        """initializes object using dictionary if given otherwise
        it gives default value
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ initialize str
        returns class name, id and the dictionary"""
        return "[{:s}] ({}) {}".format(self.__class__.__name__,
                  self.id, self.__dict__)

    def save(self):
        """ updates the public instance attributes"""
        self.updated_at = datetime.now()
        storage.save()
        return 

    def to_dict(self):
        """ returns dictionary containing all key value pairs
        of __dict__ of the instance"""
