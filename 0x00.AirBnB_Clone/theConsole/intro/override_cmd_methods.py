#!/usr/bin/python3
import cmd


class Illustrate(cmd.Cmd):
 "Illustrate the base class method use."
 
 def cmdloop(self, intro=None):
     print('cmdloop({})'.format(intro))
     return cmd.Cmd.cmdloop(self, intro)
 
 def preloop(self):
    print('preloop()')
 
 def postloop(self):
    print('postloop()')
 
 def parseline(self, line):
    print('parseline({}) =>'.format(line)),
    ret = cmd.Cmd.parseline(self, line)
    print(ret)
    return ret
 
 def onecmd(self, s):
    print('onecmd({})'.format(s))
    return cmd.Cmd.onecmd(self, s)
 def emptyline(self):
    print('emptyline()')
    # return cmd.Cmd.emptyline(self)
    pass  # override behaviour by doing nothing
 
 def default(self, line):
    print(f'default({line})')
    return cmd.Cmd.default(self, line)
 
 def precmd(self, line):
    print(f'precmd({line})')
    classes = ['User', 'State']
    for obj in classes:
        if line.startswith(obj):
            commands = line.split('.')
            print(commands)
            commands[1] = commands[1].strip('()')
            print(commands[1])
            line = ' '.join(reversed(commands))
    return cmd.Cmd.precmd(self, line)
 
 def postcmd(self, stop, line):
    print(f'postcmd({stop}, {line})')
    if '[' in line:
        cmd.Cmd.onecmd(self, line)
    return cmd.Cmd.postcmd(self, stop, line)
 
 def do_greet(self, line):
    print('hello,', line)
 
 def do_EOF(self, line):
    "Exit"
    return True
if __name__ == '__main__':
 Illustrate().cmdloop('Illustrating the methods of cmd.Cmd')
