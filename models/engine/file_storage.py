#!/usr/bin/python3
"""
This module containsa class FileStorage
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    Implementation of the class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        if not obj:
            return
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_obj, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists
        """
        try:
            with open(self.__file_path, 'r') as f:
                json_obj = json.load(f)
            for key in json_obj:
                self.__objects[key] = BaseModel(**json_obj[key])
        except Exception:
            pass
