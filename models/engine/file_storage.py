#!/usr/bin/python3

"""FileStorage Module"""

from models.base_model import BaseModel
import json
import os


class FileStorage:
    """Serializes instances to JSON file and also the reverse"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[str(obj.__class__.__name__ + "." + obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        update_dict = {}
        temp_dict = self.__objects
        for key, value in temp_dict.items():
            update_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as my_open:
            json.dump(update_dict, my_open)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        exists = os.path.isfile(self.__file_path)
        if exists:
            with open(self.__file_path) as my_load:
                data_load = json.load(my_load)
            for key in data_load.values():
                my_new_class = key["__class__"]
                del key["__class__"]
                self.new(eval(my_new_class)(**key))
        else:
            return self.__objects

    def delete(self, class_name, id):
        """Delete an instance from storage"""
        FileStorage.__objects.pop("{}.{}".format(class_name, id))
        self.save()
