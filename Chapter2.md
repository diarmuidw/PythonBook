# Chapter 2: Object Oriented Programming in Python

# Introduction to OOPs Concepts

Object-Oriented Programming (OOP) is a programming paradigm that focuses on the use of objects to design and build applications. OOP is based on the concept of objects, which can contain data and code to manipulate that data. Python is a powerful language that supports OOP concepts.

## Objects

In OOP, an object is an instance of a class. A class can be thought of as a blueprint for creating objects. Each object is unique, but it shares the same structure and behavior as other objects created from the same class. For example, a class called `Person` can be used to create objects that represent people. Each `Person` object would have attributes like `name`, `age`, and `gender`, and methods like `speak()` and `walk()`.

```python
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def speak(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")
    
    def walk(self):
        print(f"{self.name} is walking.")
    
p1 = Person("John", 25, "male")
p1.speak() # Output: "Hi, my name is John and I am 25 years old."
p1.walk() # Output: "John is walking."
```

## Encapsulation

Encapsulation is the idea of bundling data and methods together and hiding the implementation details from the user. This makes the code more modular and easier to maintain. In Python, encapsulation is achieved through the use of private and protected attributes and methods.

Private attributes and methods are indicated by using double underscores (`__`) before the name. These attributes and methods cannot be accessed directly from outside the class.

Protected attributes and methods are indicated by using a single underscore (`_`) before the name. These attributes and methods can be accessed from outside the class, but they are intended to be used only within the class or its subclasses.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")
            
    def get_balance(self):
        return self.__balance
    
acc1 = BankAccount(1000)
acc1.deposit(500)
acc1.withdraw(200)
print(acc1.get_balance()) # Output: 1300
```

## Inheritance

Inheritance is the idea of creating a new class from an existing class. The new class, known as the child class, inherits the attributes and methods of the parent class. In Python, inheritance is achieved by passing the parent class as an argument to the child class.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        pass
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "dog")
        
    def make_sound(self):
        print("Bark!")
        
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "cat")
        
    def make_sound(self):
        print("Meow!")
        
dog1 = Dog("Fido")
cat1 = Cat("Whiskers")
dog1.make_sound() # Output: "Bark!"
cat1.make_sound() # Output: "Meow!"
```

## Polymorphism

Polymorphism is the idea of using a single interface to represent different types of objects. In Python, polymorphism is achieved through the use of inheritance and method overriding.

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
        return 3.14 * (self.radius ** 2)
        
shapes = [Rectangle(5, 10), Circle(7)]
for shape in shapes:
    print(shape.area())
```

## Conclusion

In this section, we introduced the fundamental concepts of OOP in Python, including objects, encapsulation, inheritance, and polymorphism. These concepts provide a powerful and flexible way to design and build complex applications.# Chapter 2: Object Oriented Programming in Python

# Creating and Using Classes

Classes are the fundamental building blocks of Object-Oriented Programming in Python. A class is a user-defined blueprint for creating objects that encapsulate variables and functions. 

## Creating a Class

To create a class in Python, we use the `class` keyword followed by the name of the class. Let's create a simple `Person` class that holds the name and age of a person. 

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Here, we have defined a `Person` class with a constructor method `__init__` that takes two arguments: `name` and `age`. The `self` parameter refers to the instance of the class that we are creating. 

## Creating an Object

Once we have defined a class, we can create an instance of that class, which we call an object. We create an object using the class name followed by parentheses. Let's create a `Person` object and print its attributes. 

```python
person = Person("John", 30)
print(person.name)  # Output: John
print(person.age)  # Output: 30
```

Here, we have created a `Person` object named `person` with the name "John" and age 30. We can access the instance variables `name` and `age` using dot notation. 

## Adding Methods to a Class

We can also add methods to a class that operate on the instance variables. Let's add a `greet` method to the `Person` class that prints a greeting. 

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
```

Now, we can create a `Person` object and call the `greet` method. 

```python
person = Person("John", 30)
person.greet()  # Output: Hello, my name is John and I am 30 years old.
```

Here, we have created a `Person` object named `person` and called the `greet` method, which prints a greeting.

## Conclusion

In this section, we learned how to create a class in Python and create objects from that class. We also learned how to add methods to a class that operate on the instance variables. Classes are a powerful way to organize and encapsulate code in Python, and they are a fundamental concept in Object-Oriented Programming.# Chapter 2: Object Oriented Programming in Python

# Inheritance and Polymorphism

Inheritance is one of the pillars of Object-Oriented Programming (OOP) and allows for the creation of a new class that is a modified version of an existing class. The existing class is called the parent or base class, while the new class is called the child or derived class.

The derived class inherits all the properties and methods of the base class, which it can then modify or extend. This means that the derived class can be used in the same way as the base class, but with additional functionality.

Here is an example of inheritance:

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}"
    
    def make_sound(self):
        return "Meow!"

gizmo = Cat("Gizmo", "Siamese", "String")
print(gizmo)
print(gizmo.play())
print(gizmo.make_sound())
```

In this example, we create an `Animal` class with a `name` and `species` attribute, as well as a `make_sound` method. We then create a `Cat` class that inherits from `Animal` and adds a `breed` and `toy` attribute, as well as a `play` method. We also override the `make_sound` method to make it specific to a cat.

We then create a `Cat` object called `gizmo` and call its `play` and `make_sound` methods.

The output of the code would be:

```
Gizmo is a Cat
Gizmo plays with String
Meow!
```

Polymorphism is another important feature of OOP that allows objects of different types to be treated as if they were the same type. This is possible due to inheritance and the ability of objects to override or extend methods of their parent class.

Here is an example of polymorphism:

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        return f"{self.name} plays with {self.toy}"
    
    def make_sound(self):
        return "Meow!"

def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

cat = Cat("Gizmo", "Siamese", "String")
dog = Dog("Buddy", "Golden Retriever")

animal_sounds([cat, dog])
```

