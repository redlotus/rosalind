# The complement of A is T, and the complement of C is G.
#!/usr/bin/python

rev = ''
with open('rosalind_revc.txt', mode = 'r', encoding = 'utf-8') as fi:
    with open('rosalind_revc.out', mode = 'w', encoding = 'utf-8') as fo:
        dna = fi.read() # get dna string
        dna = dna.strip() # remove trailing spaces
        # define complement pair
        comp = { 'A': 'T',
                'C': 'G',
                'T': 'A',
                'G': 'C'
                }

        for base in dna:
            rev = rev + comp[base]
        rev = rev[::-1]
        fo.write(rev)
