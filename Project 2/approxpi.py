'''
    Author: Jordan Mitchell Lewis
    Class: CIS 210, Winter 2016
    Date: 01/19/2016
    Credits: Bradley N. Miller and David L. Ranum for starter code
    This file contains functions that use a Monte Carlo algorithm to approximate the value of pi,
    and graphically represents it using Turtle graphics. This file also contains a function that identifies
    whether or not a simulated point was inside the circle from montePi, or outside of the circle.
'''

import random
import math
import turtle

def montePi(numDarts):
    '''
    (int) ---> (float)

    This function contains code used to approximate pi using a Monte Carlo algorithm.
    Function showMontePi takes an input in the form of one parameter, numDarts, the number of times
    the approximating pi process should be run.

    Examples below may not be replicable due to the nature of this function:
    >>>montePi(10)
    3.08

    >>>montePi(100000)
    3.143072
    '''
    circle = 0
    r = 1 
    for i in range(numDarts): #For loop determining through input how many "darts" will be thrown
        x = random.random()
        y = random.random()
        TorF = isInCircle(x, y, r) #isInCircle called here
        if TorF == True:
            circle = circle + 1
        else:
            pass
        
    pi = circle / numDarts * 4
    return pi

def showMontePi(numDarts):
    '''
    (int) ---> (float)
    
    This function contains code used to approximate pi using a Monte Carlo algorithm.
    Function showMontePi takes an input in the form of one parameter, numDarts, the number of times
    the approximating pi process should be run. It then graphically displays numDarts number of points
    on a graph to visually represent the algorithm taking place.

    Examples below may not be replicable due to the nature of this function:
    >>>showMontePi(100)
    3.08

    >>>showMontePi(100000)
    3.143072
    '''
    wn = turtle.Screen()
    drawingT = turtle.Turtle()

    wn.setworldcoordinates(-2, -2, 2, 2)

    drawingT.up()
    drawingT.goto(-1, 0)
    drawingT.down()
    drawingT.goto(1, 0)

    drawingT.up()
    drawingT.goto(0, 1)
    drawingT.down()
    drawingT.goto(0, -1)

    circle = 0
    drawingT.up()

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        d = math.sqrt((x ** 2) + (y ** 2))

        drawingT.goto(x, y)

        if d <= 1:
            circle = circle + 1
            drawingT.color("blue") #Color of coordinates inside the circle
        else:
            drawingT.color("red") #Color of coordinates outside the circle

        drawingT.dot()
    
    pi = circle / numDarts * 4
    pi2 = math.pi
    percent_error = abs(((pi - pi2)/pi2) * 100)
    wn.exitonclick()
    print('With {} iterations (darts):'.format(numDarts))
    print('My approximate value for pi is: {}'.format(pi))
    print('Math lib pi value is: {}'.format(pi2))
    print('This is a {} percent error.'.format(round(percent_error, 2)))
    print('')
    return pi

def isInCircle(x, y, r):
    '''
    (int) ---> (Boolean)
    
    Function isInCircle is called by montePi and takes inputs in the form of three parameters:
    the x and y values of a point, and a radius, r. isInCircle will return True if the input point
    is inside the circle centered at point (0,0) with radius r, and False if otherwise.

    Ex:
    >>>isInCircle(0, 0, 1)
    True

    >>>isInCircle(.5, .5, 1)
    True

    >>>isInCircle(1, 2, 1)
    False
    '''
    d = math.sqrt((x ** 2) + (y ** 2))
    if d <= r:
        return True
    else:
        return False
    
def montePi_stub(numDarts):
    '''
    (int) ---> (float)

    This function contains code used to approximate pi using a Monte Carlo algorithm.
    Function showMontePi takes an input in the form of one parameter, numDarts, the number of times
    the approximating pi process should be run.

    Examples below may not be replicable due to the nature of this function:
    >>>montePi(10)
    3.08

    >>>montePi(100000)
    3.143072
    '''
    pass
    return #float

def isInCircle_stub(x, y, r):
    '''
    (int) ---> (Boolean)
    
    Function isInCircle is called by montePi and takes inputs in the form of three parameters:
    the x and y values of a point, and a radius, r. isInCircle will return True if the input point
    is inside the circle centered at point (0,0) with radius r, and False if otherwise.

    Ex:
    >>>isInCircle(0, 0, 1)
    True

    >>>isInCircle(.5, .5, 1)
    True

    >>>isInCircle(1, 2, 1)
    False
    '''
    pass
    return #Boolean
