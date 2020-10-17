# crypto.py
# --------------
# COMP1405A - Fall2020

## Student: Queenie Li
## ID: 101185786


def encrypt(message, shift, alphabet):
    result = ""
    for x in range(0,len(message)):
        for y in range(0,len(alphabet)):
            if message[x] == alphabet[y]:
                shift_position = y + shift
                if (shift_position) > len(alphabet) - 1: 
                    result = result + alphabet[shift_position - len(alphabet)]
                    break
                else:
                    result = result + alphabet[shift_position]    
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
    special_characters = '!@#$%^_'       
    for i in range(len(passwd)):
        if passwd[i] in special_characters:
            break
        elif i == len(passwd) - 1:
            return False
    
    #upper and lower
    upper_lower_found = False
    for i in range(len(passwd)):
        if passwd[i].isupper() == True:
            for h in range(len(passwd)):
                if passwd[h].islower() == True:
                    upper_lower_found = True

    if upper_lower_found == False:
        return False  

    #start
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if passwd[0] !='_':
        if passwd[0] not in alphabet:
            return False
    return True
