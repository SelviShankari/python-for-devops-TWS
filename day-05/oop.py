# What is Object Oriented Programming ?
# Object Oriented Programming is a way of writing programs by thiinking in terms of real-world objects instead of just functions and logic.
# OOPS consists of classes and objects.


#  What is a class ?
# Class is a blueprint for creating objects. Blueprint means it stores informmation about what all things to have inside the class.

# What is a object ?
# Object is the real instance created from the class.

# Example 1 for classes and objects 

class Student:  #This is how we create a class
    name ="karan"   #this is the blueprint that we talk about
s1=Student()   # this is how we create a new object. this is also called as instance
# print(s1)
# print(s1.name)

s2=Student()
# print(s2.name)

# Example 2 for classes and objects

# class Dress:
    # color="antiquewhite"
    # pattern="co-ord set"
    # def __init__(self): #default functions that get runs automatically if not created manually. And 
        # print("Function got initialized....")
# customer_1=Dress() #The paranthesis over here is for calling the constructor
# print(customer_1.color)
# print(customer_1.pattern)

# Understanding __init__ function or Constructor

# All classes have a function called __init__() which is always executed when the object is being initiated.

# example 1 for constructor 
# class Dress:
#     color="antiquewhite"
#     pattern="co-ord set"
#     def __init__(self,Size): # default functions that get runs automatically if not created manually. And if we add any extra parameters we call it as parameterized constructor.
#         self.size=Size
#         print("Function got initialized....")
# customer_1=Dress("S")  #The paranthesis over here is for calling the constructor
# print(customer_1.size)

# Understanding Attributes (class attribute and object attribute)


class School:
    school_name="Adarsha Vidyalaya"  # In this example school_name is called as class attributes
    def __init__(self,name,standard,age):
        self.name=name #And the following three of them are called as is=nstance attributes.
        self.standard=standard
        self.age=age
Student=School("Selvi",4,21)
print("The name of the student is:",Student.name)
print("The standrd in which the student is studying is: ",Student.standard)
print("The age of the student is: ",Student.age)

# Methods are functions that belong to objects. In the above example def __init__ is a method














