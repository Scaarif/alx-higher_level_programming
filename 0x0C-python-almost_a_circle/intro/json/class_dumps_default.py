#!/usr/bin/python3
""" Encoding a class (an example of serializing a custom 
python object ) """
import json


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

# test the two classes by encoding an instance of Student
address = Address('Nairobi', 'Saika', 203001)
student = Student('Rahab',  53, address)
# Encoding
student_json = student.to_json()
print('student_json:', student_json)
print(type(student_json))

# Decoding
student = json.loads(student_json)
print('student:',student)
print(type(student))
