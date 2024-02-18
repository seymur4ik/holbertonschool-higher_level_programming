#!/usr/bin/python3
"""
Creating first class
"""
import turtle
import os
import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """toJson"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves JSON str to file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as fd:
            if list_objs is None:
                fd.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                fd.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Json -> Dict"""
        json_list = []

        if json_string is not None and json_string != '':
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """Dict -> Instance"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(13579, 24680)
        elif cls.__name__ == 'Square':
            dummy = cls(123456789)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """File -> Instance ?"""
        filename = "{}.json".format(cls.__name__)
        inst = []
        dictlist = []

        if os.path.exists(filename):
            with open(filename, "r") as fd:
                json = fd.read()
                dictlist = cls.from_json_string(json)
                for i in dictlist:
                    inst.append(cls.create(**i))
        return inst

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Oh My Gosh I write with turtle"""
        win = turtle.Screen()
        cur = turtle.Turtle()
        cur.speed(1)
        def side(s, cur):
            cur.right(90)
            cur.forward(s)

        for r in list_rectangles:
            cur.penup()
            cur.goto(r.x, r.y)
            cur.pendown()
            for i in range(4):
                if i % 2 == 0:
                    side(r.width, cur)
                else:
                    side(r.height, cur)

        for s in list_squares:
            cur.penup()
            cur.goto(s.x, s.y)
            cur.pendown()
            for i in range(4):
                side(s.size, cur)
