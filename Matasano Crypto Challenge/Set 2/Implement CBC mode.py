# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:51:50 2019

@author: AndrewW
"""

# CBC mode is a block cipher mode that allows us to encrypt irregularly-
# sized messages, despite the fact that a block cipher natively only 
# transforms individual blocks.

# In CBC mode, each ciphertext block is added to the next plaintext block 
# before the next call to the cipher core.

# The first plaintext block, which has no associated previous ciphertext 
# block, is added to a "fake 0th ciphertext block" called the initialization 
# vector, or IV.

# Implement CBC mode by hand by taking the ECB function you wrote earlier, 
# making it encrypt instead of decrypt (verify this by decrypting whatever 
# you encrypt to test), and using your XOR function from the previous 
# exercise to combine them.

# The file here is intelligible (somewhat) when CBC decrypted against 
# "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c)

# Don't cheat.
# Do not use OpenSSL's CBC code to do CBC mode, even to verify your 
# results. What's the point of even doing this stuff if you aren't going 
# to learn from it?



from Crypto.Cipher import AES

''' Implement CBC mode by hand by taking the ECB function you wrote earlier, 
# making it encrypt instead of decrypt...

key = "YELLOW SUBMARINE"

filepath = './10Test.txt'  

# Open the file and read the text to the variable msg 
with open(filepath) as fp:  
    msg = fp.read()

# If the length of msg is not a multiple of 16, then pad msg with repeated 
# bytes of the remainder to make up the difference 
if len(msg)%16 != 0:
    msg = msg + (16 - len(msg)%16) * chr(16 - len(msg)%16)

# Setup encipher to use the UTF-8 key and encrypt in AES-ECB mode
encipher = AES.new(key.encode("utf-8"), AES.MODE_ECB)

# Use decipher to decrypt the message using the provided key & mode
msg_enc = encipher.encrypt(msg)

...(verify this by decrypting whatever you encrypt to test)...

# Setup decipher to use the UTF-8 key and decrypt in AES-ECB mode
decipher = AES.new(key.encode("utf-8"), AES.MODE_ECB)

# Use decipher to decrypt the message using the provided key & mode
msg_dec = decipher.decrypt(msg_enc)

# Convert the bytes message to hex string
msg_dec = msg_dec.hex()

# Convert the hex string results to ASCII plain text 
msg_dec = bytes.fromhex(msg_dec).decode("ascii")
print(msg_dec)
'''

# ...and using your XOR function from the previous exercise to combine them.
# The file here is intelligible (somewhat) when CBC decrypted against 
# "YELLOW SUBMARINE" with an IV of all ASCII 0 (\x00\x00\x00 &c)

key = "YELLOW SUBMARINE"
filepath = './10.txt'  
plaintext = ""
# Setup decipher to use the UTF-8 key and decrypt in AES-ECB mode
decipher = AES.new(key.encode("utf-8"), AES.MODE_ECB)

# XORvalue is initialised with the IV of all ASCII 0's 
XORvalue = 16 * chr(0)
XORvalue = bytes(XORvalue, 'UTF-8')

# Open the file and read the text to the variable msg 
with open(filepath) as fp:  
    msg = fp.read()

# If the length of msg is not a multiple of 16, then pad msg with repeated 
# bytes of the remainder to make up the difference 
if len(msg)%16 != 0:
    msg = msg + (16 - len(msg)%16) * chr(16 - len(msg)%16)

#Split msg into 16 byte blocks
cyphertext = []
for i in range(0, len(msg), 16):
    cyphertext += [msg[i:i+16]]

# For each block of 16 bytes:
for cypherblock in cyphertext:
       
    # 1) cypherblock gets decrypted to decryptedblock using the key
    # Use decipher to decrypt the message using the provided key
    decryptedblock = decipher.decrypt(cypherblock)

#    print(decryptedblock)
    
    # 2) decryptedblock gets XOR'd with XORvalue and added to plaintext
 
    # XOR the encoder key against the encoded message to decode the message
    aXOR = [ chr(x ^ y) for (x,y) in zip(decryptedblock, XORvalue) ]
    aXOR = ''.join(aXOR)

    plaintext += aXOR

    # 3) XORvalue is set to cypherblock
    XORvalue = cypherblock

print(plaintext)


