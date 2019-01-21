import codecs

# Here is the hex to be converted
a = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

print ("From here: " + a)

b = bytearray.fromhex(a).decode()

print ("Which is: " + b)

# Decodes the variable a as hex, encodes it as base64 in variable c
c = codecs.encode(codecs.decode(a, 'hex'), 'base64').decode()

print ("To there: " + c) 

