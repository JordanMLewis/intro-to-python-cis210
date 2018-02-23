'''
    Author: Jordan Mitchell Lewis
    Date: 2/08/2016
    Class: CIS 210, Winter 2016
    This file creates/draws a barcode using Turtle graphics based on a specified zipcode. 
'''

from turtle import *

def zipToBar(zipcode):
    '''
    (int) ---> None

    This function acts as the main function for the rest of program.
    It will handle resetting the turtle, creating a check digit from zipcode,
    and drawing the barcode in turtle graphics. It will return None, but will
    produce Turtle graphics to display the barcode.

    >>>zipToBar(12345)
    
    '''
    checkDigitNum = checkDigit(zipcode)
    turtleReset()
    drawBar(zipcode, checkDigitNum)
    return None

def checkDigit(zipcode):
    '''
    (int) ---> int

    This function uses the input zipcode and creates a check digit
    to ensure that the barcode has been read by the machine correctly.
    checkDigitNum is returned as an integer.

    >>>checkDigit(97403):
    7

    >>>checkDigit(123456789):
    5
    '''
    zipcode = str(zipcode) #Convert to string
    sumDigit = 0
    for ch in zipcode:
        sumDigit += int(ch)
    checkDigitNum = 10 - (sumDigit % 10)
    return checkDigitNum

def drawBar(zipcode, checkDigitNum):
    '''
    (int) ---> None

    This function will take an input zipcode and checkDigitNum in the form of an integer,
    and will use it to draw a barcode in the turtle module. The function returns the value of None.

    >>>drawBar(12345)
    
    '''
    zipcode = str(zipcode) #Convert to string
    drawY()
    for ch in zipcode:
        if int(ch) == 0:
            drawZero()
        elif int(ch) == 1:
            drawOne()
        elif int(ch) == 2:
            drawTwo()
        elif int(ch) == 3:
            drawThree()
        elif int(ch) == 4:
            drawFour()
        elif int(ch) == 5:
            drawFive()
        elif int(ch) == 6:
            drawSix()
        elif int(ch) == 7:
            drawSeven()
        elif int(ch) == 8:
            drawEight()
        else:
            drawNine()
    
    if checkDigitNum == 1: #Add the checkDigit onto the end of the barcode (before last line)
        drawOne()
    elif checkDigitNum == 2:
        drawTwo()
    elif checkDigitNum == 3:
        drawThree()
    elif checkDigitNum == 4:
        drawFour()
    elif checkDigitNum == 5:
        drawFive()
    elif checkDigitNum == 6:
        drawSix()
    elif checkDigitNum == 7:
        drawSeven()
    elif checkDigitNum == 8:
        drawEight()
    else:
        drawNine()
    drawY()
    return None

def turtleReset():
    '''
    None ---> None

    This function primes the turtle graphics window for the zipToBar function
    by setting the speed of the turtle, adjusting the module resolution, and
    making other adjustments. This function takes no parameters and returns
    the value of None.

    >>>turtleReset()

    '''
    reset() #Clear the graphics/window
    pu()
    speed(0)
    setpos(-300, y=0) #Start on the side of the window
    setup(width=1000, height=700, startx=None, starty=None)
    return None

def drawY():
    '''
    (None) ---> None

    This function draws a line symbolizing a one, or a yes.
    The function take no parameters and returns the value of None.
    As a side effect, turtle graphcis are drawn.

    >>>drawY()
    
    '''
    pd()
    seth(90)
    fd(100)
    pu()
    sety(0)
    seth(0)
    fd(10) #Space between each bar
    return None

def drawN():
    '''
    (None) ---> None

    This function draws half of a line symbolizing a zero, or a no.
    The function take no parameters and returns the value of None.
    As a side effect, turtle graphcis are drawn.

    >>>drawN()
    
    '''
    pd()
    seth(90)
    fd(50)
    pu()
    sety(0)
    seth(0)
    fd(10) #Space between each bar
    return None

def drawZero():
    '''
    (None) ---> None

    This function contains the order of calls to the functions drawY and
    drawN needed to produce a segment of barcode to represent the number zero.
    This function takes no inputs and returns the value of None. Turtle graphics
    are produced as a side effect of this function.

    >>>drawZero()
    
    '''
    drawY()
    drawY()
    drawN()
    drawN()
    drawN()
    return None
    
def drawOne():
    '''
    (None) ---> None

    This function contains the order of calls to the functions drawY and
    drawN needed to produce a segment of barcode to represent the number one.
    This function takes no inputs and returns the value of None. Turtle graphics
    are produced as a side effect of this function.

    >>>drawOne()
    
    '''
    drawN()
    drawN()
    drawN()
    drawY()
    drawY()
    return None
    
