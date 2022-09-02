#!/usr/bin/python3
"""
This module contains the command line interpreter
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}


class HBNBCommand(cmd.Cmd):
    """
    Implementation of the command line interpreter
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handling the EOF command"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, line):
        """Creates a new instance and prints the id"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in classes:
            print("** class doesn't exist **")
            return False

        instance = classes[args[0]]()
        print(instance.id)
        instance.save()

    def do_show(self, line):
        """Prints an instance based on the class name and id"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in classes:
            print("** class doesn't exist **")
            return False

        if len(args) == 1:
            print("** instance id missing **")
            return False

        model = args[0] + "." + args[1]
        if model not in models.storage.all():
            print("** no instance found **")
            return False

        print(models.storage.all()[model])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in classes:
            print("** class doesn't exist **")
            return False

        if len(args) == 1:
            print("** instance id missing **")
            return False

        model = args[0] + "." + args[1]
        if model not in models.storage.all():
            print("** no instance found **")
            return False

        models.storage.all().pop(model)
        models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        hold = []
        args = shlex.split(line)
        if not args:
            for key in models.storage.all().keys():
                hold.append(str(models.storage.all()[key]))
        elif args[0] in classes:
            for key in models.storage.all().keys():
                if args[0] in key:
                    hold.append(str(models.storage.all()[key]))
        else:
            print("** class doesn't exist **")
            return False
        print(hold)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = shlex.split(line)[0:4]
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False

        model = args[0] + "." + args[1]
        if model not in models.storage.all():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            print("** value missing **")
            return False

        setattr(models.storage.all()[model], args[2], args[3])
        models.storage.all()[model].save()

    def default(self, line):
        """Called when a cmd prefix is unrecognized"""
        args = shlex.split(line)
        model, method = args[0].split(".")

        if method == "all()":
            self.do_all(model)
            return

        if method == "count()":
            count = 0
            for key in models.storage.all().keys():
                if model in key:
                    count += 1

            print(count)
            return

        if "show" in method:
            hold_id = method[5:-1]
            nmodel = model + " " + hold_id
            self.do_show(nmodel)
            return

        if "destroy" in method:
            hold_id = method[8:-1]
            nmodel = model + " " + hold_id
            self.do_destroy(nmodel)
            return
        
        if "update" in method:
            args = line.split(".")
            nmodel = model
            hold_args = args[1].split(",")

            if len(hold_args) > 0:
                hold_id = hold_args[0][8:-1]
                if len(hold_id) > 0 and hold_id[-1] == '"':
                    hold_id = hold_id.replace('"', '')
                nmodel += " " + hold_id
            if len(hold_args) > 1:
                hold_name = hold_args[1][2:-1]
                if hold_name[-1] == '"':
                    hold_name = hold_name.replace('"', '')
                nmodel += " " + hold_name
            if len(hold_args) > 2:
                hold_value = hold_args[2][2:-1]
                if hold_value[-1] == '"':
                    hold_value = hold_value.replace('"', '')
                nmodel += " " + hold_value
            
            self.do_update(nmodel)
            return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
