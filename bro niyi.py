# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 07:26:08 2020

@author: pc
"""

def add (x, y):
    return x+y
def substract (x, y):
    return x-y
def multiply (x, y):
    return x*y
def divide (x, y):
    return x/y

print("the select operation.")
print("add")
print("substract")
print("multiply")
print("divide")

select = input("enter operator")
w = int(input("enter number1"))
q = int(input("enter number2"))
if select == "+":
    print(w, "+", q, "=" , add(w,q))
elif select == "-":
    print(w, "-", q, "=" , substract(w,q))
elif select == "*":
    print(w, "*", q, "=" , multiply(w,q))
elif select == "/":
    print(w, "/", q, "=" , divide(w,q))
else:
    print("invalid input")
