# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 17:37:45 2021

@author: User
"""

temp = float(input('Enter the celcius or fahrenheit in digits: '))
st = input("Enter either 'c' for celcius or 'f' for fahrenheits: ")

if st == 'c':
    fahrenheit = (temp * 1.8) + 32
    print(f'{temp} celsius is {fahrenheit} fahrenheit')
else:
    celcius =   (temp - 32) / 1.8 
    print(f'{temp} fahrenheit is {celcius} celcius')