#!/usr/bin/python3
"""A module that contains the entry point of the command interpreter"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines an interpreter"""

    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    prompt = '(hbnb) '

    def emptyline(self):
        """Doesn't execute an empty line + ENTER"""
        pass

    def do_quit(self, line):
        """exit the program"""
        return True

    def help_quit(self):
        """A handler that provides information for the command quit"""
        print('Quit command to exit the program')

    def do_EOF(self, line):
        """exit the program"""
        return True

    def help_EOF(self):
        """A handler that provides information for the command EOF"""
        print('Quit command to exit the program')

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg in self.classes:
            for key, value in self.classes.items():
                if key == arg:
                    new_instance = self.classes[key]()
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance
            based on the class name and id
        """
        args = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) >= 1:
            try:
                my_objects = FileStorage.all(self)
                my_key = args[0] + "." + args[1]
                flag = 0
                for key, values in my_objects.items():
                    if key == my_key:
                        flag = 1
                        print(values)
                if flag == 0:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
            (save the change into the JSON file)
        """
        args = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) >= 1:
            try:
                my_objects = FileStorage.all(self)
                my_key = args[0] + "." + args[1]
                try:
                    my_objects.pop(my_key)
                    storage.save()
                except KeyError:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_all(self, arg):
        """ Prints all string representation of all instances
            based or not on the class name
        """
        args = arg.split(" ")
        if not arg:
            my_list = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                my_list.append(str(values))
            print(my_list)
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            my_list = []
            my_objects = FileStorage.all(self)
            for key, values in my_objects.items():
                my_key = key.split(".")
                if my_key[0] == args[0]:
                    my_list.append(str(values))
            print(my_list)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by
            adding or updating attribute (save the change into the JSON file)
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            my_objects = FileStorage.all(self)
            my_key = args[0] + "." + args[1]
            flag = 0
            for key, values in my_objects.items():
                if key == my_key:
                    flag = 1
                    my_values = my_objects.get(key)
                    setattr(values, args[2], args[3])
                    values.save()
            if flag == 0:
                print("** no instance found **")
