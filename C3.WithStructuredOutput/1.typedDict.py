from typing import TypedDict

class person(TypedDict):
    name: str
    age: int
    email: str

p1:person={"name":"John Doe",
    "age":"30",
    "email":"rk2@gmail.com"}

print(p1)
p2=person(name="Jane Smith", age=25, email="rk")

print(p2)

#Q1.what to use TypedDict?
# A1.TypedDict is used to define a dictionary with a specific structure, where each key has a defined type.
# It allows for better type checking and code clarity, especially when working with complex data structures.
#Q2.what is the difference between TypedDict and Dict?

# A2.TypedDict is a subclass of Dict that allows you to define the types of the keys and values in the dictionary.
# Dict is a more general type that does not enforce any specific structure or types for its keys.


