# Classes and Object-Oriented Programming in Python

class Animal:
    # Class variable (shared by all instances)
    kingdom = "Animalia"

    def __init__(self, name, species, age):
        # Instance variables
        self.name = name
        self.species = species
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound."

    def describe(self):
        return f"{self.name} is a {self.species}, age {self.age}."

    # String representation
    def __str__(self):
        return f"Animal({self.name}, {self.species})"

    # Representation for debugging
    def __repr__(self):
        return f"Animal(name={self.name!r}, species={self.species!r}, age={self.age})"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, "Dog", age)
        self.breed = breed

    def speak(self):
        return f"{self.name} says: Woof!"

    def fetch(self, item):
        return f"{self.name} fetched the {item}!"


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Cat", age)

    def speak(self):
        return f"{self.name} says: Meow!"


# Create objects
dog = Dog("Rex", 3, "Labrador")
cat = Cat("Whiskers", 5)

print(dog.describe())
print(dog.speak())
print(dog.fetch("ball"))

print(cat.describe())
print(cat.speak())

# Polymorphism
animals = [dog, cat, Animal("Parrot", "Bird", 2)]
for animal in animals:
    print(animal.speak())

# Class variable
print(f"Kingdom: {Dog.kingdom}")

# isinstance and issubclass
print(f"dog is Animal: {isinstance(dog, Animal)}")
print(f"Dog is subclass of Animal: {issubclass(Dog, Animal)}")

# __str__ and __repr__
print(str(dog))
print(repr(cat))
