'''
    Project 8 (Counting majors)
    Name: Jordan Mitchell Lewis
    Date: 02/28/2016
    Class: CIS 210, 2016
    Credits: Bradley N. Miller, David L. Ranum, Project 6 example for starter code
    
    This file contains functions that read a text file and determine the frequency of its data.

    Challenge: ACCEPTED (altered the drawTable function to print the report more neatly)
'''

import doctest
from turtle import *

def majors_main():
    '''
    () ---> None

    Calls: majorsf_to_li, report

    Top level function for analysis of
    data in file of majors of students in CIS 210 W16.

    Access major file, create list
    of relevant data, and report the mode
    and frequency table for the data in the file. Returns None.

    >>> majors_main()
    Most represented major(s):
    CIS
    <BLANKLINE>
    MAJOR  FREQUENCY
    ACTG   1
    ARCH   1
    BI     2
    CIS    82
    EALL   1
    EC     1
    ENG    1
    ESCI   1
    GER    1
    GS     2
    GSS    1
    HPHY   1
    MACS   7
    MARB   1
    MATH   14
    MPS    1
    MUS    1
    PBA    11
    PEN    1
    PHYS   2
    PJ     1
    SPAN   1
    UNDL   16
    '''
    with open('majors_CIS210_W16.txt', 'r') as majorsf:
        majorsli = majorsf_to_li(majorsf)               #Function call to create list of majors
    report(majorsli)                                    #Report data to user
    return None

def majorsf_to_li(majorsf):
    '''
    (file) ---> list

    Called by: majors_main

    Function majorsf_to_li takes one input, majorsf (a file), and returns
    majorsli, a list.

    >> majorsf_to_li(majorsf)
    [creates a list of each line in the file]
    '''
    majorsf.seek(6)                             #Skip header
    majorsli = majorsf.read().splitlines()      #Create list line by line
    majorsf.close()
    return majorsli
    
def report(alist):
    '''
    (list) ---> None

    Calls: mode, frequencyTable

    Function report will have one parameter, alist, and return the None value.
    It will call function mode to determine the most frequently occurring item
    (major) in the argument list, and then report the result. report will also
    call frequencyTable to report the number of occurrences for each item in alist.

    >>> report(['CIS', 'CIS', 'CIS', 'MATH', 'WGS', 'COLT', 'CIS', 'EALL'])
    Most represented major(s):
    CIS
    <BLANKLINE>
    MAJOR  FREQUENCY
    CIS    4
    COLT   1
    EALL   1
    MATH   1
    WGS    1

    >> report(['CIS', 'CIS', 'CIS', 'MATH', 'MATH', 'MATH'])
    Most represented major(s):
    MATH CIS 
    <BLANKLINE>
    MAJOR  FREQUENCY
    CIS    3
    MATH   3
    '''

    #Report most frequency major
    print('Most represented major(s):')
    if len(mode(alist)) > 1:
        for item in (mode(alist)):
            print(item, end=" ")
        print('')
    else:
        print((mode(alist)[0]))
    print('')
    
    #Call to create print majors and frequency
    frequencyTable(alist)
    return None

def frequencyTable(alist):
    '''
    (list of numbers) -> None

    Print frequency table of count of each number in alist.
    None value is returned.

    Calls:  genFreqTable, drawTable

    >>> frequencyTable(['CIS', 'CIS', 'CIS', 'MATH', 'WGS', 'COLT', 'CIS', 'EALL'])
    MAJOR  FREQUENCY
    CIS    4
    COLT   1
    EALL   1
    MATH   1
    WGS    1
    '''
    freqD = genFreqTable(alist)
    drawTable(freqD)
    return None

def genFreqTable(alist):
    '''
    (list) -> dictionary

    Generate a frequency dictionary with
    number of occurrences of each number
    in alist.

    Called by: frequencyTable

    >>> genFreqTable([1, 2, 3, 3, 1, 4, 5]) #List of integers
    {1: 2, 2: 1, 3: 2, 4: 1, 5: 1}

    >> genFreqTable(['CIS', 'CIS', 'CIS', 'MATH', 'WGS', 'COLT', 'CIS', 'EALL']) #List of strings
    #Order will change
    {'COLT': 1, 'EALL': 1, 'MATH': 1, 'WGS': 1, 'CIS': 4}
    '''
    freqD = {}
    for item in alist:
        if item in freqD:
            freqD[item] += 1     #Add one to value if it already exists in the dictionary
        else:
            freqD[item] = 1      #Otherwise, create a new entry
    return freqD

def drawTable(freqD):
    '''
    (dict) -> None

    Display each key-value pair from freqD in a frequency table.
    None value is returned.
   
    Called by: report, genFreqTable

    >>> drawTable({'ACTG':1, 'ARCH':1, 'BI':2, 'CIS':82, 'EALL':1})
    MAJOR  FREQUENCY
    ACTG   1
    ARCH   1
    BI     2
    CIS    82
    EALL   1
    '''
    iteml = list(freqD.keys())
    iteml.sort()                                #Alphabetical sorting

    title = 'MAJOR' + (' '*2) + 'FREQUENCY'
    print(title)

    #Table creation + CHALLENGE
    for item in iteml:
        print(item, ' '*(5-len(item)), freqD[item])
    return None

def mean(alist):
    '''
    (list of numbers) ---> float

    Function mean will have one parameter, alist, a list of numbers,
    and will return a number which is the average value of the numbers in alist.

    >>> mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) #Even number of items in list
    5.5

    >>> mean([1, 2, 3, 4, 5, 6, 7, 8, 9]) #Odd number of items in list
    5.0

    >>> mean([99]) #One item in list
    99.0
    '''
    mean = sum(alist) / len(alist)
    return mean

def mode(alist):
    '''
    (list) ---> list

    Calls: genFreqTable

    Function mode will have one parameter, alist, a list of strings (majors),
    and will return a list of the majors(s) that occur(s) the most frequently in alist.
    The function will also work with numbers.

    >>> mode(['CIS', 'CIS', 'CIS', 'CIS', 'EALL', 'MATH']) #List of strings
    ['CIS']

    >>> mode([1, 1, 1, 2, 2, 3, 4, 5, 8, 8, 8, 8, 9]) #List of integers
    [8]

    >>> mode([1, 2, 3, 3, 5, 5, 7, 84, 21, 35, 0]) #List with two integers of same frequency
    [3, 5]

    '''
    frequencyDict = genFreqTable(alist) #Gather frequencies in dictionary
    countlist = frequencyDict.values()  #Collect dictionary values
    maxcount = max(countlist)           #Find the highest value

    modeList = []
    for item in frequencyDict:          #If any other values are equal to the max, add them to the mode list
        if frequencyDict[item] == maxcount:
            modeList.append(item)
            
    return modeList

print(doctest.testmod())

