
# coding: utf-8

# In[ ]:

'''
In this lecture, we will discuss abstract classes and design patterns. 
'''


# In[ ]:

'''
Abstract Base Class (ABC) - This is similar to interfaces in C#

http://pymotw.com/2/abc/

Abstract classes are used to define a signature that will be implemented by 
all the classes that inherit it. For example, let us say that two programming 
groups have to read and write into files but how they read and write method 
may differ. In such cases we can have read and write method signature in the 
abstract class and the two groups can inherit from the abstract class and 
create their own concrete classes.
'''


# In[ ]:

# This is an example of an abstract class without importing any special module
class AbstractImage():
    def read(self):
        raise NotImplementedError()
    def write(self):
        raise NotImplementedError()
'''
Here the abstract class AbstractImage has the methods that consist of signature 
that all the child classes will inherit. We are raising not implemented error to 
say that the methods by themselves are not doing anything until implemented by a child class.
'''        

ai = AbstractImage()
print ai
ai.read()


# In[ ]:

# This is an example of an abstract class created by importing a module called abc
import abc
class AbstractImage():
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def read(self):
        return       
    @abc.abstractmethod
    def write(self):
        return
    
ai = AbstractImage()
print ai # Will give an error that it cannot create an instance of the abstract class
#ai.read()


# In[ ]:

class AbstractDicom():
    def read(self):
        raise NotImplementedError()
    def write(self):
        print "write in main class"
        raise NotImplementedError()
    
class Dicom(AbstractDicom):
    def read(self):
        print "reading file"
        
d = Dicom()
print d
d.read() # Makes the call to Dicom child class
d.write() 
# First makes the call to Dicom child class. But since this is not implemented in the 
# child class the write method in the parent class will be called and 'NotImplementedError' 
# will be raised.


# In[ ]:

class AbstractDicom():
    def read(self):
        raise NotImplementedError()
    def write(self):
        print "write in main class"
        raise NotImplementedError()
    
class Dicom(AbstractDicom):
    def read(self):
        print "reading file"
    def write(self):
        print "writing file"
        
d = Dicom()
print d
d.read() # Makes the call to Dicom child class
d.write() # Makes the call to Dicom child class


# In[ ]:

# If the line @abc.abstractmethod is commented, you will notice that if the
# method is not implemented in the child, the parent class write method will be called.

import abc
class AbstractDicom():
    #__metaclass__ = abc.ABCMeta
    #@abc.abstractmethod
    #def read(self):
    #    return       
    #@abc.abstractmethod
    def write(self):
        print "inside the base write method"
        return
    
class Dicom(AbstractDicom):
    def read(self):
        print "reading file"
    #def write(self):
    #    print "writing file"
        
d = Dicom()
print d
d.read()
d.write()


# In[ ]:

'''
Design Patterns is a general repeatable solution to a commonly occurring problem in software design. 
It is a description or template for how to solve a problem that can be used in many different situations.
https://sourcemaking.com/design_patterns

Two design patters that we will consider are:
    Proxy pattern
    Factory pattern
'''


# In[ ]:

'''
The syntax for Proxy pattern is 

class Proxy:
    def __init__(self,subject):
        self.__subject = subject
    def __getattr__(self,name):
        return getattr( self.__subject, name )   

'''


# In[ ]:

# Proxy Pattern is used when an object has to be shielded from its clients.

class ConcreteImplementation1:
    def a(self):
        print("Calling a1")
    def b(self):
        print("Calling b1")
    def c(self):
       print("Calling c1")
        
class ConcreteImplementation2:
    def a(self):
        print("Calling a2")
    def b(self):
        print("Calling b2")
    def c(self):
       print("Calling c2")

class Proxy:
    def __init__(self):
        # Change the call to ConcreteImplementation1() to see the result
        self.__implementation = ConcreteImplementation2()
    def __getattr__(self, name):
        return getattr(self.__implementation, name)

p = Proxy()
p.a(); p.b(); p.c();


# In[ ]:

# Proxy Pattern

class ConcreteImplementation1:
    def a(self):
        print("Calling a1")
    def b(self):
        print("Calling b1")
    def c(self):
       print("Calling c1")
        
class ConcreteImplementation2:
    def a(self):
        print("Calling a2")
    def b(self):
        print("Calling b2")
    def c(self):
       print("Calling c2")

class Proxy:
    def __init__(self,name):
        self.__implementation = eval(name)()
    def __getattr__(self, name):
        return getattr(self.__implementation, name)

# Change the call to ConcreteImplementation2 to see the result
p = Proxy('ConcreteImplementation1')
p.a(); p.b(); p.c();


# In[ ]:

# Factory pattern is a creational pattern which uses factory methods to deal with the problem of creating objects without specifying 
# the exact class of object that will be created - Wikipedia

import random

def myfactory(objtype):
        if objtype == 1: return Burger()
        if objtype == 2: return Fries()
        print "Bad menu choice: "
        
class Menu(object):
    pass

class Burger(Menu):
    def listitem(self): print("Burger")

class Fries(Menu):
    def listitem(self): print("Fries")

print "Choose a menu item"
print "1: Burger, 2: Fries"

choice = int(raw_input('Enter your choice number :'))
        
f = myfactory(choice)
f.listitem()
print type(f)


# In[ ]:

# Factory pattern

import random

class Menu(object):
    @staticmethod
    def factory(objtype):
        if objtype == 1: return Burger()
        if objtype == 2: return Fries()
        print "Bad menu choice: "
    
class Burger(Menu):
    def listitem(self): print("Burger")

class Fries(Menu):
    def listitem(self): print("Fries")

print "Choose a menu item"
print "1: Burger, 2: Fries"

choice = int(raw_input('Enter your choice number :'))
        
f = Menu.factory(choice)
f.listitem()
#print type(f)


# In[ ]:

'''
Create an abstract base class called 'InterestCal'. Create a child class called 
'CICal'. The 'CICal' class will inherit the abstract base class. 
This child class will have three methods:
1) __init__ method, 
2) a method called compcal that computes the compound interest 
3) a method called compout that prints the compounded value.


Once all classes have been defined, the call to calculate and print the final 
value must follow the code below.

c = CICal(1000,5,6)
c.compcal()
print c.compout()

'''

