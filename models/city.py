#!/usr/bin/python3
"""Defines City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel."""
    state_id = ""  # It will be the State.id
    name = ""
