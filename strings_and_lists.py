#!usr/bin/python

""" the slice of particular string from indices """

count = 0
a_list = []

with open('rosalind_ini3.txt') as fi:
    for line in fi:
        if len(line) == 0:
            break
        a_list.append(line)

input_str = a_list[0]
indexs = a_list[1]
a_index = indexs.split(' ') # get index numbers
first_word = input_str[int(a_index[0]) : int(a_index[1]) + 1]
print(first_word, end = ' ')
second_word = input_str[int(a_index[2]) : int(a_index[3]) + 1]
print(second_word)

fi.close()

