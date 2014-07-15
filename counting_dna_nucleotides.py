#!/usr/bin/python

dna = '' # use to store dna string
with open('rosalind_dna.txt', mode = 'r', encoding = 'utf-8') as fi:
    with open('rosalind_dna.out', mode = 'w', encoding = 'utf-8') as fo:
        dna = fi.read() # get dna string
        dna = dna.strip() # remove all unecessary whitespace
        bases = ('A', 'C', 'G', 'T') # define bases

        # count number of times each symbol occur in dna string
        for base in bases:
            fo.write('{:d} '.format(dna.count(base, 0, len(dna))))
