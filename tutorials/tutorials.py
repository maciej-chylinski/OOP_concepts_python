"""
some_string = "Manchester United"
lenght = len(some_string)
print(lenght)
"""

"""#operations on strings
number = 12345
int_to_str = str(number)
print(int_to_str[2])

print("albania".upper())
print("BELGIUM".lower())

name = input("Jak masz na imie?")
print("Your name is " + "%s" % (name))
"""

""" #if, elif,else
name= input("What's your name? ")
lenghth = len(name)

if lenghth < 4:
    print ("your name is less than 4 chars")
elif (lenghth >= 4 and lenghth <10):
    print ("your name is at least 4 chars and less than 10")
else:
    print ("Your name is very long")
"""

"""#functions 
def function1():
    print ("this is a function")
function1()


def multiply(a):
    return a * 2


def multiply2(a, b):
    return a * b


def multiply3(int1, int2, int3):
    print (multiply2(multiply(int1), int2) * int3)

multiply3(7,4,2)
"""

""" #importing modules
import random
from random import randint
from random import *

randomNum = randint(5,10)
print(randomNum)

from math import *
print(factorial(4))

print(random())"""

"""#build-in functions
print(type(1), type(2.45), type("aaa"), type(True), type([1,2,3]))
print(abs(-5), type(-8.3), max(1,9,2,3,20), min("bca", "cde"))
"""

"""#lists
#.append(element), .insert(index, element_value), .remove(element_value), pop(index) - removes item and assigns to a variable


list1 = [1,2,3,4,4,6]
print(list1)

list1[4] = 5
print(list1)

list1.append(7)
print(list1)


print(list1[:4])
print(list1[2:5])
print(list1[5:])

print(list1.index(7))

list1.insert(0,0)
print(list1)


#list1.append(3)
list1.remove(3)
print(list1)

var1 = list1.pop()
print(var1)

print(list1)
"""

"""For loop and tuples
#tuple - immutable list
tuple1 = (4,3,2,1)
print(tuple1[1])

print(tuple1[:2])
print(tuple1[1:3])
print(tuple1[2:])

for elements in tuple1:
    print(elements)
"""

"""#Dictionaries
#dictionary = {key: value, ....}
#add elem: Dict[key] = value
#del elem: del Dict[key]
Dict1 = {}
Dict1 = {0:"test1", 1:"test2", 2:"test3"}
Dict2 = {"test1":10, "test2":20, "test3":30}
print(len(Dict1))

print(Dict1)
print("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
print(Dict2)
for key in Dict2:
    print(Dict2[key])

for key in Dict1:
    print(Dict1[key])


print(Dict1[0], Dict1[1], Dict1[2])

Dict1[0] = 3
print(Dict1[0])

Dict1[1] = 4
print(Dict1[1])

Dict1[2] = 5
print (Dict1[2])

print("$$$$$$$$$$$$$$$$$$$$$$")
del Dict1[2]
for key in Dict1:
    print(Dict1[key])

print(Dict2)
print(Dict1)
"""

"""#using functions with lists
exList = [9,0,2,1,0]
def list_modifier(li):
    return li[2]/0.5
print(list_modifier(exList))

def list_passer(li):
    return li
print (list_passer(exList))

list1 = ["one", "two", "three"]
def list_manip(li):
    print(li[1])
    li[2] += "frog"
    print(li[2])
    li.remove(li[0])
    print(li)
    return li

list_manip(list1)
"""

"""
#range
#range(8) -> stop, range(1,4) ->(start, stop), range(start,stop,step)
#lists created with usage of range are immutable - the same as tuples / append and pop does not work on it - ale w 3.5 dziąła na pewno

list1 = [2,3,4,5]

def print_list(li):
    for el in li:
        print(el)


first = range(3)
second = range(2,5)
third = range(2,13,5)


def fun4(li1, li2,li3):
    emptyList = []
    for elems in range(0, len(li1)):
        emptyList.insert(elems, li1[elems] + li2[elems] + li3[elems])
        #emptyList.append(li1[elems] + li2[elems] + li3[elems])
    return(emptyList)


list_of_lists = [[1,2],[0,1],[3,4]]
def fun5(li):
    for els in li:
        for vals in els:
            print (vals)
fun5(list_of_lists)

print ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
print_list(list1)
print(fun4(first, second, third))
"""

"""#loops
from random import randint

counter = 5
while counter < 10:
    print(counter)
    if counter == 7:
        print("counter == 7")
        break
    #if (counter < 10 and counter != 7) :
    counter = randint(5,10)
else:
    print("Counter equal 10")



#Ważne
#iterowanie po wartościach tablicy : for char in tab:
#iterowanie po indexach tablicy: for char in range(len(tab))


#wypisywanie ciągu znaków w jednej linii
ex_str = "example"
for char in ex_str:
    print(char, end="")



#dictionaries are not ordered - wypisywanie elementów jest losowo
#zip() - do iterowania i porównywania elementów listy - może przyjmować wiele list na wejście, ale listy muszą mieć tyle samo elementów

str_var = "value"
int_var = [1,2,3,4,5]
dict_val = {"a": 1, "b": 5, "c": 18}

for index in range(0,len(str_var)):
    print(str_var[index])

for val in int_var:
    print(val, end="")

print("\n")

for key in dict_val:
    print(dict_val[key])

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
int_var2 = [6,7,8,9,5]

def compare_lists(li1, li2):
    for num1, num2 in zip(li1, li2):
        if num1 > num2:
            print(num1)
        elif num2 > num1:
            print(num2)
        else:
            print(100)
compare_lists(int_var, int_var2)


for el in int_var:
    print(el, end="")
else:
    print(100)

"""

"""#List comprehensions"""
"""
#example = [item for item in range(1,10,2)]
ex1 = [num1 for num1 in range(1,10,2)]
ex2 = [num2 for num2 in range(3,8)]
ex3 = [num3 for num3 in range(1,10) if num3 % 2 != 0]
ex4 = [num4 for num4 in range(1,10) if num4 > 2 and num4 < 8]
print(ex4)
"""

"""#list slicing with Stride 
exList = [1,2,3,4,5]
ommited = exList[1::2]
print(ommited)

#reversing list
exList2 = [6,7,8,9, 10]
reversed = exList[::-1]

list_stride = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list_stride2 = list_stride[1:19:2]
print(list_stride2)
print(list_stride[0:20:5])
print(list_stride[11:0:-3])
print(list_stride[::-1])
"""

"""#Try and except statemants"""
from random import randint


def compare_values():
    val2 = randint(0, 5)
    print(str(val2) + "\n")
    val1 = input("podaj liczbe: ")

    try:
        val1 = int(val1)
        val2 = int(val2)

        if val1 > val2:
            print(val1)
        elif val2 > val1:
            print(val2)
        else:
            print("so równe")
    except:
        print("nie moge skonwertować")


compare_values()

