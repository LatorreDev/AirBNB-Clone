#!/usr/bin/python3
"""HBNBCommand Module"""

import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB"""
    prompt = "(hbnb)"

    def do_quit(self, args):
        """Quit command to exit the program"""
        return(True)

    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self):
        """EOF command to exit the program"""
        return(True)

    def help_EOF(self):
        """Help for EOF command"""
        print("EOF command to exit the program\n")

    def emptyline(self):
        """If there is no command entered and Return is pressed"""
        pass

    def do_create(self, args):
        """create a new instace of a class"""
        my_list = ["User", "City", "Amenity", "Name", "Place", "Review",
                   "BaseModel"]
        arg_eval = (args.split())
        if len(arg_eval) == 0:
            print("** class name missing **")
        elif arg_eval[0] in my_list:
            new_obj = eval(arg_eval[0])(arg_eval[1:])
            print(new_obj.id)
            new_obj.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """show the info of an instance of a class"""
        my_list = ["User", "City", "Amenity", "Name", "Place", "Review",
                   "BaseModel"]
        arg_eval = (args.split())
        if len(arg_eval) == 0:
            print("** class name missing **")
        elif arg_eval[0] in my_list:
            if len(arg_eval) == 1:
                print("** instance id missing **")
            else:
                models.storage.reload()
                my_args = arg_eval[0] + "." + arg_eval[1]
                if my_args in list(models.storage.all().keys()):
                    print(models.storage.all()[my_args])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """destroy a instance of a class"""
        my_list = ["User", "City", "Amenity", "Name", "Place", "Review",
                   "BaseModel"]
        arg_eval = (args.split())
        my_arg = arg_eval[0] + "." + arg_eval[1]
        temp_list = list(models.storage.all().keys())
        if len(arg_eval) == 0:
            print("** class name missing **")
        elif arg_eval[0] in my_list:
            if len(arg_eval) == 1:
                print("** instance id missing **")
            elif my_arg in temp_list:
                del models.storage.all()[my_arg]
                models.storage.save()
                print(arg_eval)
            else:
                print("** no instance found **")
                print(arg_eval)
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Show all objects from an instance"""
        temp_list = []
        my_list = ["User", "City", "Amenity", "Name", "Place",
                   "Review", "BaseModel"]
        arg_eval = (args.split())
        if arg_eval[0] in my_list:
            temp_dict = models.storage.all()
            for obj_id in temp_dict.keys():
                if arg_eval[0] in temp_dict:
                    obj = temp_dict[obj_id]
                    temp_list.append(str(obj))
            print(temp_list)
        else:
            print("** class name missing **")

    def do_update(self):
        """update the info of the objects in an instance"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
