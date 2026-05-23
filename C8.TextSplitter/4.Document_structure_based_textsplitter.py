# python code splitting

from langchain.text_splitter import RecursiveCharacterTextSplitter , Language

text="""# 🧱 Class Definition
class Car:
    # 🧰 Method Definition (Constructor)
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # 🚗 Method to display car info
    def display_info(self):
        print(f"This is a {self.brand} {self.model}.")

    # 🛣️ Method to simulate driving
    def drive(self):
        print(f"The {self.brand} {self.model} is now driving!")

# 🎯 Object Creation
my_car = Car("Toyota", "Camry")  # my_car is an object of class Car
second_car = Car("Honda", "City")

# 🔁 Method Calls using Object
my_car.display_info()   # Output: This is a Toyota Camry.
my_car.drive()          # Output: The Toyota Camry is now driving!

second_car.display_info()  # Output: This is a Honda City.
second_car.drive()         # Output: The Honda City is now_
"""

text_splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

chunks=text_splitter.split_text(text)

print(len(chunks))
print(chunks[1])