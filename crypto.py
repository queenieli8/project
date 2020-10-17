# crypto.py
# --------------
# COMP1405A - Fall2020

## Student: Queenie Li
## ID: 101185786


def encrypt(m, shift, alph):
    result = ""
    x = 0
    y = 0
    while x < len(m):
        for y in range(0,len(alph)):
            if m[x] == alph[y]:
                if (y + shift) > len(alph) - 1: 
                    result = result + alph[j + shift - len(alph)]
                    break
                else:
                    result = result + alph[j + shift]    
                    break  
            y = y + 1
        x = x + 1     
    print(result)


def passwordIsValid(passwd):
    #length > 5
    if len(passwd) < 5:
        return False
    #2 digits
    numbers = '0123456789'
    for i in range(len(passwd)):
        if passwd[i] in numbers:
            break
        elif i == len(passwd) - 1:
            return False
    #special char
    sChar = '!@#$%^_'       
    for i in range(len(passwd)):
        if passwd[i] in sChar:
            break
        elif i == len(passwd) - 1:
            return False
    #upper and lower
    if passwd.isupper() == passwd:
        return False    
    if passwd.islower() == passwd:
        return False   
    #start
    alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if passwd[0] !='_':
        if passwd[0] not in alph:
            return False
    return True
