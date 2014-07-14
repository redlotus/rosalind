#!/usr/bin/python

def count_character(dna, base):
    print(dna.count(base), end=' ')

try:
    fi = open('rosalind_dna.txt')
except IOError:
    print('File not found')

dna = fi.read()
bases = ('A', 'C', 'G', 'T')

for base in bases:
    count_character(dna, base)

fi.close()

