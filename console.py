#!/usr/bin/python3
"""
This module contains the command line interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Implementation of the command line interpreter
    """

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Handling the EOF command"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
