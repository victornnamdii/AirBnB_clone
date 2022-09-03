#!/usr/bin/python3
"""
This module contains the command line interpreter
"""

import cmd
import models
from models.engine.file_storage import classes
import shlex

integers = ["number_rooms", "number_bathrooms", "max_guest",
            "price_by_night"]

floats = ["latitude", "longitude"]


class HBNBCommand(cmd.Cmd):
    """
    Implementation of the command line interpreter
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handling the EOF command"""
        print()
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

        if args[2] in integers:
            args[3] = int(args[3])

        if args[2] in floats:
            args[3] = float(args[3])

        setattr(models.storage.all()[model], args[2], args[3])
        models.storage.all()[model].save()

    def default(self, line):
        """Called when a cmd prefix is unrecognized"""
        if "." not in line:
            super().default(line)
            return

        model, method = line.split(".")

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
            self.do_show(f"{model} {hold_id}")
            return

        if "destroy" in method:
            hold_id = method[8:-1]
            self.do_destroy(f"{model} {hold_id}")
            return

        if "update" in method:
            args = line.split(".")
            if args[1] == "update()":
                self.do_update(model)
                return
            u_args = eval(args[1][7:-1])

            if isinstance(u_args[1], dict):
                id, attr = u_args
                for key, value in attr.items():
                    self.do_update(f"{model} {id} {key} {value}")
                return

            if type(u_args) != str:
                u_args = " ".join(u_args)

            self.do_update(f"{model} {u_args}")
            return

        super().default(line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
