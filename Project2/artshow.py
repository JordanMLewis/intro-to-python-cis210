'''
    Author: Jordan Mitchell Lewis
    Class: CIS 210, Winter 2016
    Date: 01/19/2016
    Credits: Thanks to Python and Turtle graphics for making this project possible.
    This file contains a list of fuctions that use Turtle commands to create my "art show".
'''

from turtle import *

def art_show():
    '''
    None ---> None

    This function calls each individual function of my larger project to produce my art show using Turtle commands.
    It is otherwise known as the main function, holding all of the pieces together. It also defines the speed,
    screen resolution, and background color of the turtle graphics display.
    Executing the code does not print or return any relevant values; it only draws the picture.

    Ex:
    >>>art_show()
    
    >>>art_show(orange)
    Traceback (most recent call last):
       File "<pyshell#0>", line 1, in <module>
         art_show(orange)
    NameError: name 'orange' is not defined
    '''
    bgcolor("sky blue") #Peter Gabriel: "Sky blue... So tired of all this traveling..."
    speed(0)
    setup(width=700, height=700, startx=None, starty=None)
    reset()
    myLand()
    myHouse()
    myTree()
    myLake()
    return None

def myLand():
    '''
    None ---> None

    This function draws the ground or land that will appear in my art show and colors it.
    Executing the code does not print or return any relevant values; it only draws the picture.

    Ex:
    >>>myLand()
    
    >>>myLand(green)
    Traceback (most recent call last):
       File "<pyshell#0>", line 1, in <module>
         myLand(green)
    NameError: name 'green' is not defined
    '''
    pu()
    setpos(-350, 0)
    pd()
    fillcolor('#395D33') #This determines the color of the ground
    begin_fill()
    fd(700)
    rt(90)
    fd(350)
    rt(90)
    fd(700)
    rt(90)
    fd(350)
    end_fill()
    return None

def myHouse():
    '''
    None ---> None

    This function draws the foundation and roof of the house that will appear in my art show and colors it.
    Executing the code does not print or return any relevant values; it only draws the picture.

    Ex:
    >>>myHouse()
    
    >>>myHouse(green)
    Traceback (most recent call last):
       File "<pyshell#0>", line 1, in <module>
         myHouse(green)
    NameError: name 'green' is not defined
    '''
    pu()
    setpos(200, 0)
    pd()
    seth(90)
    fillcolor("#b69b4c") #This determines the color of the house
    begin_fill()
    for item in range(4): #Builds foundation of the house
        fd(80)
        left(90)
    end_fill()
    fd(80)
    fillcolor("red") #This determines the color of the roof on the house
    begin_fill()
    seth(0)
    for item in range(3): #builds triangular roof
        left(120)
        fd(80)
    end_fill()
    return None

def myTree():
    '''
    None ---> None

    This function draws the tree that will appear next to the house in my art show and colors it.
    Executing the code does not print or return any relevant values; it only draws the picture.

    Ex:
    >>>myTree()
    
    myTree(green)
    Traceback (most recent call last):
       File "<pyshell#0>", line 1, in <module>
         myTree(green)
    NameError: name 'green' is not defined
    '''
    pu()
    setpos(300, 0)
    fillcolor("#825201") #Tree trunk color
    begin_fill()
    seth(90)
    pd()
    fd(130) #Tree trunk begins here
    left(90)
    fd(20)
    left(90)
    fd(130)
    left(90)
    fd(20)
    end_fill()
    fillcolor("#3A5F0B") #Leaves color
    pu()
    setpos(325, 120)
    begin_fill()
    pd()
    circle(40, None, None) #Leaves begin here
    pu()
    setpos(315, 130)
    pd()
    circle(40, None, None)
    pu()
    setpos(300, 140)
    pd()
    circle(40, None, None)
    pu()
    setpos(285, 130)
    pd()
    circle(40, None, None)
    pu()
    setpos(270, 120)
    pd()
    circle(40, None, None)
    end_fill()
    return None

def myLake():
    '''
    None ---> None

    This function draws the lake that will appear in my art show and colors it.
    Executing the code does not print or return any relevant values; it only draws the picture.

    Ex:
    >>>myLake()
    
    >>>myLake(green)
    Traceback (most recent call last):
       File "<pyshell#0>", line 1, in <module>
         myLake(green)
    NameError: name 'green' is not defined
    '''
    pu()
    setpos(0, -100)
    seth(0)
    shape("circle") #Actually an oval
    shapesize(4, 25, 2) #Size of the Lake (h, w, outline)
    fillcolor("#0077be") #Color of lake
    end_fill()
    return None

def art_show_stub():
    '''
    None ---> None

    This function calls each individual function of my larger project to produce my art show using Turtle commands.
    It is otherwise known as the main function, holding all of the pieces together. It also defines the speed,
    screen resolution, and background color of the turtle graphics display.
    Executing the code does not print or return any relevant values; it only draws the picture.

    Ex:
    >>>art_show_stub()
    
    >>>art_show_stub(orange)
    Traceback (most recent call last):
       File "<pyshell#0>", line 1, in <module>
         art_show_stub(orange)
    NameError: name 'green' is not defined
    '''
    pass
    return None

def myLand_stub():
    '''
    None ---> None

    This function draws the ground or land that will appear in my art show and colors it.
    Executing the code does not print or return any relevant values; it only draws the picture.

    Ex:
    >>>myLand()
    
    >>>myLand(green)
    Traceback (most recent call last):
       File "<pyshell#0>", line 1, in <module>
         myLand_stub(green)
    NameError: name 'green' is not defined
    '''
    pass
    return None

def myHouse_stub():
    '''
    None ---> None

    This function draws the foundation and roof of the house that will appear in my art show and colors it.
    Executing the code does not print or return any relevant values; it only draws the picture.

    Ex:
    >>>myHouse_stub()

    >>>myHouse_stub(green)
    Traceback (most recent call last):
       File "<pyshell#0>", line 1, in <module>
         myHouse_stub(green)
    NameError: name 'green' is not defined
    '''
    pass
    return None

def myTree_stub():
    '''
    None ---> None

    This function draws the tree that will appear next to the house in my art show and colors it.
    Executing the code does not print or return any relevant values; it only draws the picture.

    Ex:
    >>>myTree_stub()
    
    >>>myTree_stub(green)
    Traceback (most recent call last):
       File "<pyshell#0>", line 1, in <module>
         myTree_stub(green)
    NameError: name 'green' is not defined
    '''
    pass
    return None

def myLake_stub():
    '''
    None ---> None

    This function draws the lake that will appear in my art show and colors it.
    Executing the code does not print or return any relevant values; it only draws the picture.

    Ex:
    >>>myLake_stub()
    
    >>>myLake_stub(green)
    Traceback (most recent call last):
       File "<pyshell#0>", line 1, in <module>
         myLake_stub(green)
    NameError: name 'green' is not defined
    '''
    pass
    return None
