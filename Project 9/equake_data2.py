'''
    Author: Jordan Mitchell Lewis
    Date: 03/07/2016
    Project: 9.2
    Class: CIS 210, Winter 2016
    Credits: Credits to CIS 210 faculty and python programming in context for starter code
    
    equake_data2 will use a K-means cluster analysis algorithm to analyze earthquake data
    accessed via the USGS API, and report it back to the user.
    
    CHALLENGE: Earthquake dots will get bigger depending on magnitude.
'''

import doctest
import math
from turtle import *
import urllib.request
import random

def visualizeQuakes(k, r):
    '''
    (int, int) ---> None #turtle graphics and print statements

    Calls: readeqf, createCentroids, createClusters

    Function visualizeQuakes will take two parameters;
    k for the number of clusters, and r for the number
    of passes or repeats. The function will use Turtle
    graphics to display where earthquakes occurred on a
    world map, and will color-code them based on their cluster.
    As a side effect, each instance of earthquake will be printed
    after the turtle window has been closed.

    visualizeQuakes returns the value of None.

    >> visualizeQuakes(6, 5)
    ****************************** PASS 0 ******************************
    CLUSTER
    #Random list of magnitudes that will get more similar in proximity with each pass

    #Long printed list of each earthquake instance
    
    '''
    #Create Dictionary of magnitudes and coordinates
    datadict = readeqf()

    quakeCentroids = createCentroids(k, datadict)
    clusters = createClusters(k, quakeCentroids, datadict, r)

    #Turtle setup
    quakeT = Turtle()
    quakeWin = Screen()
    quakeWin.bgpic("worldmap.gif")
    quakeWin.screensize(1800,900)

    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90

    quakeT.hideturtle()
    quakeT.up()

    colorlist = ["red", "purple", "blue", "orange", "cyan", "yellow"]
    
    #Create dots on the map based on latitude and longitude
    for clusterIndex in range(k):
        quakeT.color(colorlist[clusterIndex])
        for akey in clusters[clusterIndex]:
            lon = datadict[akey][1]
            lat = datadict[akey][2]
            quakeT.goto(lon*wFactor, lat*hFactor)                       #CHALLENGE: 
            quakeT.dot(((datadict[akey][0])*10)//2.5)                   #Dot size will vary slightly
                                                                        #depending on the magnitude

    quakeWin.exitonclick()

    print('')
    print('Done')
    return None

def readeqf():
    '''
    () --> dict(int -> list of floats)

    Function readeqf mines earthquake magnitude
    data from a given URL input.

    Returns a dictionary of magnitudes and coordinates, datadict.

    #Data will change depending on the URL being accessed
    >> readeqf()
    {1: [5.0, 128.33, 2.36], 2: [5.1, 142.98, 28.61], 3: [5.1, -80.33, -1.39]}
    '''

    #Access data via the internet
    datafile = urllib.request.urlopen('http://earthquake.usgs.gov/fdsnws/event/1/\
                                       query?format=csv&starttime=2016-02-01&minmagnitude=1')
    '''
    datafile = urllib.request.urlopen('http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv\
                                       &starttime=1916-02-01&latitude=35.6833&longitude=\
                                       139.6833&maxradiuskm=350&minmagnitude=5')
    '''
    #Skip header, declare variables
    next(datafile)
    aline = datafile.readline().decode()
    datadict = {}
    key = 0
    magList = []
    eqdict = {}
    key = 0

    #Find magnitude of each line (earthquake), stop when there is nothing else
    while aline != "":
        key = key + 1
        line = aline.strip().split(',')
        eqInstance = []
        latitude = round(float(line[1]), 2)
        longitude = round(float(line[2]), 2)
        score = float(line[4])
        datadict[key] = [score, longitude, latitude]
        aline = datafile.readline().decode()
    
    datafile.close()
    return datadict

def createCentroids(k, datadict):
    '''
    (int, dict) ---> list of lists

    Called by: visualizeQuakes
    
    Function createCentroids takes two parameters,
    k (an integer), and datadict (a dictionary of
    earthquake data), and creates k number of
    centroids that will be used for the k-cluster
    algorithm.

    Returns a list of lists, centroids

    >> createCentroids(6, datadict) #While datadict is a dictionary of lists
    [[5.4, -73.64, -16.49], [5.3, -171.82, -17.4], [5.1, 153.62, -4.44],
    [5.0, -71.67, -30.58], [5.7, 123.45, 25.57], [5.1, 95.04, 32.06]]
    
    '''
    centroids = []
    centroidCount = 0
    centroidKeys = []

    while centroidCount < k:
        rkey = random.randint(1, len(datadict))
        if rkey not in centroidKeys:
            centroids.append(datadict[rkey])
            centroidKeys.append(rkey)
            centroidCount = centroidCount + 1

    return centroids

def createClusters(k, centroids, datadict, repeats):
    '''
    (int, list of lists, dict of magnitudes and coordinates, int) ---> list of lists ints #print statements

    Function createClusters will have four parameters;
    
    k, an integer number of clusters,
    centroids, the centroids already created by createCentroids,
    datadict, a dictionary of magnitudes and coordinates,
    and repeats, an integer of the number of passes, or times the code will repeat

    createClusters will return clusters, the clusters used for he cluster algorithm.

    >> createClusters(3, centroids(pre-existing), datadict, 5)
    #Print statements for each pass
    [[5, 8, 24, 26, 31, 52, 53, 65, 66, 71, 73, 84, 86, 89, 100, 105, 117, 119, 120, 121, 126],
    [3, 4, 13, 21, 23, 25, 32, 33, 38, 43, 44, 48, 49, 51, 54, 57, 60, 61, 68, 78, 79, 87, 88,
    90, 93, 95, 96, 98, 99, 101]]
    
    '''
    for apass in range(repeats):
        print("*"*40, "PASS", apass, "*"*40)
        clusters = []
        for i in range(k):
            clusters.append([])

        for akey in datadict:
            distances = []
            for clusterIndex in range(k):
                dist = euclidD(datadict[akey], centroids[clusterIndex])
                distances.append(dist)

            mindist = min(distances)
            index = distances.index(mindist)

            clusters[index].append(akey)

        dimensions = len(datadict[1])
        for clusterIndex in range(k):
            sums = [0]*dimensions
            for akey in clusters[clusterIndex]:
                datapoints = datadict[akey]
                for ind in range(len(datapoints)):
                    sums[ind] = sums[ind] + datapoints[ind]
            for ind in range(len(sums)):
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind]/clusterLen

            centroids[clusterIndex] = sums

        for c in clusters:
            print("CLUSTER")
            for key in c:
                print(datadict[key][0], end=" ")
            print()

    return clusters
            
def euclidD(point1, point2):
    '''
    (list of int, list of int) ---> float

    Called by: createClusters

    Computes the euclidean distance between points on a graph.

    euclidean distance is returned as euclidDistance

    >>> euclidD([1, 2],[2, 3]) #Two points
    1.4142135623730951

    >>> euclidD([0, 0],[0, 0]) #Same points
    0.0

    >>> euclidD([1, 2, 5, 3, 1, 4],[8, 5, 2, 6, 9, 4]) #Multiple points
    11.832159566199232
    '''
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index])**2
        total = total + diff

    euclidDistance = math.sqrt(total)
    return euclidDistance

'''
print(doctest.testmod())
'''
print(euclidD((0, 0),(7, 7)))
