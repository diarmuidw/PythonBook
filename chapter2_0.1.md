# Introduction to OOPs Concepts

Object-Oriented Programming (OOP) is a programming paradigm that is based on the concept of "objects", which can contain data and code that operate on that data. In OOP, everything is treated as an object that has a state (variables) and a behavior (methods/functions).

The main benefit of OOP is that it allows us to organize our code into reusable, modular units. These units can be easily extended and modified without affecting the rest of the codebase. 

For example, let's say you're building a game. You can create a class called "Player" that contains all the necessary attributes and methods to represent a player in the game. This class can then be reused for all the players in the game, without the need to write redundant code.

Another important concept in OOP is encapsulation. Encapsulation refers to the practice of hiding the implementation details of a class or method from the outside world. This is done by making certain variables and methods private or protected. 

For instance, let's take the example of a bank account. The account balance is a private variable that is accessible only through the methods of the account class. This way, no one can directly modify the account balance without going through the appropriate methods.

Overall, OOP is a powerful tool for building complex, scalable, and maintainable software systems. By encapsulating data and functionality in well-defined objects, we can write code that is easier to reason about and modify, which leads to more robust and effective applications.## Creating and Using Classes

Classes are the cornerstone of object-oriented programming. A class is a blueprint or a template for creating objects. It defines a set of properties and methods that are common to a group of objects.

In Python, you can create a class using the `class` keyword followed by the name of the class. Here's an example:

```python
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def start(self):
        print(f"{self.make} {self.model} is starting...")

    def stop(self):
        print(f"{self.make} {self.model} is stopping...")
```

In this example, we've defined a `Car` class with four properties (`make`, `model`, `year`, and `color`) and two methods (`start` and `stop`). The `__init__` method is a special method that is called when the object is created. It initializes the properties of the object with the values passed in as parameters.

To create an instance of the `Car` class, we simply call the `Car` constructor and pass in the required parameters:

```python
my_car = Car("Toyota", "Camry", 2021, "red")
```

We can then access the properties and methods of the `my_car` object:

```python
print(my_car.make)   # Output: Toyota
print(my_car.color)  # Output: red

my_car.start()       # Output: Toyota Camry is starting...
my_car.stop()        # Output: Toyota Camry is stopping...
```

As you can see, classes make it easy to create objects with common properties and methods. They are a powerful tool for organizing and structuring your code.# Inheritance and Polymorphism

Inheritance is a powerful object-oriented programming concept where a new class is created by inheriting the properties of an existing class. The class that is being inherited from is called the parent or base class, and the new class is called the child or derived class. This allows the child class to reuse the code of the parent class and add its own functionality.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow"

pets = [Dog("Rufus"), Cat("Mittens"), Dog("Buddy")]

for pet in pets:
    print(f"{pet.name} says {pet.speak()}")
```

In the above example, we have a parent class `Animal` with a `speak()` method which raises a `NotImplementedError`. This means that the method must be implemented by any child class that inherits from `Animal`. We then have two child classes, `Dog` and `Cat`, which implement their own `speak()` methods. Finally, we create three instances of our child classes and store them in a list. We then iterate over the list and call the `speak()` method on each instance, which returns the appropriate animal sound.

Polymorphism is another concept that goes hand-in-hand with inheritance. It allows objects of different types to be treated as if they were objects of the same type. This means that we can use a single interface to represent multiple classes. Polymorphism is achieved through inheritance and method overriding.

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(5, 10), Circle(7)]

for shape in shapes:
    print(f"The area of this shape is {shape.area()}")
```

In the above example, we have a parent class `Shape` with an `area()` method that is not implemented. We then have two child classes, `Rectangle` and `Circle`, which inherit from `Shape` and implement their own `area()` methods. Finally, we create a list of shapes and iterate over them, calling the `area()` method on each shape. Since each shape has its own implementation of the `area()` method, we get the correct area for each shape. This is an example of polymorphism.# Magic Methods

In Python, there are certain methods which have double underscores before and after their names called Magic Methods. These methods are special methods that allow us to perform certain operations on Python objects. They are also known as dunder methods.

Some common magic methods are:

- \_\_init\_\_ : This method is called the constructor method and is used to initialize the object.
- \_\_str\_\_ : This method returns the string representation of an object.
- \_\_len\_\_ : This method is used to get the length of the object.
- \_\_add\_\_ : This method is used to add two objects.
- \_\_eq\_\_ : This method is used to compare two objects for equality.

