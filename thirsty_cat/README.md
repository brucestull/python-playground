# Thirsty Cat

## Modules

### `bottles.py`

### `table.py`

## Description

This is a simple game where you have to help a cat to drink water. The cat is very thirsty and it needs to drink water as soon as possible. The cat is in a maze and it needs to find the water bottle. The cat can move in four directions: up, down, left and right. The cat can't go through walls. The walls are

## Python Concepts

* Module:
    * A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended.
* Class:
    * A class is a code template for creating objects. Objects have member variables and have behaviour associated with them. In python a class is created by the keyword `class`. An object is created using the constructor of the class. This object will then be called the instance of the class. In Python we create instances in the following manner

        ```python
        instance = class(arguments)
        ```
* Constructor:
    * A constructor is a special kind of method that Python calls when it instantiates an object using the definitions found in your class. Python relies on the constructor to perform tasks such as initializing (assigning values to) any instance variables that the object will need when it starts. Constructors can also verify that there are enough resources for the object and perform any other start-up task you can think of.
* Instance:
    * An instance is a specific realization of any object. An object may be varied in a number of ways. Each realized variation of that object is an instance. The creation of a realized instance is called instantiation.
* Method:
    * A method is a function that “belongs to” an object. (In Python, the term method is not unique to class instances: other object types can have methods as well. For example, list objects have methods called append, insert, remove, sort, and so on. However, in the following discussion, we’ll use the term method exclusively to mean methods of class instance objects, unless explicitly stated otherwise.)
* Function:
    * A function is a block of code which only runs when it is called. You can pass data, known as arguments, into a function. A function can return data as a result.
* Compare `method` and `function`:
    * A function is a piece of code that is called by name. It can be passed data to operate on (i.e. the parameters) and can optionally return data (the return value). All data that is passed to a function is explicitly passed.
    * A method is a piece of code that is called by a name that is associated with an object. In most respects it is identical to a function except for two key differences:
        * A method is implicitly passed the object on which it was called.
        * A method is able to operate on data that is contained within the class (remembering that an object is an instance of a class - the class is the definition, the object is an instance of that data).
* Object:
    * An object is a component of a program that knows how to perform certain actions and how to interact with other elements of the program. Objects are the basic units of object-oriented programming.
* Attribute:
    * An attribute is a specification that defines a property of an object, element, or file. It may also refer to or set the specific value for a given instance of such. For clarity, attributes should more correctly be considered metadata.
* Inheritance:
* Encapsulation:
* Polymorphism:
* Abstraction:
* `__init__`:
    * The `__init__` method is roughly what represents a constructor in Python. When you call `A()`, Python creates an object for you, and passes it as the first parameter to the `__init__` method. Any additional parameters (e.g., `A(24, 'Hello')`) will also get passed as arguments--in this case causing an exception to be raised, since the constructor isn't expecting them.