def drawTwo():
    '''
    (None) ---> None

    This function contains the order of calls to the functions drawY and
    drawN needed to produce a segment of barcode to represent the number two.
    This function takes no inputs and returns the value of None. Turtle graphics
    are produced as a side effect of this function.

    >>>drawTwo()
    
    '''
    drawN()
    drawN()
    drawY()
    drawN()
    drawY()
    return None

def drawThree():
    '''
    (None) ---> None

    This function contains the order of calls to the functions drawY and
    drawN needed to produce a segment of barcode to represent the number three.
    This function takes no inputs and returns the value of None. Turtle graphics
    are produced as a side effect of this function.

    >>>drawThree()
    
    '''
    drawN()
    drawN()
    drawY()
    drawY()
    drawN()
    return None

def drawFour():
    '''
    (None) ---> None

    This function contains the order of calls to the functions drawY and
    drawN needed to produce a segment of barcode to represent the number four.
    This function takes no inputs and returns the value of None. Turtle graphics
    are produced as a side effect of this function.

    >>>drawFour()
    
    '''
    drawN()
    drawY()
    drawN()
    drawN()
    drawY()
    return None

def drawFive():
    '''
    (None) ---> None

    This function contains the order of calls to the functions drawY and
    drawN needed to produce a segment of barcode to represent the number five.
    This function takes no inputs and returns the value of None. Turtle graphics
    are produced as a side effect of this function.

    >>>drawFive()
    
    '''
    drawN()
    drawY()
    drawN()
    drawY()
    drawN()
    return None

def drawSix():
    '''
    (None) ---> None

    This function contains the order of calls to the functions drawY and
    drawN needed to produce a segment of barcode to represent the number six.
    This function takes no inputs and returns the value of None. Turtle graphics
    are produced as a side effect of this function.

    >>>drawSix()
    
    '''
    drawN()
    drawY()
    drawY()
    drawN()
    drawN()
    return None

def drawSeven():
    '''
    (None) ---> None

    This function contains the order of calls to the functions drawY and
    drawN needed to produce a segment of barcode to represent the number seven.
    This function takes no inputs and returns the value of None. Turtle graphics
    are produced as a side effect of this function.

    >>>drawSeven()

    '''
    drawY()
    drawN()
    drawN()
    drawN()
    drawY()
    return None

def drawEight():
    '''
    (None) ---> None

    This function contains the order of calls to the functions drawY and
    drawN needed to produce a segment of barcode to represent the number eight.
    This function takes no inputs and returns the value of None. Turtle graphics
    are produced as a side effect of this function.

    >>>drawEight()

    '''
    drawY()
    drawN()
    drawN()
    drawY()
    drawN()
    return None

def drawNine():
    '''
    (None) ---> None

    This function contains the order of calls to the functions drawY and
    drawN needed to produce a segment of barcode to represent the number nine.
    This function takes no inputs and returns the value of None. Turtle graphics
    are produced as a side effect of this function.

    >>>drawNine()

    '''
    drawY()
    drawN()
    drawY()
    drawN()
    drawN()
    return None

def zipToBar_stub(zipcode):
    '''
    (int) ---> None

    This function acts as the main function for the rest of program.
    It will handle resetting the turtle, creating a check digit from zipcode,
    and drawing the barcode in turtle graphics. It will return None, but will
    produce Turtle graphics to display the barcode.

    >>>zipToBar(12345)
    
    '''
    pass
    return None

def checkDigit_stub(zipcode):
    '''
    (int) ---> int

    This function uses the input zipcode and creates a check digit
    to ensure that the barcode has been read by the machine correctly.
    checkDigit is returned as an integer.

    >>>checkDigit(97403):
    7

    >>>checkDigit(123456789):
    5
    '''
    pass
    return None

def drawBar_stub(zipcode, checkDigitNum):
    '''
    (int) ---> None

    This function will take an input zipcode and checkDigitNum in the form of an integer,
    and will use it to draw a barcode in the turtle module. The function returns the value of None.

    >>>drawBar(12345)
    
    '''
    pass
    return None

def turtleReset_stub():
    '''
    None ---> None

    This function primes the turtle graphics window for the zipToBar function
    by setting the speed of the turtle, adjusting the module resolution, and
    making other adjustments. This function takes no parameters and returns
    the value of None.

    >>>turtleReset()

    '''
    pass
    return None