Here's an example demonstrating the use of magic methods:

```python
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def __len__(self):
        return 2

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return Complex(real, imaginary)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

c1 = Complex(1, 2)
c2 = Complex(2, 3)

print(len(c1)) # Output: 2
print(c1 + c2) # Output: 3 + 5i
print(c1 == c2) # Output: False
```

In the above example, we have defined a Complex class and have used magic methods to define various operations. The `__str__` method is used to return a string representation of the object. The `__len__` method is used to return the length of the object. The `__add__` method is used to add two complex numbers, and the `__eq__` method is used to check if two complex numbers are equal or not.# Properties and Class Methods

Properties and Class Methods are advanced OOP concepts that allow you to fine-tune the behavior of your classes.

## Properties

A property is a way to get and set the value of an instance variable. In Python, it's common to use underscore-based naming conventions for instance variables that are not meant to be accessed outside of the class. Properties provide an abstraction on top of these variables, allowing you to control the way they are accessed.

Here's an example:

```python
class Car:
    def __init__(self, make, model):
        self._make = make
        self._model = model

    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, value):
        self._make = value

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value):
        self._model = value

car = Car('Toyota', 'Corolla')
print(f"Make: {car.make}, Model: {car.model}")

car.make = 'Honda'
car.model = 'Civic'
print(f"Make: {car.make}, Model: {car.model}")
```

In the above example, we define two instance variables `_make` and `_model` in the constructor. We then define two properties `make` and `model` using the `@property` decorator. The `@make.setter` and `@model.setter` decorators allow us to define a custom setter method for each property.

When we access `car.make` and `car.model`, we are actually calling the getter methods for the properties, which return the values of the instance variables `_make` and `_model`. When we set `car.make` and `car.model`, we are calling the setter methods for the properties, which set the values of the instance variables.

Properties provide a way to control the way instance variables are accessed, without changing the API of the class. For example, if we decided to change the name of the `_make` instance variable to `_manufacturer`, we could do so without affecting any code that depends on the `make` property.

## Class Methods

Class methods are methods that are bound to the class, rather than an instance of the class. They are defined using the `@classmethod` decorator.

Here's an example:

```python
class Car:
    num_wheels = 4

    @classmethod
    def get_num_wheels(cls):
        return cls.num_wheels

print(Car.get_num_wheels())
```

In the above example, we define a class method `get_num_wheels` using the `@classmethod` decorator. When we call `Car.get_num_wheels()`, the `cls` parameter is set to the `Car` class itself, and we can access the `num_wheels` class variable using `cls.num_wheels`.

Class methods are useful for defining methods that operate on the class itself, rather than individual instances of the class. For example, we could define a class method that returns the number of cars that have been created from the class.

## Conclusion

Properties and Class Methods are powerful tools for fine-tuning the behavior of your classes. They allow you to control the way instance variables are accessed, and define methods that operate on the class itself.# Abstract Classes and Interfaces

Python supports Abstract Base Classes (ABCs) and interfaces similar to other Object Oriented Programming languages. Abstract classes define a basic structure for other classes to follow, but cannot be instantiated themselves. They provide a way to define a blueprint of methods that must be implemented by subclasses.

Abstract classes can be used to ensure that subclasses implement all necessary methods, while also allowing for the flexibility to define other methods unique to each subclass. One example of an abstract class in Python is the `abc.ABC` class:

```python
import abc

class MyAbstractClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def my_method(self):
        pass
```

This creates an abstract class `MyAbstractClass` with an abstract method `my_method`. Any subclass of `MyAbstractClass` must implement `my_method`, otherwise it will raise an error.

Interfaces in Python can also be created using ABCs. An interface is a set of methods that must be implemented by a class, but without any implementation details. These methods only define the method signature, which includes the name, parameters, and return type.

```python
import abc

class MyInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def my_method(self, arg1: int, arg2: str) -> bool:
        pass
```

This creates an interface `MyInterface` with an abstract method `my_method`. Any class that implements `MyInterface` must implement `my_method` with the same method signature.

Overall, abstract classes and interfaces provide a way to define a set of rules that must be followed by subclasses or implementing classes, while still allowing for flexibility in implementation.