In this example, we create an `Animal`, `Dog`, and `Cat` classes just like in the previous example. However, we also create a `animal_sounds` function that takes a list of animals and calls their `make_sound` methods.

We then create a `Cat` object called `cat` and a `Dog` object called `dog`, and pass them both to the `animal_sounds` function.

Since both the `Cat` and `Dog` classes have a `make_sound` method, the `animal_sounds` function can be called on both objects, even though they are of different types. This is an example of polymorphism in action.

The output of the code would be:

```
Meow!
Woof!
```# Chapter 2: Object Oriented Programming in Python

# Magic Methods

Magic methods are special methods in Python classes that start and end with double underscores `__`. These methods provide a way to define customized behavior for objects of our class. Magic methods are also known as dunder methods.

Here are some commonly used magic methods in Python:

- `__str__(self)` - This method is called when we use the `print()` function on an object. It returns a string representation of the object.
- `__repr__(self)` - This method is called when we use the `repr()` function on an object. It returns an unambiguous string representation of the object.
- `__len__(self)` - This method is called when we use the `len()` function on an object. It returns the length of the object.
- `__getitem__(self, key)` - This method is called when we use the square bracket notation on an object to access an item by its key. It returns the value corresponding to the key.
- `__setitem__(self, key, value)` - This method is called when we use the square bracket notation on an object to set the value of an item by its key.
- `__delitem__(self, key)` - This method is called when we use the `del` keyword to delete an item from an object by its key.

Let's see an example of using magic methods in a class:

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        return self.pages
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        setattr(self, key, value)
    
    def __delitem__(self, key):
        delattr(self, key)
```

In this example, we have defined the magic methods `__str__()`, `__repr__()`, `__len__()`, `__getitem__()`, `__setitem__()`, and `__delitem__()`. 

Now we can create an instance of the `Book` class and use these methods to customize its behavior:

```python
>>> book = Book("The Alchemist", "Paulo Coelho", 208)
>>> print(book)  # Output: The Alchemist by Paulo Coelho
>>> repr(book)  # Output: "Book('The Alchemist', 'Paulo Coelho', 208)"
>>> len(book)  # Output: 208
>>> book['title']  # Output: 'The Alchemist'
>>> book['author']  # Output: 'Paulo Coelho'
>>> book['pages']  # Output: 208
>>> book['price'] = 10.99
>>> book['price']  # Output: 10.99
>>> del book['price']
``` 

In this example, we have used the `__str__()`, `__repr__()`, `__len__()`, `__getitem__()`, `__setitem__()`, and `__delitem__()` methods to provide customized behavior for the `Book` class.# Chapter 2: Object Oriented Programming in Python

# Properties and Class Methods

In object-oriented programming, properties are used to access and modify class attributes. Properties are used to provide an interface for accessing an object's attributes. In Python, the `@property` decorator is used to define properties. 

```python
class Square:
    def __init__(self, side):
        self.side = side
    
    @property
    def area(self):
        return self.side ** 2
```

In the above example, `area` is a property of the `Square` class. It returns the area of the square, which is calculated using the `side` attribute.

Class methods, on the other hand, are methods that are bound to the class and not the instance of the class. They are typically used to manipulate the class itself or to perform some operation on the class. In Python, the `@classmethod` decorator is used to create class methods.

```python
class Square:
    number_of_squares = 0
    
    def __init__(self, side):
        self.side = side
        Square.number_of_squares += 1
    
    @property
    def area(self):
        return self.side ** 2
    
    @classmethod
    def get_number_of_squares(cls):
        return cls.number_of_squares
```

In the above example, `get_number_of_squares` is a class method that returns the number of squares that have been created. It does this by accessing the `number_of_squares` attribute of the `Square` class, which is incremented in the `__init__` method.

In conclusion, properties and class methods are powerful tools in object-oriented programming that allow for flexible and efficient manipulation of class attributes and behavior.# Chapter 2: Object Oriented Programming in Python

# Abstract Classes and Interfaces

In Python, we can declare abstract classes and interfaces using the `abc` module. 

An *abstract class* is a class that cannot be instantiated, and is used as a template for other classes to inherit from. It contains one or more abstract methods, which have no implementation in the abstract class, but must be implemented by any concrete subclass.

An *interface* is a special type of abstract class that only contains abstract methods. Interfaces define a contract that classes can implement, ensuring that they have certain methods with specified parameters and return types.

Here's an example of an abstract class:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```

In the above example, we have defined an abstract class `Shape` that defines two abstract methods - `area` and `perimeter`. Any subclass of `Shape` must implement these methods, or else it will also become an abstract class and cannot be instantiated.

Here's an example of an interface:

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass
```

In this example, we have defined an interface `Drawable` that defines a single abstract method `draw`. Any class that implements `Drawable` must implement the `draw` method.

Note that Python does not have any keyword to denote an interface, and we use an abstract class with only abstract methods to define an interface.

Abstract classes and interfaces are useful for defining a contract that classes must adhere to, ensuring consistency and providing a clear structure to our code.