#!/usr/bin/python3
"""Defines FileStorage class."""

import datetime
import json
import os


class FileStorage:

    """Class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(cls):
        """Returns the dictionary __objects"""
        return cls.__objects

    @classmethod
    def new(cls, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        cls.__objects[key] = obj

    @classmethod
    def save(cls):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(cls.__file_path, "w", encoding="utf-8") as f:
            dic = {k: v.to_dict() for k, v in cls.__objects.items()}
            json.dump(dic, f)

    @classmethod
    def classes(cls):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    @classmethod
    def reload(cls):
        """Reloads the stored objects"""
        if not os.path.isfile(cls.__file_path):
            return
        with open(cls.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: cls.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            cls.__objects = obj_dict

    @classmethod
    def attributes(cls, classname):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
