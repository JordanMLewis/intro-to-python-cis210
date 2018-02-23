"""
CIS210 Project 6 Part 2 Winter 2016

Functions from text Ch. 4.
Median, frequency table, visualization


list, dictionary, basic data processing
"""

import doctest
from turtle import *

def even(n):
    '''(num) -> boolean

    Return True if n is even,
    else return False

    >>> even(4)
    True
    >>> even(1)
    False
    >>> even(0)
    True
    '''
    return (n % 2) == 0

def median(alist):
    '''(list of numbers) -> number

    Return median of alist (of len > 0).

    >>> median([5, 7, 1, 3]) # list with even number of items
    4.0
    >>> median([1, 2, 2, 3, 99]) # list with odd number of items
    2
    >>> median([99]) # list with 1 item
    99
    >>> median([0, 0, 0, 0]) # list with all same item (even number)
    0.0
    '''
    copyl = alist[:]
    copyl.sort()
    copylen = len(copyl)
    
    if even(copylen):
        rmid = copylen // 2
        lmid = rmid - 1
        medi = (copyl[lmid] + copyl[rmid]) / 2
    else:
        mid = copylen // 2
        medi = copyl[mid]

    return medi

def genFreqTable(alist):
    '''(list of numbers) -> dictionary

    Generate a frequency dictionary with
    number of occurrences of each number
    in alist.

    Called by:  freqTable, freqChart

    > genFreqTable([1, 2, 3, 3, 1, 4, 5])
    {1:2, 2:1, 3:2, 4:1, 5:1}
    '''
    freqD = {}

    for item in alist:
        if item in freqD:
            freqD[item] += 1
        else:
            freqD[item] = 1

    return freqD

def freqTable(alist):
    '''(list of numbers) -> None

    Print frequency table of count
    of each number in alist.
    None value is returned.

    Calls:  genFreqTable, drawChart

    > freqChart([1, 2, 3, 3, 1, 4, 5])
    [frequency occurrences chart] 
    '''
    freqD = genFreqTable(alist)
    drawTable(freqD)
 
    return None

def freqChart(alist):
    '''(list of numbers) -> None

    Draw frequency chart of count
    of each number in alist.
    None value is returned.

    Calls:  genFreqTable, drawChart

    > freqChart([1, 2, 3, 3, 1, 4, 5])
    [frequency occurrences chart] 
    '''
    freqD = genFreqTable(alist)
    drawChart(freqD)
        
    return None

def drawTable(freqD):
    '''(dict) -> None

    Display each key-value pair
    from freqD in a frequency table.
    None value is returned.
   
    Called by: freqTable

    >>> drawTable({1:2, 2:1, 3:2, 4:1, 5:1})
    ITEM  FREQUENCY
    1     2
    2     1
    3     2
    4     1
    5     1
    '''
    iteml = list(freqD.keys())
    iteml.sort()

    title = 'ITEM' + (' '*2) + 'FREQUENCY'
    print(title)

    for item in iteml:
        print(item, ' '*3, freqD[item])

    return None

def drawChart(freqD):
    '''(dictionary of items/number occurrences) -> None
    
    Draw frequency chart of
    items and frequency count in freqD.
    None value is returned.

    Called by: freqChart

    > drawChart(6, 10)
    [frequency chart]
    '''
    # find min and max items
    # for drawing graph outline
    iteml = list(freqD.keys())
    iteml.sort()
    minitem = 0
    maxitem = len(iteml) - 1

    # do the same for occurrence values
    countl = freqD.values()
    maxcount = max(countl)

    # use these numbers to scale
    # the canvas appropriately
    wn = Screen()
    setworldcoordinates(-1, -1, maxitem+1, maxcount+1)

    # set up the turtle
    hideturtle()
    speed('fastest')

    # draw the chart outlines
    penup()
    goto(0,0)
    pendown()
    goto(maxitem, 0)
    penup()

    goto(-1, 0)
    write('0', font=('Helvetica', 16, 'bold'))
    goto(-1, maxcount)
    write(str(maxcount), font=('Helvetica', 16, 'bold'))

    #label the x-axis
    for i in range(len(iteml)):
        goto(i, -1)
        write(str(iteml[i]), font=('Helvetica', 16, 'bold'))

    #graph the number of occurrences
        goto(i, 0)
        pendown()
        goto(i, freqD[iteml[i]])
        penup()

    #wn.exitonclick()
    return None

shortlist = [1, 2, 3, 1, 2, 2, 2, 4, 1]

equakes = [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3,
           2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6,
           4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1,
           4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9,
           2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7,
           4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7,
           3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1,
           2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1,
           2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3,
           6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4,
           2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0,
           2.5, 4.9, 4.9, 2.5, 4.8, 3.1, 4.9,
           4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5,
           4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6,
           2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1,
           2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1,
           2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5,
           4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1,
           4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0,
           2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2,
           3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5,
           2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5,
           2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7,
           2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6,
           2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9,
           2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1,
           3.1, 4.6, 2.8, 3.1, 6.3]

       
          
    
    

    

    
    
