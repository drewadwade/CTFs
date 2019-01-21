# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 09:41:51 2019

@author: AndrewW
"""

def single_XOR(a):

    start = a
    # Convert hex to byte array for a and b
    a = bytearray.fromhex(a).decode('latin-1')
    
    english = ["E","T","A","O","I","N","S","H","R","D","L","U"]
    phrase = []
    list = []
    highest = 0
    byte =[]
    i=0
    for i in range(128): 
        score = 0
        # Convert int i to hex
        i = hex(i)
        # Convert hex i without 0x to string and place in b
        b = str(i[2::])
        # If string b is only one digit, add a zero before
        if len(b)==1:
            b = "0" + b
        # Make b into a string of 34 of the same hex number 
        b = str(b * len(start))
        c = bytearray.fromhex(b).decode()
        
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
            elif letter == " ":
                score += 6                
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
            highest = score
            phrase = e
            byte= i

    scored_line = str("This: " + start + " XOR'd against: " + byte + " is: " + phrase + " at " + str(highest))


    return scored_line    
      
filepath = './4.txt'  
highest = 0
results=[]
final_result = ""
with open(filepath) as fp:  
    lines = [line.rstrip() for line in fp]

for line in lines:
    results += [single_XOR(line)]
  
for result in results:
    end = result[-4:]
    if not end.isdigit():
        end = end[-3:]        
        if not end.isdigit():
            end = end[-2:]
            if not end.isdigit():
                end = end[-1:]
    end = int(end)
    if end >= highest:
        highest = end
        final_result = result
    
    
print(final_result)

#   print(result)
