import random
from sys import exit


def choose_first_digit():
    # no 1 or 2 because I assosiate them with years so they're easy to remember
    return str(random.choice([0,3,4,5,6,7,8,9]))

def zero():
    return [1,2,3,4,5,6]
def one_three():
    return [7,8,9,0]
def four():
    return [3,6,9,0]
def five():
    return [0,1,3,7,9]
def six():
    return [1,4,7,0]
def seven_nine():
    return [1,2,3]
    
switcher = {
    '0':zero(),
    '1':one_three(),
    '2':one_three(),
    '3':one_three(),
    '4':four(),
    '5':five(),
    '6':six(),
    '7':seven_nine(),
    '8':seven_nine(),
    '9':seven_nine()
}

def choose_next(digit,pw):
    pw = [int(d) for d in list(pw)]
    choices = switcher[digit]
    #remove repeating
    choices = [d for d in choices if d not in pw]
    

    return str(random.choice(choices))
def main():
    passcode = choose_first_digit()
    for i in range(3):
        passcode += choose_next(passcode[-1],passcode)
    print(passcode)
    f = open("screentimePass.txt","w")
    f.write(passcode)
    f.close()

while True:
    main()
    exit()
