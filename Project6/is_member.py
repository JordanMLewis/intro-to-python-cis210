'''
    Author: Jordan Mitchell Lewis
    Date: 02/13/2016
    Class: CIS 210, Winter 2016
    
    This file contains recursive and iterative methods for determining
    whether a target integer is an element in a given list.
'''

import doctest

def is_memberR(alist, target):
    '''
    (list, integer or float) ---> Boolean

    Function is_memberR will have two parameters, alist, a sorted list of integers and or floats,
    and target, a integer or float. All integers will have a value greater than or equal to 0.
    is_memberR will return True if target is an element of the the list, and False otherwise.

    >>> is_memberR([1, 3, 5, 7], 4) #Even number of items
    False

    >>> is_memberR([8, 6, 5, 4, 1], 4) #Odd number of items
    True

    >>> is_memberR([1, 2, 7.8, 3.5, 2.5, 4.6], 4.6) #List of integer and float items
    True
    '''
    alist = sorted(alist) #Sort list in ascending numerical order
    if len(alist) == 0: 
        return False
    else:
        midpoint = len(alist)//2 #new midpoint
        if alist[midpoint] == target:
            return True
        else:
            if target<alist[midpoint]: #if the target is less than that midpoint
                return is_memberR(alist[:midpoint], target) #look through everything before that midpoint
            else:
                return is_memberR(alist[midpoint+1:], target) #if not, look at everything after it

def is_memberI(alist, target):
    '''
    (list, integer or float) ---> Boolean

    Function is_memberI will have two parameters, alist, a sorted list of integers and or floats,
    and target, a integer or float. All integers will have a value greater than or equal to 0.
    is_memberI will return True if target is an element of the the list, and False otherwise.

    >>> is_memberI([1, 3, 5, 7], 4) #Even number of items
    False

    >>> is_memberI([8, 6, 5, 4, 1], 4) #Odd number of items 
    True

    >>> is_memberI([1, 2, 7.8, 3.5, 2.5, 4.6], 4.6) #List of integer and float items
    True
    
    '''
    alist = sorted(alist) #sort list in ascending numerical order
    firstIndex = 0
    lastIndex = len(alist) - 1 
    inTheList = False
    
    while firstIndex<=lastIndex and not inTheList:
        midpoint = (firstIndex + lastIndex)//2 #finds the median number
        if alist[midpoint] == target: #If the target is the midpoint, return True
            inTheList = True
        else:
            if target < alist[midpoint]: #If the target is less than the midpoint, search everything before that
                lastIndex = midpoint - 1
            else: #If not, search everything after the midpoint
                firstIndex = midpoint + 1
    return inTheList

def is_memberR_stub(alist, target):
    '''
    (list, integer or float) ---> Boolean

    Function is_memberR will have two parameters, alist, a sorted list of integers and or floats,
    and target, a integer or float. All integers will have a value greater than or equal to 0.
    is_memberR will return True if target is an element of the the list, and False otherwise.

    >>> is_memberR([1, 3, 5, 7], 4) #Even number of items
    False

    >>> is_memberR([8, 6, 5, 4, 1], 4) #Odd number of items
    True

    >>> is_memberR([1, 2, 7.8, 3.5, 2.5, 4.6], 4.6) #List of integer and float items
    True
    '''
    pass
    return #Boolean

def is_memberI_stub(alist, target):
    '''
    (list, integer or float) ---> Boolean

    Function is_memberI will have two parameters, alist, a sorted list of integers and or floats,
    and target, a integer or float. All integers will have a value greater than or equal to 0.
    is_memberI will return True if target is an element of the the list, and False otherwise.

    >>> is_memberI([1, 3, 5, 7], 4) #Even number of items
    False

    >>> is_memberI([8, 6, 5, 4, 1], 4) #Odd number of items 
    True

    >>> is_memberI([1, 2, 7.8, 3.5, 2.5, 4.6], 4.6) #List of integer and float items
    True
    
    '''
    pass
    return #Boolean
'''
doctest.testmod(verbose=True)
'''
