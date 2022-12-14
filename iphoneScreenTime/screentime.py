#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 


numbers = np.array([1,2,3,4,5,6,7,8,9,0])


from sys import exit

def create_passcode():

    firstDigit = True
    passcode = ''
    for i in range(4):

        if firstDigit == True:
            nextDigit = int(np.random.choice(numbers))
            firstDigit == False
            
        if nextDigit == 0:
            splice = numbers[0:7]
        elif nextDigit == 4:
            splice = [3,6,9,0]
        elif nextDigit == 5:
            splice = [0,1,2,3,4,6,7,8,9]
        elif nextDigit == 6:
            splice = [1,4,7,0]
        
        elif 1 <= nextDigit < 4:
            splice = numbers[6:]
        elif 6 < nextDigit <= 9:
            splice = numbers[0:3]

        nextDigit = np.random.choice(splice)
        
        passcode += str(nextDigit)
    return passcode

def checkIfDuplicates(passcode):
    
    
    ''' Check if given list contains any duplicates '''
    listOfElems = [char for char in passcode]

    
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

hasDuplicates = True

while hasDuplicates == True:
    passcode = create_passcode()
    
    hasDuplicates = checkIfDuplicates(passcode)

f = open("screentimePass.txt", "w")
f.write(passcode)
f.close()

print(passcode)
    


exit()

