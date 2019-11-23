#!/usr/bin/python3
"""Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for create a new review"""
    place_id = ""
    user_id = ""
    text = ""
