
# coding: utf-8

# In[ ]:

'''
Functions
1. Arguments and outputs
2. default argument
3. keyword based arguments

Syntax for function
def name_of_the_function(list of arguments):
    statements that need to be executed
    return value
'''


# In[ ]:

def increment(a):
    b = a+1
    return b

increment(20)
# we are calling the function and passing a value to it


# In[ ]:

def increment(a,incr):
    c = a+incr
    return c

increment(10,3)
# we are calling the function and passing two values to it


# In[ ]:

def increment(a,incr):
    c = a+incr
    return (c,a,incr)

increment(10,3)


# In[ ]:

def increment(a,incr=1):
    a = a+incr
    return a

print increment(3) # for this the incr will default to 1
print increment(3,4) 
# here the incr is assigned a value of 4 which overrides the value


# In[ ]:

def increment(a=4,incr1=1):
    a = a+incr1
    return a

print increment(a=3,incr1=2) # another way of passing values to arguments


# In[ ]:

print increment(incr1=2,a=3) # another way of passing values to arguments


# In[ ]:

print increment(incr1=5,a=2) #if you assign a value for a keyword argument 
# then other keyword arguments to its right should also be assigned values. 


# In[ ]:

increment


# In[ ]:

'''
In-class activity:
Create a function called squared which takes a list called mylist and returns 
another list where the elements are square of mylist. Also write another 
function that takes mylist and returns a dictionary where the key is the input 
and the value is the square of the input. 
'''


# In[ ]:



