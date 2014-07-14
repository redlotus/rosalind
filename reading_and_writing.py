#!/usr/bin/python

even_line = True

with open('rosalind_ini5.txt', mode = 'r', encoding = 'utf-8') as fi:
    with open('rosalind_ini5.out', mode = 'w', encoding = 'utf-8') as fo:
        for line in fi:
            even_line = not even_line
            if even_line:
                fo.write(line)

