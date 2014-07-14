#!/usr/bin/python

fi = open('rosalind_ini2.txt')
numbers = fi.read()
a_list = numbers.split(' ')

print(int(a_list[0])**2 + int(a_list[1])**2)

