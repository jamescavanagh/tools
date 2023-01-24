#!/usr/bin/env python
# coding: utf-8

"""
A script to increase my focus, by creating dificult to rememeber
Four digit passwords for my iphone's screen time

This is to limit the use of social media, streaming services, ect.
to certain times of the day
"""

import numpy as np 


numbers = np.array([1,2,3,4,5,6,7,8,9,0])


from sys import exit

def create_passcode():

    isFirstDigit = True
    passcode = ''

    for i in range(4):

        if isFirstDigit == True:
            passcode = passcode + str(int(np.random.choice(numbers)))
            isFirstDigit == False
            continue
        else:
            preceedingDigit  = passcode[-1:]
        
        # In order to generate a password that is 
        # Difficult to memorize 
        # This code selects non-adjacent digits on a number pad

        if preceedingDigit == 0:
            splice = [1,2,3,4,5,6]
        elif preceedingDigit == 4:
            #Right column
            splice = [3,6,9,0]
        elif preceedingDigit == 5:
            # Numbers on diagonals
            splice = [0,1,3,7,9]
        elif preceedingDigit == 6:
            # Numers on right column
            splice = [1,4,7,0]
        
        elif 1 <= preceedingDigit < 4:
            splice = [7,8,9,0]
        elif 7 < preceedingDigit <= 9:
            splice = [1,2,3]

        nextDigitInPassword  = np.random.choice(splice)
        
        passcode += str(NextDigitInPassword)
    
    return passcode


def check_for_repeating_numbers(passcode):
    
    
    ''' Checks if the password  contains any duplicates numbers
    This is because having the same number repeted makes it more 
    simple to remember after entering it a few times

    '''
    listOfElems = [char for char in passcode]

    # Comparing the elements of the list
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

def check_for_year(passcode):
    #Prevents me from associating the password
    # With a historical event

    if int(passcode) < 2100:
        return True
    else:
        return False

## Begin Script #############################

hasRepeating = True
resemblesYear = True

while (hasRepeating == True) or  (resemblesYear == True):
    passcode = create_passcode()
    
    hasRepeating = check_for_repeating_numbers(passcode)
    resemblesYear = check_for_year(passcode)


f = open("screentimePass.txt", "w")
f.write(passcode)
f.close()

print(passcode)
    
exit()

