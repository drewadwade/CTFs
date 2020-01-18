# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:57:55 2019

@author: AndrewW
"""

import base64
import binascii


def hamming(a,b):
    # Write a function to compute the edit distance/Hamming distance between two strings. 
    # The Hamming distance is just the number of differing bits. 
    # The distance between:
    #   this is a test
    #       and
    #   wokka wokka!!!
    # is 37. Make sure your code agrees before you proceed.

    import bitarray    

    # Hamming Tests
    # a = "this is a test".encode('utf-8')
    # b = "wokka wokka!!!".encode('utf-8')
    # distance should be 37 - PASSED
    # a = "A".encode('utf-8')
    # b = "A".encode('utf-8')
    #distance should be 0 - PASSED
    # a = "A".encode('utf-8')
    # b = "A".encode('utf-8')
    #distance should be 6 - PASSED
    
    # Convert text strings to binary bits
    abit = bitarray.bitarray()
    abit.frombytes(a)

    bbit = bitarray.bitarray()
    bbit.frombytes(b)
    
    # Compare each bit in the two strings and increment score by 1 for each difference 
    distance = 0
    position = 0
    
    while position < len(abit):
        if not abit[position] == bbit[position]:
            distance += 1
        position += 1
    return distance
    

def guesskeysize(encoded):
    
    from statistics import mean
    
    #Start a list to contain all of the keysize results
    results = []

    # Let keysize be the guessed length of the key; try values from 2 to (say) 40.
    # For each keysize, take the first keysize worth of bytes, 
    # and the second keysize worth of bytes, and repeat for all keysize blocks 
    # to find the edit distance between them and average the distances.
    for keysize in range(2,41):
    
        trial = 0
        distance = []
        while (2*keysize + trial) <= len(encoded):
            a = encoded[trial:(trial + keysize)]
            b = encoded[(trial + keysize):(trial + (2 * keysize))]
            if len(a) == keysize:
                distance += [hamming(a,b)]
            trial += 2*keysize
        average = mean(distance)

        # Normalize this result by dividing the average distance by the keysize.
        normalised = average/keysize
        # Round the resulting keysize and add it to the list of all possible keysizes
        results += [str(round(normalised,2))]

    # The keysize with the smallest normalized edit distance is probably the key,
    # but we'll take the best 5 just to be safe. 
    keysizes = []
    for likelies in range(5):
        keysize = results.index(min(results)) + 2
        keysizes += [keysize]
        del results[results.index(min(results))]
    return keysizes


def singlebyteXOR(a):

    # Convert hex string to byte array for the block to be examined
    a = bytearray.fromhex(a).decode()

    highest = 0
    byte =[]
    
    # Check each character in the ASCII range 0-120 as the single key XOR value 
    # for the block to be examined
    for i in range(121): 
        # Reset the XOR'd block's English score before trying a new key 
        score = 0
        # Convert int i to hex
        i = hex(i)
        # Convert hex i without 0x to string and place in b
        b = str(i[2::])
        # If string b is only one digit, add a zero before
        if len(b)==1:
            b = "0" + b
        # Make b into a string of the same repeated hex number to match the 
        # length of the block being examined
        b = str(b * len(a))
        # Convert the repeated key string to a byte array
        c = bytearray.fromhex(b).decode()

        # XOR the block byte array against the repeated key byte array
        d = [ chr(ord(x) ^ ord(y)) for (x,y) in zip(a, c) ]
        
        # Join the resulting XOR'd characters into a single list item
        e = ''.join(d)

        # Convert e from list to str
        e = str(e)
    
        # Count and score the English letters in relation to their frequency in 
        # words. This is how we measure which key has the "best histogram".           
        for letter in e:
            if letter == 'a' or letter == 'A':
                score += 0.08167
            elif letter == 'b' or letter == 'B':
                score += 0.01492
            elif letter == 'c' or letter == 'C':
                score += 0.02782
            elif letter == 'd' or letter == 'D':
                score += 0.04253
            elif letter == 'e' or letter == 'E':
                score += 0.12702
            elif letter == 'f' or letter == 'F':
                score += 0.02228
            elif letter == 'g' or letter == 'G':
                score += 0.02015
            elif letter == 'h' or letter == 'H':
                score += 0.06094
            elif letter == 'i' or letter == 'I':
                score += 0.06094
            elif letter == 'j' or letter == 'J':
                score += 0.00153
            elif letter == 'k' or letter == 'K':
                score += 0.00772
            elif letter == 'l' or letter == 'L':
                score += 0.04025
            elif letter == 'm' or letter == 'M':
                score += 0.02406
            elif letter == 'n' or letter == 'N':
                score += 0.06749
            elif letter == 'o' or letter == 'O':
                score += 0.07507
            elif letter == 'p' or letter == 'P':
                score += 0.01929
            elif letter == 'q' or letter == 'Q':
                score += 0.00095
            elif letter == 'r' or letter == 'R':
                score += 0.05987
            elif letter == 's' or letter == 'S':
                score += 0.06327
            elif letter == 't' or letter == 'T':
                score += 0.09056
            elif letter == 'u' or letter == 'U':
                score += 0.02758
            elif letter == 'v' or letter == 'V':
                score += 0.00978
            elif letter == 'w' or letter == 'W':
                score += 0.02360
            elif letter == 'x' or letter == 'X':
                score += 0.00150
            elif letter == 'y' or letter == 'Y':
                score += 0.01974
            elif letter == 'z' or letter == 'Z':
                score += 0.00074
            elif letter == ' ':
                score += 0.13000            
     
        # Find the highest scoring repeating key byte and format it as a hex string
        if score >= highest:
            highest = score
            if not len(i)%2 == 0:
                i = i[0:2] + "0" + i[2]
            byte = [i]

    return byte




### MAIN ###
# Here's a file. It's been base64'd after being encrypted with repeating-key XOR.
filepath = './6.txt'  
# Open the file and add each line (stripping the line end) to make one long Base64 string
with open(filepath) as fp:  
    lines = [line.rstrip() for line in fp]
encoded = ''.join(lines)

# Decode the base64 to hex bytes
encoded = binascii.hexlify(base64.b64decode(encoded))

# Clone the hex string bytes for later decoding
encodedbytes = encoded[:]

# Convert the hex bytes to a hex string
encoded = encoded.decode('utf-8')

# Guess the likely keysize of the encoded message
keysizes = guesskeysize(encodedbytes)

# Create lists for the possible key strings (possiblekeys) 
# and their matching hex strings
possiblekeys = []
possibleencoders = []

# Find the key for each of the top 5 keysizes 
for keysize in keysizes:
    # Now that you probably know the keysize 
    # break the ciphertext into blocks of keysize length.
    blocks = []
    blockencoded = encoded[:]
 
    while len(blockencoded) > keysize:
        blocks += [blockencoded[0:(2*keysize)]]
        blockencoded = blockencoded[(2*keysize)::]
    blocks += [blockencoded[0::]]

    # Now transpose the blocks: 
    # make a block that is the first byte of every block, 
    # and a block that is the second byte of every block, and so on.
    collector = []
    transposed = []
    count = 0
    while count < (2*keysize):
        for block in blocks:
            collector += [block[count:count+2]]
        count += 2
        collector = ''.join(collector)
        transposed += [collector]
        collector = []
 
    # Solve each block as if it was single-character XOR. For each block, the 
    # single-byte XOR key that produces the "best looking histogram" 
    # (see singlebyteXOR() function) is the repeating-key XOR key byte for that block.
    results = []
    hexresults = []
    possibleencoder = []
    
    for transblock in transposed:
        result = singlebyteXOR(transblock)
        result = result[-1::]
        result = ''.join(result)
        result = result.replace("0x", "")
        hexresult = result[:]
        hexresults += [hexresult]
        result = bytes.fromhex(result).decode("ascii")
        results += [result]

    # Put them together and you have the keys.        
    results = ''.join(results)
    hexresults = ''.join(hexresults)
    possiblekeys += [results]
    possibleencoders += [hexresults]

# Manually select the best English results for the key
# which you can use to decode the original message
for key in possiblekeys:
    print(str(possiblekeys.index(key)+1) + ") " + key) 
selection = input("Select the best key: ")
bestkey = str(possiblekeys[int(selection)-1])
encoder = str(possibleencoders[int(selection)-1])
print("The key is: " + bestkey)

# Make the selected bestkey into a repeating string of the same length as the 
# encoded message
encoder = encoder * ((len(encoded)//len(bestkey))+1)

# Convert hex to byte array for encoded mesage and encoder key
encoded = bytearray.fromhex(encoded).decode()
encoder = bytearray.fromhex(encoder).decode()

# XOR the encoder key against the encoded message to decode the message
aXOR = [ chr(ord(x) ^ ord(y)) for (x,y) in zip(encoder, encoded) ]

# Join the encoded hex bytes and convert them to a UTF-8 hex string 
aXOR = ''.join(aXOR)
aXOR = aXOR.encode('utf-8')

# Convert the decoded hex string to hex int
aXOR = aXOR.hex()

# Convert the decoded hex int to ASCII characters
aXOR = bytes.fromhex(aXOR).decode("ascii")
print("The decoded text is: " + str(aXOR) )