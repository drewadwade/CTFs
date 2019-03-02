# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 09:41:51 2019

@author: AndrewW
"""



# Here is the source hex to be XOR'd
a = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# Convert hex to byte array for a
a = bytearray.fromhex(a).decode('latin')

print(a)
print(type(a))

start = a[:]
phrase = []
highest = 0
byte =[]

for i in range(120,121): 
    score = 0
    # Convert int i to hex
    i = hex(i)
    # Convert hex i without 0x to string and place in b
    b = str(i[2::])
    # If string b is only one digit, add a zero before
    if len(b)==1:
        b = "0" + b
    # Make b into a string of 34 of the same hex number 
    b = str(b * len(a))
    c = bytearray.fromhex(b).decode()
    
  #  print(a)
 #   print("hello")
#    print(c)

    d = [ chr(ord(x) ^ ord(y)) for (x,y) in zip(a, c) ]
    
    e = ''.join(d)
  
    e = e.upper()
    
    for letter in e:
        if letter == "E":
            score += 13
        elif letter == "T":
            score += 9
        elif letter == "A":
            score += 8
        elif letter == "O":
            score += 8
        elif letter == "I":
            score += 7
        elif letter == "N":
            score += 7
        elif letter == "S":
            score += 6
        elif letter == "H":
            score += 6
        elif letter == "R":
            score += 6
        elif letter == "D":
            score += 4
        elif letter == "L":
            score += 4
        elif letter == "U":
            score += 3
        
        
    if score >= highest:
        phrase = e
        byte= i

print ("This: " + start + " XOR'd against: " + byte + " is: " + phrase + " at " + str(score))
  
