
# In this file are a bunch of hex-encoded ciphertexts.

# One of them has been encrypted with ECB.

# Detect it.

# Remember that the problem with ECB is that it is stateless and deterministic; 
# the same 16 byte plaintext block will always produce the same 16 byte ciphertext.

# a solution can be found by: 
# 1) reading/decoding the data from the file; 
# 2) Group the data into 16 byte chunks and count any repeating chunks; 
# 3) Select the ciphertext with the most repetitions.

import numpy
import collections

# 1) reading/decoding the data from the file; 

filepath = './8.txt'  
# Open the file  
with open(filepath) as fp:  
    lines = [line.rstrip() for line in fp]

# 2) Group the data into 16 byte chunks and count any repeating chunks; 
for line in lines:

    broken = [line[i:i+32] for i in range(0,len(line), 32)]
    counter=collections.Counter(broken)
    count_list = list(counter.values())
# 3) Select the ciphertext with the most repetitions.
    for j in count_list:
        if j > 1:
            print("This is the cyphertext encoded in AES in ECB: ")
            print(line)
    
