#Encrypt it, under the key "ICE", using repeating-key XOR.

#In repeating-key XOR, you'll sequentially apply each byte of the key; 
#the first byte of plaintext will be XOR'd against I, the next C, the next E, 
#then I again for the 4th byte, and so on.

a = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal".encode('utf-8')
encoder = "ICE".encode('utf-8')

#Repeat encoder to length of a
encoder = encoder * ((len(a)//3)+1)
    
#Convert text strings to hex
a = a.hex()
encoder = encoder.hex()

# Convert hex to byte array for a and encoder
a = bytearray.fromhex(a).decode()
encoder = bytearray.fromhex(encoder).decode()

aXOR = [ chr(ord(x) ^ ord(y)) for (x,y) in zip(a, encoder) ]
aXOR = ''.join(aXOR)

aXOR = aXOR.encode('utf-8')

aXOR = aXOR.hex()

print(aXOR)

# Should be:
# 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
# a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f


