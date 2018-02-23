'''
    Author: Jordan Mitchell Lewis
    Date: 02/24/2016
    Class: CIS 210, Winter 2016
    
    This file contains recursive and iterative methods for determining
    whether a target integer is an element in a given list. This file
    also contains a home-made testing function.
    
    Challenge included in function test_is_member.
'''

import doctest

def is_memberR(alist, target):
    '''
    (list, number) ---> Boolean

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
    (list, number) ---> Boolean

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
    (list, number) ---> Boolean

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
    (list, number) ---> Boolean

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

def test_is_member(f):
    '''
    (function) ---> Boolean

    Function test_is_member takes one parameter, f, a function is_memberR or is_memberI,
    and executes every specified test case using that function. If there are no errors,
    the value of True is returned along with a print of a short description of the test.
    Otherwise, False will be returned along with test description. As per the project 7
    challenge, test_is_member will print a short message to the user specifying the 
    test case(s) that did not meet expected outcomes. 
    
    >>> test_is_member(is_memberR)
    11 test(s) attempted, 0 test(s) failed.
    True

    >>> test_is_member(is_memberI)
    11 test(s) attempted, 0 test(s) failed.
    True

    If and only if one or more of the specified test cases fail, the following will be printed:
    
    >> test_is_member(is_memberR)
    The following test cases have failed:

    Test case: 10
    List: [] 
    Target: 99 
    Got: True 
     ---> Expected: False

    Test case: 11
    List: [1, 2, 7.8, 3.5, 2.5, 4.6] 
    Target: 4.6 
    Got: False 
     ---> Expected: True

    11 test(s) attempted, 2 test(s) failed.
    False
    '''
    attempted = 0
    passed = 0
    failed = 0
    failedList = []
    failedTargets = []
    failedOutcomes = []
    failedOutcomesIndex = []
    i = 0
    
    testList = [[1, 3, 5, 7],               #Even number of items in list - False
                [23, 24, 25, 26, 27],       #Odd number of items in list - False
                [0, 1, 4, 5, 6, 8],         #Even number of items in list - True
                [0, 1, 2, 3, 4, 5, 6],      #Odd number of items in list - True
                [1, 3],                     #Target is first (zeroth) item in list - True
                [2, 10],                    #Target is last item in list - True
                [99, 100],                  #Short list - False
                [42],                       #One item list - True
                [43],                       #One item list - False
                [],                         #Empty list - False
                [1, 2, 7.8, 3.5, 2.5, 4.6]] #List of integer and float items - True
    targets = [4, 5, 4, 3, 1, 10, 101, 42, 44, 99, 4.6]
    expectedOutcomes = [False, False, True, True, True, True, False, True, False, False, True]

    for item in testList: #Try all test cases
         if f(item, targets[i]) == expectedOutcomes[i]: 
             attempted += 1
             passed += 1
             i += 1
         else: #Failed test cases
             attempted += 1
             failed += 1
             failedList.append(item)
             failedTargets.append(targets[i])
             failedOutcomes.append(expectedOutcomes[i])
             failedOutcomesIndex.append(i)
             i += 1

    i = 0
    
    if attempted == passed: #If everything works:
        print('{} test(s) attempted, {} test(s) failed.'.format(attempted, failed))
        return True
    else: #If there is at least one failed test case
        print('The following test cases have failed:')
        for item in failedList:
            print('')
            print('Test case:', failedOutcomesIndex[i]+1)
            print('List:', item, "\n" 'Target:', failedTargets[i], "\n" 'Got:', failedOutcomes[i],"\n","---> Expected:",not (failedOutcomes[i]))
            i += 1
        print('')
        print('{} test(s) attempted, {} test(s) failed.'.format(attempted, failed))
        return False

print(doctest.testmod())

