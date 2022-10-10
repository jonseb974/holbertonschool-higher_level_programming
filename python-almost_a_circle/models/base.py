#!/usr/bin/python3
# base.py
""" Write the first class Base."""
from multiprocessing import dummy
import os.path
import json
import csv
from subprocess import list2cmdline
import turtle


class Base:
    """Represent the base model.

    Attributes:
        - private class attribute __nb_objects = 0
        - class constructor: def __init__(self, id=None)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation.

        Args:
            id (int): Identtity of the base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method returns JSON string represents
        list_dictionaries.

        Args:
            list_dictionaries (list of dict)
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """The class method writes JSON representation of list_objs.

        Args:
            list_objs (list of instances inherits of Base)
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))
            else:
                my_list_dict = []
                for i in list_objs:
                    my_list_dict.append(i.to_dictionary())
                return f.write(cls.to_json_string(my_list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Static method returns list of JSON string
        representation.

        Args:
            json_string (string representation of list of dictionaries)
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class metho returns instance with all attributes sets.
        Args:
            - **dictionary: random of args.
        """
        dummy = 0
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Class method returns list of instances.
        """
        filename = cls.__name__ + '.json'
        if os.path.exists(filename) is False:
            return []
        else:
            with open(filename, 'r', encoding='utf-8') as f:
                my_list = cls.from_json_string(f.read())
                my_list_inst = []
                for i in range(len(my_list)):
                    dummy = cls.create(**my_list[i])
                    my_list_inst.append(dummy)
                return my_list_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method serializes in CSV format.
        Args:
            - list_objs (list of instances inherits of Base)
        """
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fieldnames = ['id', 'size', 'x' 'y']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Class method deserializes in CVS format.
        """
        filename = cls.__name__ + '.csv'
        if os.path.exists(filename) is False:
            return []
        else:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                my_list_inst = []
                for row in reader:
                    for key, value in row.items():
                        row[key] = int(value)
                    dummy = cls.create(**row)
                    my_list_inst.apend(dummy)
            return my_list_inst

    @staticmethod
    def raw(list_rectangle, list_squares):
        """_summary_

        Args:
            list_rectangle (list): _description_
            list_squares (_type_): _description_
        """
        turtle.title("Welcome to the Turtle Geometry!")
        turtle.shape("turtle")
        turtle.color("#80ab3c")
        turtle.bgcolor("#faebbb")
        turtle.pensize(3)
        turtle.speed(2)

        turtle.pencolor("#0a3591")
        turtle.showturtle()
        turtle.penup()
        turtle.setpos(150, 200)
        turtle.write("Rectangle are drawing!", font=("Arial", 12, "normal"))
        turtle.pencolor("#0a3591")
        turtle.showturtle()
        turtle.penup()
        turtle.setpos(150, 200)
        turtle.write("Rectangle are drawing!", font=("Arial", 12, "normal"))

        turtle.pencolor("#168bb5")
        turtle.penup()
        turtle.setpos(150, 180)
        turtle.write("And Square now!!", font=("Arial", 12, "normal"))
        for position in list_squares:
            turtle.penup()
            turtle.goto(position.x, position.y)
            turtle.pendown()
            for square in range(2):
                turtle.forward(position.size)
                turtle.left(90)
                turtle.forward(position.size)
                turtle.left(90)
        turtle.penup()
        turtle.hideturtle()
        turtle.pencolor("#80ab3c")
        turtle.setpos(-150, -150)
        turtle.write("The Turtle Geometry is done! (Click to leave).",
                     font=("Arial", 17, "normal"))
        turtle.exitonclick()
