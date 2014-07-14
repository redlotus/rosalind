#!/usr/bin/python

from collections import OrderedDict

data = ''
word_list = []
word_dist = OrderedDict()
# read input data from text file
with open('rosalind_ini6.txt', mode = 'r', encoding = 'utf-8') as fi:
    data = fi.read()

data = data.strip()
word_list = data.split(' ')

for word in word_list:
    if word not in word_dist:
       word_dist[word] = data.count(word, 0, len(data))
with open('rosalind_ini6.out', mode = 'w', encoding = 'utf-8') as fo:
    for key, value in word_dist.items():
        fo.write("%s %d\n" % (key, value))

