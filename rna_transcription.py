#!/usr/bin/python


fi = open('rosalind_rna.txt')
dna = fi.readline()
rna = dna.replace('T', 'U')

print(rna)
