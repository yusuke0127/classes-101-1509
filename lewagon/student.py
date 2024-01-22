from datetime import date
import os 

class Student:
    # Constructor function
    def __init__(self, name, age) -> None:
        self.name = name.capitalize()
        self.age = age
        
    # Instance method
    def say(self, something):
        print(f"{self.name} says {something}")

    # Class method
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

yann = Student('yann', 21)
print(yann.__dict__)
print(yann.say('hi'))
# print(__file__)
# print(os.path.abspath(__file__)) # refers to the absolute path of the file)