#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
 obj = all_objs[obj_id]
 print(obj)
print("-- Create a new User --")
my_user = User()
print("my_user without attr: ", my_user)
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)
print("-- Create a new State --")
state = State()
state.name = 'Nairobi'
state.save()
print(state)
print("-- Create a new City --")
city = City()
city.name = 'Kasarani'
city.state_id = state.id
city.save()
print(city)
