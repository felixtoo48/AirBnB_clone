#!/usr/bin/python3
"""
Program that contains the entry point
of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    def do_EOF(self, line):
        """EOF command to quit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
