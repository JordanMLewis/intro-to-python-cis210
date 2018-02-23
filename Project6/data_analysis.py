'''
    Author: Jordan Mitchell Lewis
    Date: 02/14/2016
    Class: CIS 210, Winter 2016
    Credits: Thank you to Bradley N. Miller and David L. Ranum for the starter code.
    This file contains various functions used for data analysis and central tendency (median, mode, etc)
'''

from turtle import *
import doctest

def genFrequencyTable(alist):
    '''
    (list) ---> dictionary

    Function genFrequencyTable will take one parameter, alist, and will return a dictionary of
    the values of alist and their respective frequencies.

    >>> genFrequencyTable([1, 4, 8, 5, 1, 4, 7, 1, 5, 9, 8, 7, 4, 1, 4, 2, 3, 5])
    {1: 4, 2: 1, 3: 1, 4: 4, 5: 3, 7: 2, 8: 2, 9: 1}

    >>> genFrequencyTable([1, 1, 1, 1, 1, 1, 1])
    {1: 7}

    >>> genFrequencyTable([1])
    {1: 1}
    '''
    countDict = {}
    for item in alist:
        if item in countDict: #If the item is already in the dictionary, add one to the value
            countDict[item] = countDict[item] + 1
        else:                 #If it's not already there, create a new entry in the dictionary
            countDict[item] = 1
    return countDict

def median(alist):
    '''
    (list) ---> integer or float

    Function median takes one input, alist, a list of integers and or floats,
    and returns the median value or element of that list.

    >>> median([1, 2, 3]) #Input has odd number of items
    2

    >>> median([1, 2, 3, 4]) #Input has even number of items
    2.5

    >>> median([1, 1, 1, 1, 1, 1, 1]) #Input with all the same items
    1
    
    >>> median([1]) #List with only one item
    1

    >>> median([1, 2.5, 3.6, 3.8, 4.5])
    3.6
    '''
    copylist = alist[:] #make a copy of the list
    copylist.sort()
    
    if len(copylist)%2 == 0: #even length
        rightmid = len(copylist)//2
        leftmid = rightmid - 1
        median = (copylist[leftmid] + copylist[rightmid])/2
    else: #odd length
        mid = len(copylist)//2
        median = copylist[mid]
    return median

def frequencyTable(alist):
    '''
    (list) ---> None

    Function frequencyTable takes one input, alist, as a list of numbers.
    The function will print all of the values in alist in a table format
    as well as the frequency at which they occur next to each value.
    The value None is returned.

    >>> frequencyTable([1, 4, 8, 5, 1, 4, 7, 1, 5, 9, 8, 7, 4, 1, 4, 2, 3, 5])
    ITEM FREQUENCY
    1       4
    2       1
    3       1
    4       4
    5       3
    7       2
    8       2
    9       1
    '''
    countDict = genFrequencyTable(alist)
    itemlist = list(genFrequencyTable(alist)) #Function call to create the list from dictionary
    itemlist.sort()

    print("ITEM", "FREQUENCY")

    for item in itemlist:
        print(item, "     ", countDict[item]) #Print the number, and then the frequency
    return None

def frequencyChart(alist):
    '''
    (list) ---> None

    Function frequencyChart takes one input alist, a list of at least 2 different numbers,
    and creates a frequency chart (bar graph) of the values and the frequency at which they
    occur using Turtle graphics. Function frequencyChart will return the value of None.

    >>> frequencyChart([1, 2.5]) #List of at least 2 numbers

    >> frequencyChart([1, 2, 3, 4, 5, 6, 8, 5, 2, 1, 4, 7, 9, 6, 3, 2, 1, 4]) #Turtle graphics drawn as a side effect
    
    '''
    countDict = genFrequencyTable(alist)
    itemlist = genFrequencyTable(alist)
    itemlist = list(countDict.keys())
    minitem = 0
    maxitem = len(itemlist) - 1

    countlist = countDict.values()
    maxcount = max(countlist)

    wn = Screen()
    setworldcoordinates(-1, -1, maxitem + 1, maxcount + 1) #Set the scaled resolution for the Turtle window
    hideturtle()

    up()
    goto(0, 0)
    down()
    goto(maxitem, 0)
    up()

    goto(-1, 0)
    write("0", font=("Helvetica", 16, "bold")) #Size of min number zero
    goto(-1, maxcount)
    write(str(maxcount), font=("Helvetica", 16, "bold")) #Size of max number occuring in the list

    for index in range(len(itemlist)):
        goto(index, -1)
        write(str(itemlist[index]), font=("Helvetica", 10, "bold")) #Item text size

        goto(index, 0)
        down()
        goto(index, countDict[itemlist[index]])
        up()
    wn.exitonclick()
    return None

'''
doctest.testmod(verbose=True)
'''
