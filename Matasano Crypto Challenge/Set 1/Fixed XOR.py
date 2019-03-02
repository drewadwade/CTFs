from itertools import cycle

# Here is the source hex to be XOR'd
a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'

print (a + "\n        XOR'd against \n" + b)

# Convert hex to byte array for a and b
a = bytearray.fromhex(a).decode()
b = bytearray.fromhex(b).decode()

# XOR a against b
c = [ chr(ord(x) ^ ord(y)) for (x,y) in zip(a, b) ]

# Join the array of XOR output
d = ''.join(c)
print ("Produces: " + d)

