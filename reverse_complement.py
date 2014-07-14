#The complement of A is T, and the complement of C is G.
#!/usr/bin/python

rev = ''
fi = open('rosalind_revc.txt')
dna = fi.read()
comp = { 'A': 'T',
        'C': 'G',
        'T': 'A',
        'G': 'C'
        }

for base in dna:
    rev = rev + comp[base]

rev = rev[::-1]

print(rev)
