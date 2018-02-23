def distance(a, b):
    '''
    list of int, list of int ---> float

    Computer the euclidean distance.
    '''
    acc = 0
    total = 0
    for i in range(len(a)):
        total += (a[i] - b[i])**2
        
    return sqrt(total)







def createClusters(k, centroids, datadict, r):
    '''
    '''
    clusters = [[], [], []] #this line is wrong if he doesn't equal 3

    #How many times will we try this
    for i in range(r):
        clusters = [[], [], []]
        
        #Grab data points
        for key in datadict:
            
            #Do the test to see which centroid is closest
            for c in centroids:
                d = distance(c, datadict[key])
                
