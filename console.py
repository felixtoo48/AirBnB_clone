#!/usr/bin/python3
"""
Program that contains the entry point
of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ command interpreter to interact with the storage"""
    prompt = "(hbnb)"

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt.

        If this method is not overridden, it repeats the last nonempty
        command entered.

        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_EOF(self, line):
        """EOF command to quit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
