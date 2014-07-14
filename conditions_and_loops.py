#!/usr/bin/python

""" Sum of odd numbers in specific range """

odd_sum = 0

fi =  open('rosalind_ini4.txt')
data = fi.read()
numbers = data.split(' ')

for number in range(int(numbers[0]), int(numbers[1])):
    if (number % 2) == 1:
        odd_sum += number

print(odd_sum)

