'''
    CIS 210, Winter 2016
    Project 4, Part 1
    Author: Jordan Mitchell Lewis
    Date: 2/1/2016
    This file contains code that takes alphabetic consonant/vowel pairs, and decodes them into an interger.
'''

def alphapinDecode(tone):
    '''
    (str) ---> int

    This function, alphapinDecode, is used to automate the process of converting an easy to remember string
    back into a password, pin number, or SSN. alphapinDecode will have one parameter, tone of type
    string, and will return pin (the original pin), in the form of an integer.

    Ex:
    >>>alphapinDecode('lohi')
    4327
    >>>alphapinDecode('dizo')
    1298
    >>>alphapinDecode('bomejusa')
    3463470
    >>>alphapinDecode('')
    Input 'tone' is not in the correct format
    '''
    pin = ''
    alphabet = 'abcdefghijklmnopqrstuvwyz'
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwyz'
    toneList = alphapinLister(tone)
    if alphaChecker(tone) == False: #Roadblock check to see if tone is inputted correctly
        print("Tone is not in the correct format. Tone must have consecutive consonant+vowel pairs, and must not contain spaces.") #Error message
        return None
    for i in toneList: #Loop to gather all of the integers
        firstDigit = consonants.find(i[0]) * 5
        secondDigit = vowels.find(i[1])
        digitPair = str(firstDigit+secondDigit)
        pin = pin + digitPair
    pin = int(pin) #Convert the string of numbers to an interger
    return pin

def alphapinLister(tone):
    '''
    (str) ---> list

    Takes the string entered by the user, tone, and segments it into
    two characters while turning it into a list, alphaList, which is returned.

    Ex:
    >>>alphapinLister('lohi')
    (lo, hi)
    >>>alphapinLister('bomejusa')
    (bo, me, ju, sa)
    '''
    alphaList = () #assign variable as an empty list
    while len(tone) > 0: 
        alphaList = alphaList + (tone[0:2],) #Add first 2 letters of tone to alphaList
        tone = tone[2:] #Reassign tone starting after the previous two letters
    return alphaList

def alphaChecker(tone):
    '''
    (str) ---> Boolean

    Checks the parameter (tone), a string, checks to make sure that it has
    no spaces, no numbers, no x, and that it is not an empty string, then returns
    either True or False.
    
    Ex:
    >>>alphaChecker('lohi')
    True
    >>>alphaChecker('lo hi')
    False
    >>>alphaChecker('lohi0')
    False
    >>>alphaChecker('ihol')
    False
    >>>alphaChecker('')
    False
    '''
    alphabet = 'abcdefghijklmnopqrstuvwyz'
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwyz'
    tone = str(tone)
    toneString = alphapinLister(tone)
    if tone == '': #Check to see that tone actually has characters in it
        return False
    for i in tone:
        if i not in alphabet: #check to see if all characters in ton are letters (except x)
            return False
    for i in toneString: #Check to see if all letters in tone are in the correct order
        if i[0] not in consonants: 
            return False
        if i[1] not in vowels:
            return False
    else: #If all conditions are met, return True
        return True
        
def alphapinDecode_stub(tone):
    '''
    (str) ---> int

    This function, alphapinDecode, is used to automate the process of converting an easy to remember string
    back into a password, pin number, or SSN. alphapinDecode will have one parameter, tone of type
    string, and will return pin (the original pin), in the form of an integer.

    Ex:
    >>>alphapinDecode('lohi')
    4327
    >>>alphapinDecode('dizo')
    1298
    >>>alphapinDecode('bomejusa')
    3463470
    >>>alphapinDecode('')
    Input 'tone' is not in the correct format
    '''
    pass
    return #int

def alphapinLister_stub(tone):
    '''
    (str) ---> list

    Takes the string entered by the user, tone, and segments it into
    two characters while turning it into a list, alphaList, which is returned.

    Ex:
    >>>alphapinLister('lohi')
    (lo, hi)
    >>>alphapinLister('bomejusa')
    (bo, me, ju, sa)
    '''
    pass
    return #list

def alphaChecker_stub(tone):
    '''
    (str) ---> Boolean

    Checks the parameter (tone), a string, checks to make sure that it has
    no spaces, no numbers, no x, and that it is not an empty string, then returns
    either True or False.
    
    Ex:
    >>>alphaChecker('lohi')
    True
    >>>alphaChecker('lo hi')
    False
    >>>alphaChecker('lohi0')
    False
    >>>alphaChecker('ihol')
    False
    >>>alphaChecker('')
    False
    '''
    pass
    return #Boolean
