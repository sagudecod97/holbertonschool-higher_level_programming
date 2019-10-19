#!/usr/bin/python3
import json

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    """
    Static and Class methods
    """

    @staticmethod
    def from_json_string(json_string):
        if json_string == None:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open("{}.json".format(cls.__name__), 'w+', encoding="utf-8") as f:
            if list_objs == None:
                f.write("[]")
            else:
                for listObj in list_objs:
                    json_write = cls.to_json_string([listObj.to_dictionary()])
                    f.write(json_write)
