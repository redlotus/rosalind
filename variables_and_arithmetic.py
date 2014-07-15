#!/usr/bin/python

with open('rosalind_ini2.txt', mode = 'r', encoding = 'utf-8') as fi:
    numbers = fi.read()
    numbers = numbers.strip()
    a_list = numbers.split(' ')

with open('rosalind_ini2.out', mode = 'w', encoding = 'utf-8') as fo:
    fo.write('{}'.format(int(a_list[0])**2 + int(a_list[1])**2))

