'''
    Project 3, Part 2
    Author: Jordan Mitchell Lewis
    Date: 01/26/2016
    Credits: Bradley N. Miller and David L. Ranum for starter code
    This file contains a function that turns a number (i.e a password, pin number, SSN),
    into an easier to remember string of consonants and vowels.
'''

def alphapinEncode(pin):
    '''
    (int) ---> str

    This function, alphapinEncode, is used to automate the process of converting a password, pin number, or SSN
    to and easy to remember string consisting of consonants+vowel pairs. alphapinEncode will have one parameter,
    pin, of type integer, and will return alphaPin (the encoded pin), in the form of a string. 

    Ex:
    >>>alphapinEncode(4327)
    'lohi'

    >>>alphapinEncode(1298)
    'dizo'

    >>>alphapinEncode(3463470)
    'bomejusa'
    
    '''
    alphaPin = ''
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwyz"
    while pin > 0:
        lastDigits = pin % 100 #Seperate last two digits
        alphaPin = vowels[(lastDigits % 5)] + alphaPin #get the 1st digit and convert
        alphaPin = consonants[(lastDigits // 5)] + alphaPin #get the 2nd digit and convert
        pin = pin // 100 #divide the number to get new digits
    return alphaPin

def alphapinEncode_stub(pin):
    '''
    (int) ---> str

    This function, alphapinEncode, is used to automate the process of converting a password, pin number, or SSN
    to and easy to remember string consisting of consonants+vowel pairs. alphapinEncode will have one parameter,
    pin, of type integer, and will return alphaPin (the encoded pin), in the form of a string. 

    Ex:
    >>>alphapinEncode(4327)
    'lohi'
    
    >>>alphapinEncode(1298)
    'dizo'

    >>>alphapinEncode(3463470)
    'bomejusa'
    '''
    pass
    return #string
