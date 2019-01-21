# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:57:55 2019

@author: AndrewW
"""
import base64
import binascii

# Here's a file. It's been base64'd after being encrypted with repeating-key XOR.
filepath = './6.txt'  
with open(filepath) as fp:  
    lines = [line.rstrip() for line in fp]
encoded = ''.join(lines)

# Decode the base64 to hex
encoded = binascii.hexlify(base64.b64decode(encoded))

# Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

# Write a function to compute the edit distance/Hamming distance between two strings. 
# The Hamming distance is just the number of differing bits. 
# The distance between:
#   this is a test
#       and
#   wokka wokka!!!
# is 37. Make sure your code agrees before you proceed.


# For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, 
# and find the edit distance between them. 

# Normalize this result by dividing by KEYSIZE.

# The KEYSIZE with the smallest normalized edit distance is probably the key. 
# You could proceed perhaps with the smallest 2-3 KEYSIZE values. 
# Or take 4 KEYSIZE blocks instead of 2 and average the distances.

# Now that you probably know the KEYSIZE: 
# break the ciphertext into blocks of KEYSIZE length.

# Now transpose the blocks: 
# make a block that is the first byte of every block, 
# and a block that is the second byte of every block, and so on.

# Solve each block as if it was single-character XOR. You already have code to do this.

# For each block, the single-byte XOR key that produces the best looking histogram 
# is the repeating-key XOR key byte for that block. 

# Put them together and you have the key.