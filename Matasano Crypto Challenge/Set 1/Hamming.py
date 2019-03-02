# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:16:53 2019

@author: AndrewW
"""

    # Write a function to compute the edit distance/Hamming distance between two strings. 
    # The Hamming distance is just the number of differing bits. 
    # The distance between:
    #   this is a test
    #       and
    #   wokka wokka!!!
    # is 37. Make sure your code agrees before you proceed.

import bitarray

a = "this is a test"
b = "wokka wokka!!!"

# Convert text strings to binary bits
abit = bitarray.bitarray()
abit.frombytes(a.encode('utf-8'))

bbit = bitarray.bitarray()
bbit.frombytes(b.encode('utf-8'))


# Compare each bit in the two strings and increment score by 1 for each difference 
distance = 0
position = 0

while position < len(abit):
    if not abit[position] == bbit[position]:
        distance += 1
    position += 1

print (distance)