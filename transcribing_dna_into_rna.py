#!/usr/bin/python

dna = ''

with open('rosalind_rna.txt', mode = 'r', encoding = 'utf-8') as fi:
    dna = fi.read() # get dna string
    dna = dna.strip()
    rna = dna.replace('T', 'U') # just replace T by U
with open('rosalind_rna.out', mode = 'w', encoding = 'utf-8') as fo:
    fo.write(rna)
