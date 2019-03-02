# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 12:35:56 2019

@author: AndrewW
"""

# The Base64-encoded content in this file has been encrypted via AES-128 in ECB 
# mode under the key "YELLOW SUBMARINE" (case-sensitive, without the quotes; 
# exactly 16 characters; I like "YELLOW SUBMARINE" because it's exactly 16 bytes 
# long, and now you do too).
# Decrypt it. You know the key, after all.

# Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.
# Do this with code.

# You can obviously decrypt this using the OpenSSL command-line tool
# i.e.,   openssl enc -aes-128-ecb -d -in 7.txt -out file.txt
# but we're having you get ECB working in code for a reason. You'll need it a 
# lot later on, and not just for attacking ECB.

from Crypto.Cipher import AES
import base64

key = "YELLOW SUBMARINE"

# This key is exactly 16 characters long (128-bit), so it does not need padding, 
# but here is the code for adding or reducing padding when needed
#BS = 16
#pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
#unpad = lambda s: s[0:-ord(s[-1])]

filepath = './7.txt'  
# Open the file and decode the Base64 text 
with open(filepath) as fp:  
    msg = base64.b64decode(fp.read())

# Setup decipher to use the UTF-8 key and decrypt in AES-ECB mode
decipher = AES.new(key.encode("utf-8"), AES.MODE_ECB)

# Use decipher to decrypt the message using the provided key & mode
msg_dec = decipher.decrypt(msg)

# Convert the bytes message to hex string
msg_dec = msg_dec.hex()

# Convert the hex string results to ASCII plain text 
msg_dec = bytes.fromhex(msg_dec).decode("ascii")
print(msg_dec)


