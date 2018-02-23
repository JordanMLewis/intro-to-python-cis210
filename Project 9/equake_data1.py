'''
    Author: Jordan Mitchell Lewis
    Project: 9.1
    Date: 03/06/2016
    Class: CIS 210, Winter 2016
    Credits: Professor/GTF for the CIS210stats.py file and functions
             Thanks to Python: Programming in Context for some starter code
             
    This file accesses web data and uses statistics functions to analyze earthquake data.

    CHALLENGE in readeqf for Tokyo earthquakes (warning, there are a lot)
'''

import doctest
import math
from turtle import *
import urllib.request

def equake_main():
    '''
    () -> None/prints data

    Calls:  readeqf, equake_analysis

    Top level function for analysis of
    earthquake data from USGS website.

    Returns None.

    >> equake_main()
    #Results printed as side effect
    '''
    emags = readeqf()                 #Internet data to dictionary
    emags = magnitudeCleanup(emags)   #Clean up the data for processing
    equake_analysis(emags)            #Analyze the dictionary

    return None

def readeqf():
    '''
    () --> dict(int -> float/list of floats)

    Function readeqf mines earthquake magnitude
    data from a given URL input.

    Returns a dictionary of magnitudes, datadict.

    #Data will change depending on the URL being accessed
    >> readeqf()
    {1: [5.2], 2: [5.1], 3: [5.0], 4: [5.7], 5: [5.8], 6: [5.4], 7: [5.3], 8: [5.4], 9: [5.2], 10: [5.6]}
    '''
    datafile = urllib.request.urlopen('http://earthquake.usgs.gov/fdsnws/event/\
                                       1/query?format=csv&starttime=1916-02-01&\
                                       latitude=44.0519&longitude=-123.0867&maxradius\
                                       km=250&minmagnitude=5')
    '''
    datafile = urllib.request.urlopen('http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv\
                                       &starttime=1916-02-01&latitude=35.6833&longitude=\
                                       139.6833&maxradiuskm=350&minmagnitude=5')
    '''

                                        #CHALLENGE: All earthquakes in the
                                        #past 100 years above magnitude 5,
                                        #350km from the center of Tokyo, Japan
    
                                        #PS, the 8.1 earthquake happened just last year in May 2015
                                        
                                        #http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv
                                        #&starttime=1916-02-01&latitude=35.6833&longitude=
                                        #139.6833&maxradiuskm=350&minmagnitude=5

    #Skip header, declare variables
    next(datafile)
    aline = datafile.readline().decode()
    datadict = {}
    key = 0
    magList = []
    
    #Find magnitude of each line (earthquake), stop when there is nothing else
    while aline != "":
        key = key + 1
        magList = aline.split(",")
        score = float(magList[4])
        datadict[key] = [score]
        aline = datafile.readline().decode()

    datafile.close()
    return datadict

def magnitudeCleanup(mags):
    '''
    (Dictionary) ---> (list of magnitudes)

    Called by: equake_main

    Function magnitudeCleanup takes an input, mags,
    a dictionary, and trims it down to a computable list
    of magnitudes as floats.

    magnitudeAnalysis is returned as a list of floats.

    >>> magnitudeCleanup({1: [5.2], 2: [5.1], 3: [5.0], 4: [5.7], 5: [5.8], 6: [5.4], 7: [5.3], 8: [5.4], 9: [5.2], 10: [5.6]})
    [5.2, 5.1, 5.0, 5.7, 5.8, 5.4, 5.3, 5.4, 5.2, 5.6]
    '''
    #Create a list of the values from the dictionary
    magnitudes = list(mags.values())
    magnitudesProcess = []
    magnitudeAnalysis = []

    #converting list to string
    magSTR = ''.join(str(e) for e in magnitudes)

    #Cleaning up the string
    magnitudesProcess = magSTR.replace(']', ",").replace('[', '').split(',')
    magnitudesProcess.pop()

    #Converting each item to float and putting in new list
    for item in magnitudesProcess:
        temp = float(item)
        magnitudeAnalysis.append(temp)
        
    return magnitudeAnalysis

