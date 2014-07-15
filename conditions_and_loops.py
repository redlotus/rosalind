#!/usr/bin/python

""" Sum of odd numbers in specific range """

odd_sum = 0

fi =  open('rosalind_ini4.txt', mode = 'r', encoding = 'utf-8')
data = fi.read()
data = data.strip() # remove all unecessary whitespace
numbers = data.split(' ')

for number in range(int(numbers[0]), int(numbers[1])):
    if (number % 2) == 1: # check whether odd number or not
        odd_sum += number

with open('rosalind_ini4.out', mode = 'w', encoding = 'utf-8') as fo:
    fo.write('{}'.format(odd_sum))

