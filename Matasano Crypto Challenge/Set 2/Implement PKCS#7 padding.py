# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:14:40 2019

@author: AndrewW
"""

# A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of 
# plaintext into ciphertext. But we almost never want to transform a single 
# block; we encrypt irregularly-sized messages.

# One way we account for irregularly-sized messages is by padding, creating 
# a plaintext that is an even multiple of the blocksize. The most popular 
# padding scheme is called PKCS#7.

# So: pad any block to a specific block length, by appending the number of 
# bytes of padding to the end of the block. For instance,

# "YELLOW SUBMARINE"
# ... padded to 20 bytes would be:
# "YELLOW SUBMARINE\x04\x04\x04\x04"

irregular = "YELLOW SUBMARINE"

length = int(input("How long should the block be? "))

padding = length - len(irregular)

padding_hex = hex(padding)

padding_str = str(padding_hex)

if len(str(padding_hex))==3:
    padding_bin = "\\" + "x0" + padding_str[2::]    
else: 
    padding_bin = "\\" + "x" + padding_str[2::]

for j in range (0,int(padding)):
    irregular += str(padding_bin)

print(irregular)
print(len(irregular))