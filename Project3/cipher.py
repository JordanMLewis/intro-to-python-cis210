'''
    Project 3, Part 1
    Author: Jordan Lewis
    Class: CIS 210, Winter 2016
    Date: 01/26/2016
    Credits: Bradley N. Miller and David L. Ranum for starter code
    This file contains functions that, when given a string and a password, generate a key that creates
    a specific substitution cipher key and encrypts the user's message while removing duplicates and spaces. 
'''

from random import *

def substitutionEncrypt(plainText, password):
    '''
    (str, str) ---> str

    This function takes an input from the user, plainText, and uses a cipher, password, to encrypt a message.
    The password is created by the genKey function.

    Ex:
    >>>substitutionEncrypt('the quick brown fox', 'ajax')
    'qdznrexgjoltkblu'

    >>>substitutionEncrypt('thequickbrownfox', 'ajax')
    'qdznrexgjoltkblu'

    >>>substitutionEncrypt('the quick brown fox', 'kalypso')
    'fqpcgrluadzixszj'
    '''
    plainText = plainText.lower()
    plainText = removeSpaces(plainText)
    key = genKey(password)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText

def substitutionDecrypt(plainText, password):
    '''
    (str, str) ---> str

    This function takes an input from the user, plainText, in the form of an encrypted message,
    and uses the same password, password, specified in the function substitutionEncrypt to decrypt
    the message. The function returns the decrypted message without spaces.

    >>>substitutionDecrypt('qdznrexgjoltkblu', 'ajax')
    'thequickbrownfox'

    >>>substitutionDecrypt('frwpikrfeszdxzwkx', 'kalypso')
    'timewaitsfornoman'
    '''
    key = genKey(password)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        idx = key.find(ch)
        cipherText = cipherText + alphabet[idx]
    return cipherText

def genKey(password):
    '''
    (str) ---> str

    This function creates a cipher key, key, using a specified user input in the form of a password, password.
    This function is called by substitutionEncrypt to create a specially organized alphabet or "key" that will
    be used to encrypt the user's message.

    Ex:
    >>>genKey('ajax')
    'ajxyzbcdefghiklmnopqrstuvw'

    >>>genKey('kalypso')
    'kalypsoqrtuvwxzbcdefghijmn'
    '''
    key = "abcdefghijklmnopqrstuvwxyz"
    password = removeDupes(password)
    lastChar = password[-1]
    lastIdx = key.find(lastChar)
    afterString = removeMatches(key[lastIdx+1:], password)
    beforeString = removeMatches(key[:lastIdx], password)
    key = password + afterString + beforeString
    return key

def removeDupes(myString):
    '''
    (str) ---> str

    This function removes any duplicate letters in a string parameter, myString.
    removeDupes is utilized by genKey to create an accurate key that uses each letter
    in the English alphabet only once. removeDupes will be used in substitutionEncrypt to
    make the user's message much more difficult to decrypt by third parties.
    
    Ex:
    >>>removeDupes('loot')
    'lot'

    >>>removeDupes('boooo!')
    'bo!'
    '''
    newStr = ""
    for ch in myString:
        if ch not in newStr:
            newStr = newStr + ch
    return newStr

def removeMatches(myString, removeString):
    '''
    (str, str) ---> str

    This function takes two parameters, myString and removeString,
    and compares the two for any matching characters. Should there be
    any matching characters, the function removes them and returns a new
    string with any letters that myString does NOT have in common with
    removeString.  
    
    Ex:
    >>>removeMatches('kalypso', 'gasldknha')
    'ypo'

    >>>removeMatches('abcdefg', 'abcdef')
    'g'
    '''
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr = newStr + ch
    return newStr

def removeSpaces(plainText):
    '''
    (str) ---> str

    This function takes a user inputted string as a parameter plainText,
    and removes any spaces within the string. removeSpaces will be used
    in substitutionEncrypt to make the user's message much more difficult
    to decrypt by third parties.

    Ex:
    >>>removeSpaces('Test string')
    'Teststring'

    >>>removeSpaces('Test         string')
    'Teststring'
    '''
    plainText = plainText.replace(" ", "")
    return plainText

def substitutionDecrypt_stub(plainText, password):
    '''
    (str, str) ---> str

    This function takes an input from the user, plainText, in the form of an encrypted message,
    and uses the same password, password, specified in the function substitutionEncrypt to decrypt
    the message. The function returns the decrypted message without spaces.

    >>>substitutionDecrypt('qdznrexgjoltkblu', 'ajax')
    'thequickbrownfox'

    >>>substitutionDecrypt('frwpikrfeszdxzwkx', 'kalypso')
    'timewaitsfornoman'
    '''
    pass
    return #string
    
