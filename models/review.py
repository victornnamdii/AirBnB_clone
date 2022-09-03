#!/usr/bin/python3
"""This module holds the review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Implementation of the review class"""

    place_id = ""
    user_id = ""
    text = ""
