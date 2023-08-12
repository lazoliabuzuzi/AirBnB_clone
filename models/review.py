#!/usr/bin/python3
"""Defines Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    place_id = ""  # It will be the Place.id
    user_id = ""   # It will be the User.id
    text = ""
