#!/usr/bin/python3
"""BaseModel Module"""

import models
from uuid import uuid4
from datetime import datetime
import json


class BaseModel:
    """Root class defining all common attributes and methods"""

    def __init__(self, *args, **kwargs):
        """Initializes an instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            my_time = datetime.now()
            self.id = str(uuid4())
            self.created_at = my_time
            self.updated_at = my_time
            models.storage.new(self)

    def __str__(self):
        """User friendly name of the object"""
        my_name = str("[" + self.__class__.__name__ + "]")
        my_id = str("(" + self.id + ")")
        my_dict = str(self.__dict__)
        return (my_name + " " + my_id + " " + my_dict)

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary with keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return (new_dict)
