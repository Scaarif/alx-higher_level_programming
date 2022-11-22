#!/usr/bin/python3
''' Testing the cmd module, a framework for command-line interfaces:
    i.e. a framwork for creating line-oriented command processors '''
import cmd
import sys


# define a class that extends the  cmd.Cmd class
class CLI(cmd.Cmd):
    ''' An example class, extends (inherits from) the cmd base:
    class (Cmd) '''
    # assign a custom prompt
    prompt = '(hbtn) '

    def __init__(self):
        cmd.Cmd.__init__(self)
        # self.prompt = '> '

    def do_hello(self, arg):
        ''' the hello command corresponding call method:
        this' the method that'll be called if a hello command is
        to be executed '''
        print('Hello again', arg, '!')

    def help_hello(self):
        ''' defines the help string: what'll be returned on command
        <help hello> '''
        print('syntax: hello [message]'),
        print('-- prints a hello message')

    def do_EOF(self, arg):
        ''' end of file: Ctrl + D handler '''
        print(),  # end with a new line
        return True

    def do_quit(self, arg):
        ''' the quit command call method implementation '''
        sys.exit(1)

    def help_quit(self):
        print('syntax: quit'),
        print('-- terminates the application')

    # shortcuts
    do_q = do_quit


# test the class
if __name__ == '__main__':
    cli = CLI()  # instantiate class
    cli.cmdloop()  # start cli loop (i.e. repeatedly prompt for commands)
