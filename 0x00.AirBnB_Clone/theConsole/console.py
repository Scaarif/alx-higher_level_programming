#!/usr/bin/python3
""" Defines the entry point to the AirBnB Console project """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ Defines a line-oriented command processor
    (a command-line interface) that extends the cmd module """
    # assign a custom prompt
    prompt = '(hbtn) '

    # initialize object
    def __init__(self):
        """ Initializes class objects """
        # initialize super class (is this necessary)? No!
        cmd.Cmd.__init__(self)

    def do_quit(self, line):
        """ exits the program: <quit> call method implementation
        Args:
            line - each command call method (a do_x method)
            takes an argument containing the command to be executed
            and (potentially) the command's args """
        sys.exit(1)  # success

    def help_quit(self):
        """ quit help """
        print('syntax: quit\n--terminates the application')

    def do_EOF(self, line):
        """ exits the program: <Ctrl + D> call method implementation """
        print(),  # to exit properly(with a new line)
        return True  # to the cmdloop's stop flag

    def help_EOF(self):
        print('syntax: Ctrl + D\n--terminates the application')

    # override cmd.emptyline - re-executes last cmd if emptyline
    def emptyline(self):
        pass  # do nothing


# run the script if executed as main
if __name__ == '__main__':
    # instantiate class and run infinitely
    HBNBCommand().cmdloop()
