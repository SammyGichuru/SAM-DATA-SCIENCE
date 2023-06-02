# Python Functions
# a function is acollection/block of related code/asserrtions that  performs a specific task 
# e.g mathematical, analytical and evaluative
# two categories namely Built in and User defined functions
# why python funtion
# 1.prevent repeting code DRY(Don't Repeat yourself)
# 2.functions help divide large programs into smaller,unique and manageable divisions
# syntax def name():
def name():
    """this function prints the name of a person"""
    print('Maxwell')
#  call the function to display output
name()
#greet
def greet():
    '''function to print greetings'''
    print('Hello World')
greet()   
# built in functions
# Sqrt
num=64
from math import sqrt
square_root=sqrt(num)
print(square_root)

# sum
numbers=[20,50,50]
addition=sum(numbers)
print(addition)


def string():
    string='My favourite programming language'

    print(len(string))
string()