# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#int a = 5
#def hello(z):
print("Hello Lammers!!!")
#hello(z)

## Date: 26.04.2020 
## Contributor: Giorgi
### This code raises an error on first temp var... TypeError: unsupported operand type(s) for -: 'str' and 'int'
### Reason: 'input' function returns a String in Python3, 
### so we have to convert it to int if we are going to use returned value for math functions later
### int(some_string)
far = input("Enter farenheit ") 
print ("Entered data is " + far)
### in our case int(far)
tmp = (int(far)-32)/2 
tmp = float(tmp)

print (tmp)
## შენ რომელი ვერსია Python გაქვს, შეცდომას არ აგდებდა?