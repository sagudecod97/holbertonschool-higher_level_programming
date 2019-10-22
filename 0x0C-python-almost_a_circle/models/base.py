#!/usr/bin/python3
import json
import csv

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
        if json_string is None:
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
            list_w = []
            if list_objs == None:
                f.write("[]")
            else:
                for listObj in list_objs:
                    json_write = listObj.to_dictionary()
                    list_w.append(json_write)

                f.write(cls.to_json_string(list_w))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 1, 1)
        else:
            dummy = cls(1, 1, 1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        try:
            with open("{}.json".format(cls.__name__), 'r', encoding="utf-8") as f:
                list_ret = []

                read_f = f.read()
                new_f = cls.from_json_string(read_f)
                for elem in new_f:
                    elem_app = cls.create(**elem)
                    list_ret.append(elem_app)
                return list_ret

        except:
            return []

    """
    Serialize and deseriliaze CSV
    """
    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open("{}.csv".format(cls.__name__), 'w') as f:
            count = 0

            if cls.__name__ == "Rectangle":
                fieldnames = ["width", "height", "x", "y", "id"]
                keys = {"width":"width","height": "height", "x":"x", "y":"y","id":"id"}
            else:
                fieldnames = ["size", "x", "y", "id"]
                keys = {"size":"size","x":"x","y":"y","id":"id"}

            file_writer = csv.DictWriter(f, fieldnames = fieldnames)
            for elem in list_objs:
                if count == 0:
                   file_writer.writerow(keys)
                   count += 1
                file_writer.writerow(elem.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        with open("{}.csv".format(cls.__name__), 'r') as f:
            ret_dic = {}
            arr_inst = []

            csv_reader = csv.DictReader(f)
            for elem in csv_reader:
                for key, value in elem.items():
                    ret_dic[key] = int(value)
                inst = cls.create(**ret_dic)
                arr_inst.append(inst)

            return arr_inst
