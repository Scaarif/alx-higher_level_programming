#!/usr/bin/python3
""" Encoding a class (an example of serializing a custom 
python object ) """
import json
from json import JSONEncoder


class Student:
    """ sample class creating a student """
    def __init__(self, name, roll_no, address):
        self.name = name
        self.roll_no = roll_no
        self.address = address
    
    def say_hi(self):
        """ greet the student """
        print("Hello,", self.name, "!")

    def to_json(self):
        """ serializes (decodes) an instance of the class """
        return json.dumps(self, indent = 4, default=lambda o: o.__dict__)

class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin
# Alternatively, define a class that extends JSONEncoder (use the class with dumps)
class EncodeStudent(JSONEncoder):
    def default(self, o):
        """ the method to encode a class instance
        args:
            o: the object (class instance) to encode 
        """
        # essentially does the same thing as the to_json() method
        return o.__dict__  

# test the two classes by encoding an instance of Student
address = Address('Nairobi', 'Saika', 203001)
student = Student('Rahab',  53, address)
# Encoding
#student_json = student.to_json()
student_json = json.dumps(student, indent = 4, cls = EncodeStudent)
print('student_json:', student_json)
print(type(student_json))

# Decoding
student = json.loads(student_json)
print('student:',student)
print(type(student))