def equake_analysis(mags):
    '''
    (list of magnitudes) ---> None

    Calls: mean, median, mode, freqTable

    Function equake_analysis will take have one parameter, mags,
    a list of earthquake magnitudes. equake_analysis will call
    functions mean, median, and mode to analyze the earthquake
    magnitude data, and report the results.

    equake_analysis returns the value of None.

    >> equake_analysis([5.2, 5.1, 5.0, 5.7, 5.8, 5.4, 5.3, 5.4, 5.2, 5.6])
    #Mean, Median, and Mode of the data
    #Table that maps magnitudes to their frequency
    
    '''
    #Printing all important data about magnitudes
    print('')
    print("For earthquake events of magnitude 5 or higher,")
    print("in the 250 km radius centered around Eugene, OR, over the past 100 years:")
    print('')
    print("The average earthquake magnitude is:", mean(mags))
    print("The median earthquake magnitude is:", median(mags))
    print("The most common earthquake magnitude(s) are:", mode(mags))
    print('')
    freqTable(mags)
    return None


#########################################################################

"""
Functions from text Ch. 4, for computing
range, median, mean, mode, standard deviation
frequency table, frequency chart
"""

def mode(alist):
    '''
    (list of numbers)-> number

    Calls: genFrequencyTable

    Return list of number(s) that
    occur()s most frequently in alist.

    > mode([9, 8, 7, 6, 5])
    [5, 6, 7, 8, 9] #unordered
    > mode([1, 2, 3, 3, 1, 4, 5])
    [1, 3] #unordered
    >>> mode([1, 1, 1, 1])
    [1]
    '''
    frequencyDict = genFrequencyTable(alist)    #Gather frequencies in dictionary
    countlist = frequencyDict.values()          #Collect dictionary values
    maxcount = max(countlist)                   #Find the highest value

    modeList = []
    for item in frequencyDict:                  #If any other values are equal to the max, add them to the mode list
        if frequencyDict[item] == maxcount:
            modeList.append(item)
            
    return modeList

def standardDev(alist):
    '''(list of numbers) -> float

    Returns standard deviation
    for numbers in non-empty alist.

    >>> standardDev([7, 11, 9, 18, 15, 12])
    4.0
    >>> standardDev([2, 10, 6, 24, 18, 12])
    8.0
    >>> standardDev([20, 32, 21, 26, 33, 22, 18])
    5.94017796751194
    '''
    avg = mean(alist)
    total = 0
    for item in alist:
        diff = item - avg
        diffsq = diff ** 2
        total += diffsq

    sdev = math.sqrt(total / (len(alist) - 1))
    return sdev
    

def mean(alist):
    '''(list of numbers) -> float

    Returns average (mean) of ints
    in non-empty alist.

    >>> mean([1, 3, 5])
    3.0
    >>> mean([5, 3.5, 3, 4.5])
    4.0
    '''
    
    avg = sum(alist) / len(alist)

    return avg

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

def genFrequencyTable(alist):
    '''(list of numbers) -> dictionary

    Generate a frequency dictionary with
    number of occurrences of each number
    in alist.

    Called by: mode, freqTable, freqChart

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

    Calls:  genFrequencyTable, drawChart

    > freqTable([1, 2, 3, 3, 1, 4, 5])
    [frequency occurrences table] 
    '''
    freqD = genFrequencyTable(alist)
    drawTable(freqD)
 
    return None

def freqChart(alist):
    '''(list of numbers) -> None

    Draw frequency chart of count
    of each number in alist.
    None value is returned.

    Calls:  genFrequencyTable, drawChart

    > freqChart([1, 2, 3, 3, 1, 4, 5])
    [frequency occurrences chart] 
    '''
    freqD = genFrequencyTable(alist)
    drawChart(freqD)
        
    return None

def drawTable(freqD):
    '''(dict) -> None

    Display each key-value pair
    from freqD in a frequency table.
    None value is returned.
   
    Called by: freqTable

    >> drawTable({1:2, 2:1, 3:2, 4:1, 5:1})
    ITEM  FREQUENCY
    1     2
    2     1
    3     2
    4     1
    5     1
    '''
    iteml = list(freqD.keys())
    iteml.sort()

    #title = 'ITEM' + (' '*2) + 'FREQUENCY'
    #print(title)
    #print('%-6s %-9s' % ('ITEM', 'FREQUENCY'))
    print('{: <6} {: <9}'.format('MAGs', 'FREQUENCY'))

    for item in iteml:
        #print('%-6s %-9d' % (item, freqD[item]))
        print('{: <6} {: <9}'.format(item, freqD[item]))

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

print(doctest.testmod())

    
