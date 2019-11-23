#!/usr/bin/python3
"""city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for create a new city"""
    state_id = ""
    name = ""
