#!/usr/bin/python3

class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        i = 0

        if type(attrs) == list:
            for item in range(len(attrs)):
                if type(attrs[item]) == str:
                    i += 1

            if i == len(attrs) and type(attrs) == list:
                new_dic = {}
                self_dic = self.__dict__

                for key in self_dic.keys():
                    if key in attrs:
                        new_dic[key] = self_dic[key]
                return new_dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        return self.__dict__.update(json)
